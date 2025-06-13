# core/fuzzy_engine.py

import numpy as np
import itertools
from skfuzzy import control as ctrl
import skfuzzy as fuzz

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