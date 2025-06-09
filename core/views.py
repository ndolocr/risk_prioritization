import io
import urllib
import base64
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
from django.shortcuts import render


# Create your views here.

def risk(request):
    cost = ctrl.Antecedent(np.arange(0, 11, 1), 'cost')
    exploitability = ctrl.Antecedent(np.arange(0, 11, 1), 'exploitability')
    exploitability['low'] = fuzz.trimf(exploitability.universe, [0, 0, 5])
    exploitability['medium'] = fuzz.trimf(exploitability.universe, [0, 5, 10])
    exploitability['high'] = fuzz.trimf(exploitability.universe, [5, 10, 10])

    affected_users = ctrl.Antecedent(np.arange(0, 11, 1), 'affected_users')
    affected_users['low'] = fuzz.trimf(affected_users.universe, [0, 0, 5])
    affected_users['medium'] = fuzz.trimf(affected_users.universe, [0, 5, 10])
    affected_users['high'] = fuzz.trimf(affected_users.universe, [5, 10, 10])

    discoverability = ctrl.Antecedent(np.arange(0, 11, 1), 'discoverability')
    discoverability['low'] = fuzz.trimf(discoverability.universe, [0, 0, 5])
    discoverability['medium'] = fuzz.trimf(discoverability.universe, [0, 5, 10])
    discoverability['high'] = fuzz.trimf(discoverability.universe, [5, 10, 10])

    reproducibility = ctrl.Antecedent(np.arange(0, 11, 1), 'reproducibility')
    reproducibility['low'] = fuzz.trimf(reproducibility.universe, [0, 0, 5])
    reproducibility['medium'] = fuzz.trimf(reproducibility.universe, [0, 5, 10])
    reproducibility['high'] = fuzz.trimf(reproducibility.universe, [5, 10, 10])

    damage_potential = ctrl.Antecedent(np.arange(0, 11, 1), 'damage_potential')
    damage_potential['low'] = fuzz.trimf(damage_potential.universe, [0, 0, 5])
    damage_potential['medium'] = fuzz.trimf(damage_potential.universe, [0, 5, 10])
    damage_potential['high'] = fuzz.trimf(damage_potential.universe, [5, 10, 10])



    risk_score = ctrl.Consequent(np.arange(0, 11, 1), 'risk_score')
    risk_score['low'] = fuzz.trimf(risk_score.universe, [0, 0, 5])
    risk_score['medium'] = fuzz.trimf(risk_score.universe, [0, 5, 10])
    risk_score['high'] = fuzz.trimf(risk_score.universe, [5, 10, 10])

    rules = [
        ctrl.Rule(damage_potential['high'] & exploitability['high'], risk_score['high']),
        ctrl.Rule(reproducibility['high'] & affected_users['high'], risk_score['high']),
        ctrl.Rule(discoverability['low'] & exploitability['low'], risk_score['low']),
        ctrl.Rule(damage_potential['medium'] | affected_users['medium'], risk_score['medium']),
        ctrl.Rule(exploitability['low'] & damage_potential['low'], risk_score['low']),
    ]

    risk_ctrl = ctrl.ControlSystem(rules)
    risk_sim = ctrl.ControlSystemSimulation(risk_ctrl)

    # Get inputs from form or set defaults
    if request.method == 'POST':
        exploitability_input = int(request.POST.get('exploitability'))
        affected_users_input = int(request.POST.get('affected_users'))
        discoverability_input = int(request.POST.get('discoverability'))
        reproducibility_input = int(request.POST.get('reproducibility'))
        damage_potential_input = int(request.POST.get('damage_potential'))
    else:
        exploitability = affected_users = discoverability = reproducibility = damage_potential = 5
        return render(request, 'core/risk.html')

    risk_sim.input['exploitability'] = exploitability_input
    risk_sim.input['affected_users'] = affected_users_input
    risk_sim.input['discoverability'] = discoverability_input
    risk_sim.input['reproducibility'] = reproducibility_input
    risk_sim.input['damage_potential'] = damage_potential_input

    risk_sim.compute()
    result = risk_sim.output['risk_score']

    # Plot risk score output
    plt.figure()
    risk_score.view(sim=risk_sim)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    input_dict = {
        'exploitability': exploitability, 
        'affected_users': affected_users, 
        'discoverability': discoverability, 
        'reproducibility': reproducibility, 
        'damage_potential': damage_potential
        }
    
    context = {
        'result': round(result, 2),
        'graph': graph,
        'input': input_dict,
    }

    return render(request, 'core/risk.html', context)
    

    



# # Antecedent
# def createCostAntecedent():
#     cost = ctrl.Antecedent(np.arange(0, 11, 1), 'cost')
#     return cost

# def createExploitabilityAntecedent():
#     exploitability = ctrl.Antecedent(np.arange(0, 11, 1), 'exploitability')
#     return exploitability

# def createAffectedUsersAntecedent():
#     affected_users = ctrl.Antecedent(np.arange(0, 11, 1), 'affected_users')
#     return affected_users

# def createDiscoverabilityAntecedent():
#     discoverability = ctrl.Antecedent(np.arange(0, 11, 1), 'discoverability')
#     return discoverability

# def createReproducibilityAntecedent():
#     reproducibility = ctrl.Antecedent(np.arange(0, 11, 1), 'reproducibility')
#     return reproducibility
    
# def createDamagePotentialAntecedent():
#     damage_potential = ctrl.Antecedent(np.arange(0, 11, 1), 'damage_potential')
#     return damage_potential

# # Consequent
# def riskRankingValueConsequent():
#     risk_ranking = ctrl.Consequent(np.arange(0, 11, 1), 'risk_ranking_value')
#     return risk_ranking

# def riskQuantificationValueConsequent():
#     risk_quantification = ctrl.Consequent(np.arange(0, 11, 1), 'risk_quantification_value')
#     return risk_quantification
