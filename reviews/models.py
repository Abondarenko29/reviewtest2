from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name="reviews", null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
