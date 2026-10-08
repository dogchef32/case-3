from django.shortcuts import render
from .forms import NameForm
from .models import Visitor

def home(request):
    greeting = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            visitor = Visitor.objects.create(name=form.cleaned_data['name'])
            greeting = f'Привет, {visitor.name}! Рады тебя видеть!'
            form = NameForm()
    else:
        form = NameForm()
    return render(request, 'greetings/home.html', {'form': form, 'greeting': greeting})
