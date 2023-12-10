from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Categorie(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Localizacao(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Campo(models.Model):
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    categorie = models.ForeignKey(Categorie, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="campo_liked", null=True)
    rating = models.PositiveSmallIntegerField(default=0)
    total_rating = models.PositiveIntegerField(default=0)
    num_evaluations = models.PositiveIntegerField(default=0)
    Monday_opening = models.TimeField(null=True)
    Monday_closing = models.TimeField(null=True)
    Tuesday_opening = models.TimeField(null=True)
    Tuesday_closing = models.TimeField(null=True)
    Wednesday_opening = models.TimeField(null=True)
    Wednesday_closing = models.TimeField(null=True)
    Thursday_opening = models.TimeField(null=True)
    Thursday_closing = models.TimeField(null=True)
    Friday_opening = models.TimeField(null=True)
    Friday_closing = models.TimeField(null=True)
    Saturday_opening = models.TimeField(null=True)
    Saturday_closing = models.TimeField(null=True)
    Sunday_opening = models.TimeField(null=True)
    Sunday_closing = models.TimeField(null=True)
    closed_days = models.DateField(null=True)
    image = models.ImageField(null=True, upload_to="images/")
    preco_hora = models.PositiveIntegerField(default=0)

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

    def get_opening_time_field(self, day_of_week):
        return getattr(self, f"{day_of_week}_opening", None)

    def get_closing_time_field(self, day_of_week):
        return getattr(self, f"{day_of_week}_closing", None)

    def get_closing_days(self):
        return self.closed_days


class Reserva(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.id} - {self.campo.title} - {self.start_time} to {self.end_time}"
