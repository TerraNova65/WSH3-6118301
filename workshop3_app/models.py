from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Attend(models.Model):
    ATTN_Number = models.IntegerField()
    Movie_Name = models.CharField(max_length=255)
    Seat_Number = models.CharField(max_length=255)
    Show_Time = models.CharField(max_length=255)

    def __str__(self):
        return f"Attendance {self.ATTN_Number} for {self.Movie_Name}"
