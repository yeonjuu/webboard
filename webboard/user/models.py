from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model) :
    name = models.CharField(max_length =200)
    mail = models.CharField(max_length =200) 
    age = models.IntegerField(defult = 0)
    # phNum = models.TextField()
    # address = models.TextField()
    created_data = models.DataTimeField(
        defult = timezone.now
    )
    def __str__(self) :
        return self.title



