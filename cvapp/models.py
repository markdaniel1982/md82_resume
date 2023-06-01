from django.db import models
from django.contrib.auth.models import User

STATUS = {(0, "Draft"), (1, "Published")}

class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", default="Mark Daniel")
    content = models.TextField()
    added_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    class Meta:
        ordering = ['-added_on']

    def __str_(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["added_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"