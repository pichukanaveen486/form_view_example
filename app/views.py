from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from app.forms import *
from app.models import *
from django.http import HttpResponse




class Student_data_Form(FormView):
    template_name='StudentForm.html'
    form_class=StudentForm

    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))
    







class friendshipList(FormView):
    template_name='friendshipList.html'
    form_class=FriendshipList

    def form_valid(self, form):
        form.save()
        return HttpResponse('insert_data_SuryaGFList is done successfully')
