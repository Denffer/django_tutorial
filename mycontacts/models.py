from django.db import models

class Contact(models.Model):
    """ For other types of fields for different purpose, please refer to: https://docs.djangoproject.com/ja/1.10/ref/models/fields/ """
    
    name = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
