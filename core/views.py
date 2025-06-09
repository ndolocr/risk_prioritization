import io
import urllib
import base64
import itertools
import numpy as np
import skfuzzy as fuzz
import matplotlib
matplotlib.use('Agg')
from datetime import datetime
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.text import slugify



# Create your views here.

def risk(request):
    if request.method == 'POST':
        exploitability_input = int(request.POST.get('exploitability'))
        affected_users_input = int(request.POST.get('affected_users'))
        discoverability_input = int(request.POST.get('discoverability'))
        reproducibility_input = int(request.POST.get('reproducibility'))
        damage_potential_input = int(request.POST.get('damage_potential'))

        # cost = ctrl.Antecedent(np.arange(0, 11, 1), 'cost')
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
            'exploitability': exploitability_input, 
            'affected_users': affected_users_input, 
            'discoverability': discoverability_input, 
            'reproducibility': reproducibility_input, 
            'damage_potential': damage_potential_input
            }
        
        context = {
            'graph': graph,
            'result': result,            
            'input': input_dict,
        }

        return render(request, 'core/risk.html', context)
    
    return render(request, 'core/risk.html')
    

  # Use a non-interactive backend suitable for servers/macOS


def risk_view(request):
    if request.method == 'POST':
        exploitability_input = int(request.POST.get('exploitability'))
        affected_users_input = int(request.POST.get('affected_users'))
        discoverability_input = int(request.POST.get('discoverability'))
        reproducibility_input = int(request.POST.get('reproducibility'))
        damage_potential_input = int(request.POST.get('damage_potential'))

        # cost = ctrl.Antecedent(np.arange(0, 11, 1), 'cost')
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

        risk_sim.input['exploitability'] = exploitability_input
        risk_sim.input['affected_users'] = affected_users_input
        risk_sim.input['discoverability'] = discoverability_input
        risk_sim.input['reproducibility'] = reproducibility_input
        risk_sim.input['damage_potential'] = damage_potential_input

        risk_sim.compute()
        result = risk_sim.output['risk_score']

        # Create a plot
        fig, ax = plt.subplots()
        ax.bar(['Risk Score'], [result], color='orange')
        ax.set_ylim([0, 10])
        ax.set_ylabel('Risk Level')
        ax.set_title('Fuzzy Risk Score')

        # Save plot to memory
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Encode image to base64
        graph = base64.b64encode(image_png).decode('utf-8')

        input_dict = {
            'exploitability': exploitability_input, 
            'affected_users': affected_users_input, 
            'discoverability': discoverability_input, 
            'reproducibility': reproducibility_input, 
            'damage_potential': damage_potential_input
            }
        
        # Pass risk score and graph to template
        context = {
            'graph': graph,
            'result': round(result, 2),
            'input': input_dict,
        }
        return render(request, 'core/risk.html', context)

    return render(request, 'core/risk.html')


def generate_rules():
    # Define membership levels
    levels = ['low', 'medium', 'high']
    antecedents = ['damage_potential', 'exploitability', 'reproducibility', 'affected_users', 'discoverability']

    # Generate all 243 combinations
    combinations = list(itertools.product(levels, repeat=len(antecedents)))

    # Create rules list
    rules = []

    rules_number = 0
    for combo in combinations:
        rules_number = rules_number + 1
        condition = ' & '.join(f"{var}['{level}']" for var, level in zip(antecedents, combo))

        # Fixed fuzzy rule assignment logic
        if combo.count('high') >= 3:
            risk = "risk_score['high']"
        elif combo.count('low') >= 3:
            risk = "risk_score['low']"
        else:
            risk = "risk_score['medium']"

        rules.append(f"ctrl.Rule({condition}, {risk})")

    return [rules, rules_number]


def download_fuzzy_rules(request):
    rules_response = generate_rules()
    all_rules = rules_response[0]
    number_of_rules = rules_response[1]
    
    # Prepare text file content
    filename = f"fuzzy_rules_{slugify(datetime.now().isoformat())}.txt"
    file_content = f"{number_of_rules} Rules\n\n" + "\n".join(all_rules)

    # Create response to download file
    response = HttpResponse(file_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response