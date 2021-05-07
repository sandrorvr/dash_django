from django.shortcuts import render
from .models import Dados

import pandas as pd
import random

data = pd.read_csv('./scriptAux/db.csv')


def generateColor(n):
    color = []
    for i in range(n):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color.append(f'rgba({r}, {g}, {b}, 1)')
    return color

def fKPI2():
    dic = {}
    kpi2 = pd.crosstab(data.did_id, data.kpi2)

    for col in kpi2.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi2.loc[:,col].values)
    
    dic['did'] = list(kpi2.index)
    dic['color'] = generateColor(len(kpi2.columns))
    
    return dic


def index(request):

    context = fKPI2()
    print(context)
    
    return render(request, 'index.html', context)
