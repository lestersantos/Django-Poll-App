from django.db import models

# Create your models here.
"""
It contains essential fields and behaviors of the data
you're storing. Each model maps to a single database table.
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

"""
python manage.py makemigrations polls

Migrations are Django's way of propagating changes you make to your
models into your database schema.

Migrations like as a version control system for your database schema.
makemigrations - commit
migrate - push
"""