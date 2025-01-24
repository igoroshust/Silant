from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Machine)
admin.site.register(Maintenance)
admin.site.register(Complaints)
admin.site.register(Client)
admin.site.register(EquipmentModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DrivingBridgeModel)
admin.site.register(ControlledBridgeModel)
admin.site.register(ServiceCompany)
admin.site.register(MaintenanceType)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
