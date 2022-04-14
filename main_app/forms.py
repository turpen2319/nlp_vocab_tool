from dataclasses import fields
from django.forms import ModelForm
from .models import VocabWord

# I want to show a form to add a vocab word on the list detail page, I need to create
# my own custom ModelForm. When using Class-Based Views (CBVs), they generated these forms
# automatically, but I don't want the user to leave the details page to add a new word.

# 1. Generate a feeding's inputs inside of the <form> tag we provide.
# 2. Be used to validate the posted data by calling is_valid().
# 3. Persist the model instance to the database by calling save() on the instance of the ModelForm.

class VocabWordForm(ModelForm):
    class Meta:
        model = VocabWord
        fields = ['word', 'definition', 'example_sentence']