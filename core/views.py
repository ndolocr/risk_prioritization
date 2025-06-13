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

# from core.utils import rules_with_cost
from core.utils import fuzzy_engine

control_system_with_cost, antecedents_with_cost = fuzzy_engine.get_fuzzy_risk_control_system_with_cost()
control_system_without_cost, antecedents_without_cost, risk_score = fuzzy_engine.get_fuzzy_risk_control_system_without_cost()

# Create your views here.
def risk_with_cost_for_windows(request):
    if request.method == 'POST':        

        cost_input = int(request.POST.get('cost'))
        exploitability_input = int(request.POST.get('exploitability'))
        affected_users_input = int(request.POST.get('affected_users'))
        discoverability_input = int(request.POST.get('discoverability'))
        reproducibility_input = int(request.POST.get('reproducibility'))
        damage_potential_input = int(request.POST.get('damage_potential'))

        cost_sim = ctrl.ControlSystemSimulation(control_system_with_cost)
        risk_sim = ctrl.ControlSystemSimulation(control_system_without_cost)

        cost_sim.input['cost'] = cost_input

        risk_sim.input['exploitability'] = exploitability_input
        risk_sim.input['affected_users'] = affected_users_input
        risk_sim.input['discoverability'] = discoverability_input
        risk_sim.input['reproducibility'] = reproducibility_input
        risk_sim.input['damage_potential'] = damage_potential_input

        risk_sim.compute()
        cost_sim.compute()
        
        result_cost_sim =cost_sim.output['cost_score']
        result_risk_sim =risk_sim.output['risk_score']

        result = result_cost_sim + result_risk_sim

        # Plot risk score output
        plt.figure()
        risk_score.view(sim=risk_sim)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graph_1 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        # Plot a simple bar chart showing individual and combined scores
        labels = ['Cost Risk', 'Threat Risk', 'Combined Risk']
        values = [result_cost_sim, result_risk_sim, result]

        plt.figure(figsize=(8, 5))
        bars = plt.bar(labels, values, color=['#ff9999','#66b3ff','#99ff99'])
        plt.ylim(0, 20)  # max score is 10 + 10
        plt.title('Fuzzy Risk Evaluation')
        plt.ylabel('Risk Score')

        # Annotate bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                    f'{height:.2f}', ha='center', va='bottom')

        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graph = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        input_dict = {
            'cost': cost_input,
            'result_cost_sim': round(result_cost_sim, 2),
            'result_risk_sim': round(result_risk_sim, 2),
            'exploitability': exploitability_input, 
            'affected_users': affected_users_input, 
            'discoverability': discoverability_input, 
            'reproducibility': reproducibility_input, 
            'damage_potential': damage_potential_input
            }
        
        context = {
            'graph': graph, 
            'graph_1': graph_1,            
            'input': input_dict,
            'result': round(result, 2),
        }

        return render(request, 'core/risk_with_cost_windows.html', context)
    
    return render(request, 'core/risk_with_cost_windows.html')

def risk_without_cost_for_windows(request):
    if request.method == 'POST':        
        exploitability_input = int(request.POST.get('exploitability'))
        affected_users_input = int(request.POST.get('affected_users'))
        discoverability_input = int(request.POST.get('discoverability'))
        reproducibility_input = int(request.POST.get('reproducibility'))
        damage_potential_input = int(request.POST.get('damage_potential'))

        cost_sim = ctrl.ControlSystemSimulation(control_system_with_cost)
        risk_sim = ctrl.ControlSystemSimulation(control_system_without_cost)

        risk_sim.input['exploitability'] = exploitability_input
        risk_sim.input['affected_users'] = affected_users_input
        risk_sim.input['discoverability'] = discoverability_input
        risk_sim.input['reproducibility'] = reproducibility_input
        risk_sim.input['damage_potential'] = damage_potential_input

        risk_sim.compute()
        
        result_risk_sim =risk_sim.output['risk_score']

        result = result_risk_sim

        # Plot risk score output
        plt.figure()
        risk_score.view(sim=risk_sim)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graph_1 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        # Plot a simple bar chart showing individual and combined scores
        labels = ['Threat Risk']
        values = [result]

        plt.figure(figsize=(8, 5))
        bars = plt.bar(labels, values, color=['#ff9999','#66b3ff','#99ff99'])
        plt.ylim(0, 20)  # max score is 10 + 10
        plt.title('Fuzzy Risk Evaluation')
        plt.ylabel('Risk Score')

        # Annotate bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                    f'{height:.2f}', ha='center', va='bottom')

        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png')
        buf.seek(0)
        graph = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        input_dict = {
            'result_risk_sim': round(result_risk_sim, 2),
            'exploitability': exploitability_input, 
            'affected_users': affected_users_input, 
            'discoverability': discoverability_input, 
            'reproducibility': reproducibility_input, 
            'damage_potential': damage_potential_input
            }
        
        context = {
            'graph': graph, 
            'graph_1': graph_1,            
            'input': input_dict,
            'result': round(result, 2),
        }

        return render(request, 'core/risk_without_cost_windows.html', context)
    
    return render(request, 'core/risk_without_cost_windows.html')

