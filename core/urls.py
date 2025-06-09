from django.urls import path
from core import views

app_name = 'risk'
urlpatterns = [
    path('', views.risk, name='calculate_risk'),
    path('view', views.risk_view, name='calculate_risk'),
    path('view/rules/with/cost', views.view_fuzzy_rules_with_cost, name='view_fuzzy_rules_with_cost'),
    path('view/rules/without/cost', views.view_fuzzy_rules_without_cost, name='view_fuzzy_rules_without_cost'),
    path('download/rules/with/cost', views.download_fuzzy_rules_with_cost, name='download_fuzzy_rules_with_cost'),
    path('download/rules/without/cost', views.download_fuzzy_rules_without_cost, name='download_fuzzy_rules_without_cost'),
]