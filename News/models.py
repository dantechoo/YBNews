from django.db import models

# Create your models here.
class News_info(models.Model):
    cat = models.CharField(max_length=10, null=False) # category
    name = models.CharField(max_length=20, null=False) # nickname
    title = models.CharField(max_length=50, null=False) # title
    message = models.TextField(null=False) # content
    pubtime = models.DateTimeField(auto_now=True) # publish time
    enabled = models.BooleanField(default=False) # show or hide
    press = models.IntegerField(default=0) # click times

    def __str__(self):
        return self.title