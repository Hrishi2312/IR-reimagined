from django.shortcuts import render
from django import forms
from .models import Document
from .processing import *

def homepage(request):
    context = {'words': unique_words_all}
    return render(request, 'main/index.html', context)

def retrieve(request):
    if request.method == 'POST':
        query = request.POST['query']
        output = processing(query)
    connect = []
    files = []
    input_query = output[0]
    query_words = output[1]
    if output[2]:
        connect = output[2]
    values = output[3]
    if output[4]:
        files = output[4]
    context = {'input_query': input_query,
               'query_words': query_words,
               'connect': connect,
               'values': values,
               'files': files}
    return render(request, 'main/retrieve.html', context)
