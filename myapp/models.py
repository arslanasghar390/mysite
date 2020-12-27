from django.db import models
# Create your models here.

class Contact(models.Model):
    firstname= models.CharField(max_length=200,null=True)
    lastname= models.CharField(max_length=200,null=True)
    email= models.EmailField()
    subject =models.TextField()
   
    def __str__(self):
        return self.firstname
    
class upload(models.Model):
 notefile=models.FileField(upload_to="media", null=True)
 title= models.CharField(max_length=200, default="" , null=True)

 def __str__(self):
        return self.title
    