from django.urls import path
from core import views

app_name = 'risk'
urlpatterns = [
    path('with/cost/for/windows', views.risk_with_cost_for_windows, name='risk_with_cost_for_windows'),
    path('with/cost/for/macbook', views.risk_with_cost_for_macbook, name='risk_with_cost_for_macbook'),
    path('without/cost/for/windows', views.risk_without_cost_for_windows, name='risk_without_cost_for_windows'),    
    path('without/cost/for/macbook', views.risk_without_cost_for_macbook, name='risk_without_cost_for_macbook'),

    path('view/rules/with/cost', views.view_fuzzy_rules_with_cost, name='view_fuzzy_rules_with_cost'),
    path('view/rules/without/cost', views.view_fuzzy_rules_without_cost, name='view_fuzzy_rules_without_cost'),
    path('view/rules/for/cost/only', views.view_fuzzy_rules_for_cost_only, name='view_fuzzy_rules_for_cost_only'),
    path('download/rules/with/cost', views.download_fuzzy_rules_with_cost, name='download_fuzzy_rules_with_cost'),
    path('download/rules/without/cost', views.download_fuzzy_rules_without_cost, name='download_fuzzy_rules_without_cost'),
    path('download/rules/for/cost/only', views.download_fuzzy_rules_for_cost_only, name='download_fuzzy_rules_for_cost_only'),
]