from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo
# Create your views here.

def todo(request):
  todo = Todo.objects.all()
  form = TodoForm()
  if request.method == "POST":
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('/')
  
  context = {'form':form, 'todo':todo}
  return render(request, 'todo/index.html', context)

def delt(request,pk):
  item = Todo.objects.get(id=pk)
  item.delete()
  messages.info(request, 'item removed! ')
  return redirect('/')