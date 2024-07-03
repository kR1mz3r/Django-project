from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    middle_name = models.CharField(max_length=150, verbose_name='Отчество')
    photo = models.ImageField(upload_to='photos/avatar/', verbose_name='Аватар', blank=True)
    department = models.CharField(max_length=150, verbose_name='Отдел')
    role = models.CharField(max_length=150, verbose_name='Должность')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.middle_name
    class Meta:
        verbose_name = 'Доп. информация о пользоваетеле'
        verbose_name_plural = 'Доп. информация'





