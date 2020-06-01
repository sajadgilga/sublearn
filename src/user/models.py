from PIL import Image
from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    score = models.FloatField()
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics') #todo upload_to

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size =  (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Payment(models.Model):
    amount = models.IntegerField()
    time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Subtitle(models.Model):
    text = models.CharField()
    upload_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Exam(models.Model):
    time = models.DateTimeField()
    score = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    words = models.ManyToManyField(Word)


class Word(models.Model):
    english_word = models.CharField()
    translation = models.CharField()
    difficulty = models.CharField()


class Flashcard(models.Model):
    learnt = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

