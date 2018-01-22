from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.11/ref/models/fields/
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField()
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    user = models.CharField(max_length=100)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()
        
    def __str__(self):
        return self.comment





    
    
