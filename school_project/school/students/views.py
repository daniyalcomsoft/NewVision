from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from .models import gr_register
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def index(request):
    all_gr_reg = gr_register.objects.all()
    #template is the variable in this variable we tell that which file we are using and where is that (this is in students one)

    # context is the name of dictionary and context is the standard name. Dictionary send our data from views to index

    return render(request, 'students/index.html', {'all_gr_reg': all_gr_reg})

def detail(request, gr_no):

    try:
        gr = gr_register.objects.get(pk=gr_no)
    except gr_register.DoesNotExist:
        raise Http404("This ID Does Not Exist")

    return render(request, 'students/detail.html', {'gr':gr})





# Create your views here.
