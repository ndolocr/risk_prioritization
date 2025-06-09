from django.urls import path
from core import views

app_name = 'risk'
urlpatterns = [
    path('', views.risk, name='calculate_risk'),
    path('view', views.risk_view, name='calculate_risk'),
]