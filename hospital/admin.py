
from django.contrib import admin
from .models import Doctor,Appointment,PatientDischargeDetails, VaccineInfo,Patient, VaccineSchedule, VaccineScheduleReminder, Profile
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

admin.site.register(VaccineSchedule)

admin.site.register(VaccineScheduleReminder)
admin.site.register(Profile)
admin.site.register(VaccineInfo)