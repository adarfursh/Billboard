from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    post_content = models.CharField(max_length=500)
    post_author = models.CharField(max_length= 24)

    def __str__ (self):
        return self.post_title