from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('machine_serial_number', 'model_of_equipment', 'client', 'service_company')
    search_fields = ('machine_serial_number', 'model_of_equipment__title')
    list_filter = ('service_company',)

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('machine', 'type_of_maintenance', 'date_of_maintenance', 'service_company')
    search_fields = ('machine__machine_serial_number', 'type_of_maintenance__title')
    list_filter = ('service_company',)

@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('machine', 'date_of_refusal', 'failure_node', 'service_company')
    search_fields = ('machine__machine_serial_number', 'failure_node__title')
    list_filter = ('service_company',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'user')
    search_fields = ('name',)

@admin.register(EquipmentModel)
class EquipmentModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(EngineModel)
class EngineModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(TransmissionModel)
class TransmissionModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(DrivingBridgeModel)
class DrivingBridgeModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(ControlledBridgeModel)
class ControlledBridgeModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(ServiceCompany)
class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user')
    search_fields = ('title',)

@admin.register(MaintenanceType)
class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(FailureNode)
class FailureNodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)