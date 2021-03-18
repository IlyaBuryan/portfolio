from django.db import models
from datetime import datetime


class Courses(models.Model):
    number = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=70)
    result = models.CharField(max_length=150, blank=True)
    status = models.BooleanField(default=0, name="Completed")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['number']

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Classes(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lessons = models.CharField(max_length=100)

    def __str__(self):
        return self.lessons

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'


class News(models.Model):
    title = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None)
    datetime = models.DateTimeField(default=datetime.now())
    picture = models.ImageField(default=None)
    status = models.BooleanField(default=1, name="Completed")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField(verbose_name='message')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
