from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    group = models.CharField(max_length=255)


class Category(models.Model):
    category = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.category


class Projects(models.Model):
    project_name = models.CharField(max_length=255)


class ProjectsInfo(models.Model):
    project_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)


class Deadlines(models.Model):
    project_id = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    data = models.DateTimeField()
    files = models.FileField(upload_to='media/%Y/%m/%d/')



