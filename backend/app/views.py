from django.shortcuts import render

def index(request):
    return render(request, '../templates/app/index.html')

def main(request):
    return render(request, '../templates/app/main.html')

def detail_machine(request):
    return render(request, '../templates/app/detail_machine.html')

def about_machine(request):
    return render(request, '../templates/app/about_machine.html')
