from django.urls import path
from core import views

app_name = 'risk'
urlpatterns = [
    path('with/cost/for/windows', views.risk_with_cost_for_windows, name='risk_with_cost_for_windows'),
    path('with/cost/for/macbook', views.risk_with_cost_for_macbook, name='risk_with_cost_for_macbook'),
    path('without/cost/for/windows', views.risk_without_cost_for_windows, name='risk_without_cost_for_windows'),    
    path('without/cost/for/macbook', views.risk_without_cost_for_macbook, name='risk_without_cost_for_macbook'),

    path('view/rules/with/cost', views.view_fuzzy_rules_with_cost, name='view_fuzzy_rules_with_cost'),
    path('view/rules/for/dream-c', views.view_fuzzy_rules_for_dream_c, name='view_fuzzy_rules_for_dream_c'),
    path('view/rules/without/cost', views.view_fuzzy_rules_without_cost, name='view_fuzzy_rules_without_cost'),
    path('view/rules/for/cost/only', views.view_fuzzy_rules_for_cost_only, name='view_fuzzy_rules_for_cost_only'),
    
    path('download/dream-c/rules', views.download_dream_c_fuzzy_rules, name='download_dream_c_fuzzy_rules'),
    path('download/rules/with/cost', views.download_fuzzy_rules_with_cost, name='download_fuzzy_rules_with_cost'),
    path('download/rules/without/cost', views.download_fuzzy_rules_without_cost, name='download_fuzzy_rules_without_cost'),
    path('download/rules/for/cost/only', views.download_fuzzy_rules_for_cost_only, name='download_fuzzy_rules_for_cost_only'),
    path('risk_with_cost_from_generated_list', views.risk_with_cost_from_generated_list, name='risk_with_cost_from_generated_list'),
    path('risk_with_cost_from_generated_list_with_ascending_cost', views.risk_with_cost_from_generated_list_with_ascending_cost, name='risk_with_cost_from_generated_list_with_ascending_cost'),
    path('with/varying/dread/and/constant/cost/parameters', views.risk_with_varying_dread_and_constant_cost_parameters, name='risk_with_varying_dread_and_constant_cost_parameters'),
    path('with/varying/cost/and/constant/dread/parameters', views.risk_with_varying_cost_and_constant_dread_parameters, name='risk_with_varying_cost_and_constant_dread_parameters'),
    path('with/varying/cost/and/constant/dread/parameters/to/excel', views.risk_with_varying_cost_and_constant_dread_parameters_to_excel, name='risk_with_varying_cost_and_constant_dread_parameters_to_excel'),
    path('with/varying/dread/and/constant/cost/parameters/to/excel', views.risk_with_varying_dread_and_constant_cost_parameters_to_excel, name='risk_with_varying_dread_and_constant_cost_parameters_to_excel'),
]