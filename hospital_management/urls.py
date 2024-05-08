from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointment/', include('appointment.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('service/', include('service.urls')),

]
