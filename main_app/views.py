from dataclasses import fields
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from main_app.forms import VocabWordForm
from .models import List, VocabWord, Student



# lists = [
#     List('Romeo & Juliet #1', 'Romeo and Juliet', 'Shakespeare', ['wherefor', 'hath', 'charnel']),
#     List('Romeo & Juliet #2', 'Romeo and Juliet', 'Shakespeare', ['amerce', 'caitiff', 'countervail']),
#     List('Cien Años de Soledad: Chapter 1-3', 'Cien Años de Soledad', 'Gabriel García Márquez', ['abejorreo', 'calcificado', 'hermetismo'])
# ]
        

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lists_index (request):
    lists = List.objects.all()
    return render(request, 'lists/index.html', { 'lists': lists })

def list_details(request, list_id):
    list = List.objects.get(id=list_id)
    #must instantiate our custom ModelForm class so it can be rendered inside our details page
    vocab_word_form = VocabWordForm() #store an instance of our form so we can pass it to the context object
    return render(request, 'lists/details.html', {'list': list, 'vocab_word_form': vocab_word_form})

def add_word(request, list_id):
    #create a ModelForm instance from the data passed from the new word form...that data is represented by request.POST!!!
    print("request!!!!" + request.POST)
    form = VocabWordForm(request.POST)
    #validate the form
    if form.is_valid():
        #dont save form to db until it has the list_id assigned
        new_word = form.save(commit=False)
        new_word.list_id = list_id
        new_word.save()
    return redirect('details', list_id=list_id)

    
class ListCreate(CreateView): #must inherit from CreateView for our class-based view (CBV) to create data
    model = List
    fields = '__all__'

class ListUpdate(UpdateView):
    model = List
    fields = '__all__'

class ListDelete(DeleteView):
    model = List
    success_url = '/lists/'

class StudentList(ListView):
    model = Student
    fields = '__all__'

#  Note: Everything in a Python module is automatically exported, thus, the Cat class and 
#the cats list will be accessable in other modules.