def risk_with_cost_for_macbook(request):
    if request.method == 'POST':

        cost_input = int(request.POST.get('cost'))
        exploitability_input = int(request.POST.get('exploitability'))
        affected_users_input = int(request.POST.get('affected_users'))
        discoverability_input = int(request.POST.get('discoverability'))
        reproducibility_input = int(request.POST.get('reproducibility'))
        damage_potential_input = int(request.POST.get('damage_potential'))

        cost_sim = ctrl.ControlSystemSimulation(control_system_with_cost)
        risk_sim = ctrl.ControlSystemSimulation(control_system_without_cost)
        
        cost_sim.input['cost'] = cost_input

        risk_sim.input['exploitability'] = exploitability_input
        risk_sim.input['affected_users'] = affected_users_input
        risk_sim.input['discoverability'] = discoverability_input
        risk_sim.input['reproducibility'] = reproducibility_input
        risk_sim.input['damage_potential'] = damage_potential_input

        risk_sim.compute()
        cost_sim.compute()
        
        result_cost_sim =cost_sim.output['cost_score']
        result_risk_sim =risk_sim.output['risk_score']

        print(f"Cost Score --> {result_cost_sim}")
        print(f"Risk Score --> {result_risk_sim}")

        # result = risk_sim.output['risk_score']
        result = result_cost_sim + result_risk_sim

        print(f"Total Risk Score --> {result}")

        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Bar chart for risk score
        ax.bar(['Risk Score'], [result], color='orange', width=0.4, label='Fuzzy Risk Score')

        # Overlay line chart for inputs
        input_labels = ['cost', 'Exploitability', 'Affected Users', 'Discoverability', 'Reproducibility', 'Damage Potential']

        input_values = [
            cost_input,
            exploitability_input, 
            affected_users_input, 
            discoverability_input, 
            reproducibility_input, 
            damage_potential_input
        ]

        ax.plot(input_labels, input_values, color='blue', marker='o', linestyle='-', label='Input Factors')

        ax.set_ylim(0, 15)
        ax.set_ylabel('Score (0-15)')
        ax.set_title('Fuzzy Risk Score with Input Factors')
        ax.legend()

        # Save and encode image
        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graph = base64.b64encode(image_png).decode('utf-8')

        input_dict = {
            'cost': cost_input,
            'result_cost_sim': round(result_cost_sim, 2),
            'result_risk_sim': round(result_risk_sim, 2),
            'exploitability': exploitability_input,
            'affected_users': affected_users_input,
            'discoverability': discoverability_input,
            'reproducibility': reproducibility_input,
            'damage_potential': damage_potential_input
        }

        print(input_dict)
        
        # Pass risk score and graph to template
        context = {
            'graph': graph,
            'result': round(result, 2),
            'input': input_dict,
        }
        return render(request, 'core/risk_with_cost_for_macbook.html', context)
    return render(request, 'core/risk_with_cost_for_macbook.html')

