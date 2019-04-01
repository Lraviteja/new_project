from django.db import models

# Create your models here.
class Categories(models.Model):
    categories_text = models.CharField(max_length=30)

    def __str__(self):
        return self.categories_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    tittle = models.CharField(max_length=10)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)

    def __str__(self):
        return self.answer_text


class Comment(models.Model):
    comment_text = models.CharField(max_length=500)

    def __str__(self):
        return self.comment_text

