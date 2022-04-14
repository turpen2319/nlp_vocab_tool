from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
#import all the functionality of the nlp file here...use those funcs to create data in the db

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    reading_level = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('students_detail', kwargs={'pk': self.id})
    
class List(models.Model):
    title = models.CharField(max_length=200)
    origin_text_title = models.CharField(max_length=200)
    text_author = models.CharField(max_length=200)
    reading_level = models.CharField(max_length=50)
    #many to many field
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'list_id': self.id})

class VocabWord(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField(max_length=1000)
    example_sentence = models.TextField(max_length=1000)
    #make another model for sentences later...M:M words with sentences...show user sentences that contain the word and let them add to examples
    
    # create a list_id column in the word table
    list = models.ForeignKey(List, on_delete=models.CASCADE) #should I do this? Would it be good to keep these words if they aren't being used?

    def __str__(self):
        return f'Word: {self.word} \nDefinition: {self.definition}'



