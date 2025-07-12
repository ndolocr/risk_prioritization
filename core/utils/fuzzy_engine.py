# core/fuzzy_engine.py

import numpy as np
import itertools
from skfuzzy import control as ctrl
import skfuzzy as fuzz

# Generating rules for DREAD
def get_fuzzy_risk_control_system_without_cost():
    levels = ['low', 'medium', 'high']
    antecedents_names = ['damage_potential', 'exploitability', 'reproducibility', 'affected_users', 'discoverability']
    
    # Define Antecedents
    antecedents = {
        name: ctrl.Antecedent(np.arange(0, 11, 1), name)
        for name in antecedents_names
    }

    for a in antecedents.values():
        a['low'] = fuzz.trimf(a.universe, [0, 0, 5])
        a['medium'] = fuzz.trimf(a.universe, [0, 5, 10])
        a['high'] = fuzz.trimf(a.universe, [5, 10, 10])

        risk_score = ctrl.Consequent(np.arange(0, 11, 1), 'risk_score')
        risk_score['low'] = fuzz.trimf(risk_score.universe, [0, 0, 4])
        risk_score['medium'] = fuzz.trimf(risk_score.universe, [3, 5, 7])
        risk_score['high'] = fuzz.trimf(risk_score.universe, [6, 10, 10])

    # Define Consequent
    # risk_score = ctrl.Consequent(np.arange(0, 51, 1), 'risk_score')
    # risk_score['low'] = fuzz.trimf(risk_score.universe, [0, 0, 25])
    # risk_score['medium'] = fuzz.trimf(risk_score.universe, [0, 25, 50])
    # risk_score['high'] = fuzz.trimf(risk_score.universe, [25, 50, 50])

    # Generate rules
    combinations = list(itertools.product(levels, repeat=len(antecedents_names)))
    rules = []
    for combo in combinations:
        condition_str = ' & '.join(f"{name}['{level}']" for name, level in zip(antecedents_names, combo))

        if combo.count('high') >= 3:
            risk_str = "risk_score['high']"
        elif combo.count('low') >= 3:
            risk_str = "risk_score['low']"
        else:
            risk_str = "risk_score['medium']"

        rules.append(ctrl.Rule(eval(condition_str, {**antecedents, 'risk_score': risk_score}), eval(risk_str, {'risk_score': risk_score})))

    # Control System
    #These are the generated rules for DREAM
    control_system = ctrl.ControlSystem(rules)

    return control_system, antecedents, risk_score

#Function to Generting rules for DREAD-C
def get_fuzzy_risk_control_system_with_cost_and_dread():
    levels = ['low', 'medium', 'high']
    antecedents_names = ['cost', 'dread']
    
    # Define Antecedents
    antecedents = {
        name: ctrl.Antecedent(np.arange(0, 11, 1), name)
        for name in antecedents_names
    }
    # antecedents = {
    #     name: ctrl.Antecedent(np.arange(0, 51, 1), name)
    #     for name in antecedents_names
    # }

    #Generating antecedents for Cost and DREAD
    for a in antecedents.values():
        a['low'] = fuzz.trimf(a.universe, [0, 0, 5])
        a['medium'] = fuzz.trimf(a.universe, [0, 5, 10])
        a['high'] = fuzz.trimf(a.universe, [5, 10, 10])
    # for a in antecedents.values():
    #     a['low'] = fuzz.trimf(a.universe, [0, 0, 25])
    #     a['medium'] = fuzz.trimf(a.universe, [0, 25, 50])
    #     a['high'] = fuzz.trimf(a.universe, [25, 50, 50])

    # Define Consequent
    risk_score = ctrl.Consequent(np.arange(0, 11, 1), 'risk_score')
    risk_score['low'] = fuzz.trimf(risk_score.universe, [0, 0, 4])
    risk_score['medium'] = fuzz.trimf(risk_score.universe, [3, 5, 7])
    risk_score['high'] = fuzz.trimf(risk_score.universe, [6, 10, 10])
    # risk_score = ctrl.Consequent(np.arange(0, 101, 1), 'risk_score')
    # risk_score['low'] = fuzz.trimf(risk_score.universe, [0, 0, 50])
    # risk_score['medium'] = fuzz.trimf(risk_score.universe, [25, 50, 75])
    # risk_score['high'] = fuzz.trimf(risk_score.universe, [50, 100, 100])

    # Generate rules
    combinations = list(itertools.product(levels, repeat=len(antecedents_names)))
    rules = []
    for combo in combinations:
        condition_str = ' & '.join(f"{name}['{level}']" for name, level in zip(antecedents_names, combo))

        if combo.count('high') >= 2:
            risk_str = "risk_score['high']"
        elif combo.count('low') >= 2:
            risk_str = "risk_score['low']"
        else:
            risk_str = "risk_score['medium']"

        rules.append(ctrl.Rule(eval(condition_str, {**antecedents, 'risk_score': risk_score}), eval(risk_str, {'risk_score': risk_score})))

    # Control System
    #Rules Generated for DREAD-C
    print(f"RULES -- > {rules}")
    control_system = ctrl.ControlSystem(rules)

    return control_system, antecedents, risk_score














