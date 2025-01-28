### Инсталляция приложения
1. Скачайте архив приложения;
2. Откройте консоль (cmd) от имени администратора и перейдите по пути расположения проекта;
3. Выполните команды 
4. python -m venv venv
5. venv\scripts\activate
6. pip install -r requirements.txt
7. cd backend
8. python manage.py runserver
9. Откройте браузер и перейдите по адресу: http://127.0.0.1:8000/

### Данные для входа

| Логин       | Пароль            | Роль                  | Организация  |
|-------------|-------------------|-----------------------|--------------|
| victor      | MyS3cr3tP@ssw0rd! | Клиент                | ООО "ФПК21"  |
| veronika    | MyS3cr3tP@ssw0rd! | Сервисная организация | ООО "ФНС"    |
| maxim       | MyS3cr3tP@ssw0rd! | Менеджер              | ООО "Силант" |

### Регистрация пользователя
1. Перейдите по адресу по адресу: http://127.0.0.1:8000/admin/
2. Авторизуйтесь под учёткой superuser
3. Создайте пользователя в разделе "Пользователи": http://127.0.0.1:8000/admin/app/user/add/
3. Вернитесь в IDE, откройте консоль в директории backend и выполните команды:
4. python manage.py shell
5. from django.contrib.auth.models import User
6. user = User.objects.get(username='username')
7. user.set_password('новый пароль')
8. user.save()
