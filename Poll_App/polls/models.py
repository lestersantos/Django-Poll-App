from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
"""
Models, databse layout (DRY) Don't repeat youself

It contains essential fields and behaviors of the data
you're storing. Each model maps to a single database table.
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    """
    Fixing the bug Question.was_published_recently() by overriding? maybe
    """
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
"""
python manage.py makemigrations polls

Migrations are Django's way of propagating changes you make to your
models into your database schema.

Migrations like as a version control system for your database schema.
makemigrations - commit
migrate - push
"""