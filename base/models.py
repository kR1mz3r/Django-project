from django.db import models
from django.urls import reverse
from project.models import Task

class BaseProjectTask(models.Model):
    project = models.CharField(verbose_name='Название проекта')
    task = models.ManyToManyField(Task, verbose_name='Список задач')
    description = models.TextField()
    def get_absolute_url(self):
        return reverse('base_detail', kwargs={"pk": self.pk})
    class Meta:
        verbose_name = 'Проекты (архив)'
        verbose_name_plural = 'Проекты (архив)'

