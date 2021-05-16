from django.shortcuts import render
from django import forms
from .models import Document
from .words import *
from .Node import *

def homepage(request):
    context = {'words': unique_words_all}
    return render(request, 'main/index.html', context)
