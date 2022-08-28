from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models

from django.db import models
class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)