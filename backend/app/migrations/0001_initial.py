# Generated by Django 5.1.5 on 2025-01-23 08:34

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('address', models.CharField(default='Не указан', max_length=255, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='ControlledBridgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='DrivingBridgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='EquimentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='FailureNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('guest', 'Гость'), ('client', 'Клиент'), ('service', 'Сервисная организация'), ('manager', 'Менеджер')], default='guest', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_serial_number', models.CharField(max_length=120, verbose_name='Заводской номер машины')),
                ('engine_serial_number', models.CharField(max_length=120, verbose_name='Заводской номер двигателя')),
                ('transmission_serial_number', models.CharField(max_length=120, verbose_name='Заводской номер трансмиссии')),
                ('driving_bridge_serial_number', models.CharField(max_length=120, verbose_name='Заводской номер ведущего моста')),
                ('controlled_bridge_serial_number', models.CharField(max_length=120, verbose_name='Заводской номер управляемого моста')),
                ('supply_contract', models.CharField(blank=True, max_length=120, null=True, verbose_name='Договор поставки')),
                ('date_of_shipment', models.DateTimeField(blank=True, null=True, verbose_name='Дата отгрузки с завода')),
                ('consignee', models.CharField(blank=True, max_length=120, null=True, verbose_name='Грузополучатель')),
                ('delivery_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес поставки')),
                ('equipment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комплектация')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='machines', to='app.client', verbose_name='Клиент')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.enginemodel', verbose_name='Модель двигателя')),
                ('model_of_a_controlled_bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.controlledbridgemodel', verbose_name='Модель управляемого моста')),
                ('model_of_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equimentmodel', verbose_name='Модель техники')),
                ('model_of_the_drivig_bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.drivingbridgemodel', verbose_name='Модель ведущего моста')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicecompany', verbose_name='Сервисная компания')),
                ('transmission_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transmissionmodel', verbose_name='Модель трансмиссии')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_maintenance', models.DateTimeField(verbose_name='Дата проведения ТО')),
                ('maintenance_development', models.IntegerField(verbose_name='Наработка')),
                ('order_number', models.CharField(max_length=100, verbose_name='Номер заказ-наряда')),
                ('order_date', models.DateTimeField(verbose_name='Дата заказ-наряда')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.machine', verbose_name='Экземпляр машины')),
                ('type_of_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.maintenancetype', verbose_name='Вид ТО')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicecompany', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Техническое обслуживание',
                'verbose_name_plural': 'Техническое обслуживание',
            },
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_refusal', models.CharField(max_length=120, verbose_name='Дата отказа')),
                ('complaints_development', models.IntegerField(verbose_name='Наработка')),
                ('description_of_the_failure', models.TextField(verbose_name='Описание отказа')),
                ('used_spare_parts', models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')),
                ('date_of_restoration', models.DateTimeField(verbose_name='Дата восстановления')),
                ('machine_downtime', models.TextField(editable=False, verbose_name='Время простоя техники')),
                ('failure_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.failurenode', verbose_name='Узел отказа')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.machine')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recoverymethod', verbose_name='Способ восстановления')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicecompany', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
            },
        ),
    ]
