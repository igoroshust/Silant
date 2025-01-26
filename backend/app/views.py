from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import SearchForm
from .models import *

# def index(request):
#     return render(request, '../templates/app/index.html')

# def main(request):
#     return render(request, '../templates/app/main.html')

def main_view(request):
    """Возвращаем данные каждой таблицы"""
    machines = Machine.objects.all()
    maintenances = Maintenance.objects.all()
    complaints = Complaints.objects.all()

    context = {
        'machines': machines,
        'maintenances': maintenances,
        'complaints': complaints,
    }

    return render(request, '../templates/app/main.html', context)

def detail_machine(request):
    return render(request, '../templates/app/detail_machine.html')

def about_machine(request):
    return render(request, '../templates/app/about_machine.html')

def index_view(request):
    """Страница для клиента (неавторизованный пользователь)"""
    form = SearchForm()
    results = []

    # Проверяем, был ли запрос методом GET
    if request.method == 'GET':
        form = SearchForm(request.GET)
        # Проверяем, была ли форма отправлена и валидна
        if form.is_valid():
            query = form.cleaned_data['query']
            # Выполняем поиск в базе данных только если форма валидна
            results = Machine.objects.filter(machine_serial_number__icontains=query)

    # Обработка авторизации
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})  # Успешная авторизация
        else:
            # Отладочные сообщения
            print(f"Попытка входа с именем пользователя: {username}")
            print(f"Пароль: {password}")
            return JsonResponse({'success': False, 'message': 'Неверный логин или пароль.'}, status=400)

    # Передаём информацию о наличии результатов в контекст
    has_results = bool(results)

    return render(request, '../templates/app/index.html', {
        'form': form,
        'results': results,
        'has_results': has_results,  # Передаем has_results в контекст
    })