def risk_without_cost_for_macbook(request):
    if request.method == 'POST':

        exploitability_input = int(request.POST.get('exploitability'))
        affected_users_input = int(request.POST.get('affected_users'))
        discoverability_input = int(request.POST.get('discoverability'))
        reproducibility_input = int(request.POST.get('reproducibility'))
        damage_potential_input = int(request.POST.get('damage_potential'))

        risk_sim = ctrl.ControlSystemSimulation(control_system_without_cost)

        risk_sim.input['exploitability'] = exploitability_input
        risk_sim.input['affected_users'] = affected_users_input
        risk_sim.input['discoverability'] = discoverability_input
        risk_sim.input['reproducibility'] = reproducibility_input
        risk_sim.input['damage_potential'] = damage_potential_input

        risk_sim.compute()
        result = risk_sim.output['risk_score']


        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Bar chart for risk score
        ax.bar(['Risk Score'], [result], color='orange', width=0.4, label='Fuzzy Risk Score')

        # Overlay line chart for inputs
        input_labels = ['Exploitability', 'Affected Users', 'Discoverability', 'Reproducibility', 'Damage Potential']

        input_values = [
            exploitability_input, 
            affected_users_input, 
            discoverability_input, 
            reproducibility_input, 
            damage_potential_input
        ]

        ax.plot(input_labels, input_values, color='blue', marker='o', linestyle='-', label='Input Factors')

        ax.set_ylim(0, 15)
        ax.set_ylabel('Score (0-15)')
        ax.set_title('Fuzzy Risk Score with Input Factors')
        ax.legend()

        # Save and encode image
        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        graph = base64.b64encode(image_png).decode('utf-8')

        input_dict = {
            'exploitability': exploitability_input,
            'affected_users': affected_users_input,
            'discoverability': discoverability_input,
            'reproducibility': reproducibility_input,
            'damage_potential': damage_potential_input
        }

        print(input_dict)
        
        # Pass risk score and graph to template
        context = {
            'graph': graph,
            'result': round(result, 2),
            'input': input_dict,
        }
        return render(request, 'core/risk_without_cost_for_macbook.html', context)

    return render(request, 'core/risk_without_cost_for_macbook.html')

def generate_rules_with_cost():
    # Define membership levels
    levels = ['low', 'medium', 'high']
    antecedents = ['cost', 'damage_potential', 'exploitability', 'reproducibility', 'affected_users', 'discoverability']

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

def generate_rules_for_cost_only():
    # Define membership levels
    levels = ['low', 'medium', 'high']
    antecedents = ['cost']

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

def generate_rules_without_cost():
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

def download_fuzzy_rules_with_cost(request):
    rules_response = generate_rules_with_cost()
    all_rules = rules_response[0]
    number_of_rules = rules_response[1]
    
    # Prepare text file content
    filename = f"fuzzy_rules_with_cost_{slugify(datetime.now().isoformat())}.txt"
    file_content = f"{number_of_rules} Rules\n\n" + "\n".join(all_rules)

    # Create response to download file
    response = HttpResponse(file_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

def download_fuzzy_rules_for_cost_only(request):
    rules_response = generate_rules_for_cost_only()
    all_rules = rules_response[0]
    number_of_rules = rules_response[1]
    
    # Prepare text file content
    filename = f"fuzzy_rules_cost_only_{slugify(datetime.now().isoformat())}.txt"
    file_content = f"{number_of_rules} Rules\n\n" + "\n".join(all_rules)

    # Create response to download file
    response = HttpResponse(file_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

def download_fuzzy_rules_without_cost(request):
    rules_response = generate_rules_without_cost()
    all_rules = rules_response[0]
    number_of_rules = rules_response[1]
    
    # Prepare text file content
    filename = f"fuzzy_rules_without_cost_{slugify(datetime.now().isoformat())}.txt"
    file_content = f"{number_of_rules} Rules\n\n" + "\n".join(all_rules)

    # Create response to download file
    response = HttpResponse(file_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response

def view_fuzzy_rules_with_cost(request):
    rules_response = generate_rules_with_cost()
    all_rules = rules_response[0]
    number_of_rules = rules_response[1]
    print(f"{type(all_rules)}")
    # for rule in all_rules:
    #     print(f"{type(rule)}")
    context = {
        "all_rules": all_rules,
        "number_of_rules": number_of_rules,
    }

    return render(request, 'core/rules_with_cost.html', context)

def view_fuzzy_rules_without_cost(request):
    rules_response = generate_rules_without_cost()
    all_rules = rules_response[0]
    number_of_rules = rules_response[1]
    print(f"{type(all_rules)}")
    # for rule in all_rules:
    #     print(f"{type(rule)}")
    context = {
        "all_rules": all_rules,
        "number_of_rules": number_of_rules,
    }

    return render(request, 'core/rules_without_cost.html', context)

def view_fuzzy_rules_for_cost_only(request):
    rules_response = generate_rules_for_cost_only()
    all_rules = rules_response[0]
    number_of_rules = rules_response[1]
    print(f"{type(all_rules)}")
    # for rule in all_rules:
    #     print(f"{type(rule)}")
    context = {
        "all_rules": all_rules,
        "number_of_rules": number_of_rules,
    }

    return render(request, 'core/cost_rules_only.html', context)