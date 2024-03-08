from django.db import models

# Create your models here.

class Developer(models.Model):

    dev_id = models.CharField(max_length = 40,primary_key=True)
    password = models.CharField(max_length = 20,null=False)
    name = models.CharField(max_length = 20)
    manager = models.BooleanField(default=False)

    class Meta:
        db_table = "developer"
