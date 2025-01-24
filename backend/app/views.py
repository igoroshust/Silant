from django.shortcuts import render
from .forms import SearchForm
from .models import *

# def index(request):
#     return render(request, '../templates/app/index.html')

def main(request):
    return render(request, '../templates/app/main.html')

def detail_machine(request):
    return render(request, '../templates/app/detail_machine.html')

def about_machine(request):
    return render(request, '../templates/app/about_machine.html')

def index_view(request):
    form = SearchForm()
    results = []

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Выполняем поск в базе данных
            results = Machine.objects.filter(machine_serial_number__icontains=query)

    return render(request, '../templates/app/index.html', {'form': form, 'results': results})
