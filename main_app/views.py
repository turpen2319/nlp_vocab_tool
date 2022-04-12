from django.shortcuts import render
from django.http import HttpResponse

class List:
    def __init__(self, title, origin_text, text_author, vocab_words):
        self.title = title
        self.origin_text = origin_text
        self.text_author = text_author
        self.vocab_words = vocab_words

lists = [
    List('Romeo & Juliet #1', 'Romeo and Juliet', 'Shakespeare', ['wherefor', 'hath', 'charnel']),
    List('Romeo & Juliet #2', 'Romeo and Juliet', 'Shakespeare', ['amerce', 'caitiff', 'countervail']),
    List('Cien Años de Soledad: Chapter 1-3', 'Cien Años de Soledad', 'Gabriel García Márquez', ['abejorreo', 'calcificado', 'hermetismo'])
]
        

# Create your views here.

def home(request):
    return HttpResponse('<h1>Home page</h1>')


def about(request):
    return render(request, 'about.html')

def lists_index (request):
    return render(request, 'lists/index.html', { 'lists': lists })


#  Note: Everything in a Python module is automatically exported, thus, the Cat class and 
#the cats list will be accessable in other modules.