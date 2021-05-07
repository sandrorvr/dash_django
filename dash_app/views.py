from django.shortcuts import render
from .models import Dados

import pandas as pd
import random

data = pd.read_csv('./scriptAux/db.csv')

context = {}

def generateColor(n):
    color = []
    for i in range(n):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color.append(f'rgba({r}, {g}, {b}, 1)')
    return color

def fKPI3():
    dic = {}
    kpi2 = pd.crosstab(data.did_id, data.kpi2)

    for col in kpi2.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi2.loc[:,col].values)
    
    dic['did'] = list(kpi2.index)
    dic['color'] = generateColor(len(kpi2.columns))
    
    return dic

def fKPI4_did():
    dic = {}
    kpi4 = pd.crosstab(data.did_id, data.kpi4)

    for col in kpi4.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi4.loc[:,col].values)
    
    dic['did'] = list(kpi4.index)
    dic['color'] = generateColor(len(kpi4.columns))
    
    return dic



def fKPI7_did():
    dic = {}
    kpi7 = pd.crosstab(data.did_id, data.kpi7)

    for col in kpi7.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi7.loc[:,col].values)
    
    dic['did'] = list(kpi7.index)
    dic['color'] = generateColor(len(kpi7.columns))
    
    return dic

def index(request):

    context['kpi3'] = fKPI3()
    context['kpi4_did'] = fKPI4_did()
    context['kpi7_did'] = fKPI7_did()
    
    return render(request, 'index.html', context)
