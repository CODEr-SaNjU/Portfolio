from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main_func(request):
    return render(request, 'main.html')