def get_fuzzy_risk_control_system_with_cost():
    levels = ['low', 'medium', 'high']
    antecedents_names = ['cost']
    
    # Define Antecedents
    antecedents = {
        name: ctrl.Antecedent(np.arange(0, 11, 1), name)
        for name in antecedents_names
    }

    for a in antecedents.values():
        a['low'] = fuzz.trimf(a.universe, [0, 0, 5])
        a['medium'] = fuzz.trimf(a.universe, [0, 5, 10])
        a['high'] = fuzz.trimf(a.universe, [5, 10, 10])

    # Define Consequent
    cost_score = ctrl.Consequent(np.arange(0, 11, 1), 'cost_score')
    cost_score['low'] = fuzz.trimf(cost_score.universe, [0, 0, 5])
    cost_score['medium'] = fuzz.trimf(cost_score.universe, [0, 5, 10])
    cost_score['high'] = fuzz.trimf(cost_score.universe, [5, 10, 10])

    # Generate rules
    combinations = list(itertools.product(levels, repeat=len(antecedents_names)))
    rules = []
    for combo in combinations:
        condition_str = ' & '.join(f"{name}['{level}']" for name, level in zip(antecedents_names, combo))

        if combo.count('high') >= 3:
            risk_str = "cost_score['high']"
        elif combo.count('low') >= 3:
            risk_str = "cost_score['low']"
        else:
            risk_str = "cost_score['medium']"

        rules.append(ctrl.Rule(eval(condition_str, {**antecedents, 'cost_score': cost_score}), eval(risk_str, {'cost_score': cost_score})))
    print(f"Rules --> {rules}")
    # Control System
    control_system = ctrl.ControlSystem(rules)

    return control_system, antecedents



def get_fuzzy_risk_control_system_with_cost_old():
    levels = ['low', 'medium', 'high']
    antecedents_names = ['cost', 'damage_potential', 'exploitability', 'reproducibility', 'affected_users', 'discoverability']
    
    # Define Antecedents
    antecedents = {
        name: ctrl.Antecedent(np.arange(0, 11, 1), name)
        for name in antecedents_names
    }

    for a in antecedents.values():
        a['low'] = fuzz.trimf(a.universe, [0, 0, 5])
        a['medium'] = fuzz.trimf(a.universe, [0, 5, 10])
        a['high'] = fuzz.trimf(a.universe, [5, 10, 10])

    # Define Consequent
    risk_score = ctrl.Consequent(np.arange(0, 11, 1), 'risk_score')
    risk_score['low'] = fuzz.trimf(risk_score.universe, [0, 0, 5])
    risk_score['medium'] = fuzz.trimf(risk_score.universe, [0, 5, 10])
    risk_score['high'] = fuzz.trimf(risk_score.universe, [5, 10, 10])

    # Generate rules
    combinations = list(itertools.product(levels, repeat=len(antecedents_names)))
    rules = []
    for combo in combinations:
        condition_str = ' & '.join(f"{name}['{level}']" for name, level in zip(antecedents_names, combo))

        if combo.count('high') >= 3:
            risk_str = "risk_score['high']"
        elif combo.count('low') >= 3:
            risk_str = "risk_score['low']"
        else:
            risk_str = "risk_score['medium']"

        rules.append(ctrl.Rule(eval(condition_str, {**antecedents, 'risk_score': risk_score}), eval(risk_str, {'risk_score': risk_score})))

    # Control System
    control_system = ctrl.ControlSystem(rules)

    return control_system, antecedents
