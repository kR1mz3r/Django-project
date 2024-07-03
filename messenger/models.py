import hashlib
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    conversation_id = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.conversation_id is None:
            user_ids = [str(self.sender), str(self.recipient)]
            sorted_user_ids = '-'.join(sorted(user_ids))
            conversation_hash = hashlib.sha256(sorted_user_ids.encode()).hexdigest()
            self.conversation_id = conversation_hash
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient}'

    class Meta:
        ordering = ('timestamp',)
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'






