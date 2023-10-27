from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Categorie(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(null=True, blank=True, upload_to="media/images/")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Campo(models.Model):
    title = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=100)
    content = models.TextField()
    categorie = models.ForeignKey(Categorie, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    added_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="campo_liked")
    rating = models.PositiveSmallIntegerField(default=0)
    total_rating = models.PositiveIntegerField(default=0)
    num_evaluations = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def calculate_average_rating(self):
        if self.num_evaluations > 0:
            self.rating = round(self.total_rating / self.num_evaluations)
        else:
            self.rating = 0
        self.save()

