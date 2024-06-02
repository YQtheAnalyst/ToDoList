from django.db import models

# Create your models here.
# This model eauqls to you ccreate a table in SQL; That's why you need to migrate!

class task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.title
    
