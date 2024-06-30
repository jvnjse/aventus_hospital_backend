from django.urls import path
from . import views

urlpatterns = [
    path("patients/", views.patients_list),
    path("patients/<str:pk>/", views.patient_detail),
    path("appointments/", views.appointments_list),
    path("appointments/<str:pk>/", views.appointment_detail),
    path("upload/", views.upload_excel),
]
