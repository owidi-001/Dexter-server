from django.db import models

# Create your models here.
class Notification(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timeModified=models.DateTimeField(auto_now_add=True,auto_created=True)
    read=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering=["-timeModified"]