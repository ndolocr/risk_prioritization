import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from django.shortcuts import render


# Create your views here.

# Antecedent
def createCostAntecedent():
    cost = ctrl.Antecedent(np.arange(0, 11, 1), 'cost')
    return cost

def createExploitabilityAntecedent():
    exploitability = ctrl.Antecedent(np.arange(0, 11, 1), 'exploitability')
    return exploitability

def createAffectedUsersAntecedent():
    affected_users = ctrl.Antecedent(np.arange(0, 11, 1), 'affected_users')
    return affected_users

def createDiscoverabilityAntecedent():
    discoverability = ctrl.Antecedent(np.arange(0, 11, 1), 'discoverability')
    return discoverability

def createReproducibilityAntecedent():
    reproducibility = ctrl.Antecedent(np.arange(0, 11, 1), 'reproducibility')
    return reproducibility
    
def createDamagePotentialAntecedent():
    damage_potential = ctrl.Antecedent(np.arange(0, 11, 1), 'damage_potential')
    return damage_potential

# Consequent
def riskRankingValueConsequent():
    risk_ranking = ctrl.Consequent(np.arange(0, 11, 1), 'risk_ranking_value')
    return risk_ranking

def riskQuantificationValueConsequent():
    risk_quantification = ctrl.Consequent(np.arange(0, 11, 1), 'risk_quantification_value')
    return risk_quantification
