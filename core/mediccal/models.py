from django.db import models
class Medical(models.Model):
    # user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    # eyeName=models.CharField(max_length=100)
    # receipe_description=models.TextField()
    Eimage=models.ImageField(upload_to='medical')
# class User
# Create your models here.
