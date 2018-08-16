# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.FileField(upload_to='pictures/')
    
    # borrow_date = models.DateTimeField(default=timezone.now())
    STATUS = Choices('borrowed', 'available')

    status = StatusField()
    borrowed_at = MonitorField(monitor='status', when=['available'])


    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.ForeignKey( Book, on_delete=models.CASCADE )
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


