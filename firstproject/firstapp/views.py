from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from .models import student
from .forms import studentform
from django.urls import reverse_lazy

# def homepage(request):
#     return render(request,'home.html')

class studentlist(ListView):

   model=student
   template_name='home.html'
   ordering=['-update_date']

   #ordering=['-id'] #to get recent one in the blog 

   
class studentdetailview(DetailView):
    model = student
    template_name='studentdetail.html'


class studentcreateview(CreateView):
    model = student
    form=studentform
    template_name = "studentcreate.html"
    fields='__all__'


class studentupdateview(UpdateView):
   model=student 
   template_name='studentupdate.html'
   fields='__all__'

class studentdeleteview(DeleteView):
    model = student
    template_name = "studentdelete.html"
    success_url=reverse_lazy('home')
