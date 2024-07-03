from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_project', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    files = models.FileField(upload_to='project/task_files/%Y/%m/%d/')
    updated_files = models.FileField(upload_to='project/update_task_files/%Y/%m/%d/', blank=True, null=True)
    updated_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('view_task', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']



