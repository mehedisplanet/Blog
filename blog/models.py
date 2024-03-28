from django.db import models

# Create your models here.
class Blog(models.Model):
    image=models.ImageField(upload_to="media/")
    title=models.CharField(max_length=150)
    topic=models.CharField(max_length=50)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} {self.title}"