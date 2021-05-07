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


def fKPI1():
    dic = {}
    dic['values'] = list(data['kpi1'].value_counts().values)
    dic['label'] = list(data['kpi1'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi1'].unique()))
    return dic


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


def fKPI5():
    dic = {}
    kpi5 = pd.crosstab(data.did_id, data.kpi5)

    for col in kpi5.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi5.loc[:,col].values)
    
    dic['did'] = list(kpi5.index)
    dic['color'] = generateColor(len(kpi5.columns))
    
    return dic


def fKPI4():
    dic = {}
    dic['values'] = list(data['kpi4'].value_counts().values)
    dic['label'] = list(data['kpi4'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi4'].unique()))
    return dic



def fKPI6():
    dic = {}
    dic['values'] = list(data['kpi6'].value_counts().values)
    dic['label'] = list(data['kpi6'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi6'].unique()))
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

def fKPI7():
    dic = {}
    dic['values'] = list(data['kpi7'].value_counts().values)
    dic['label'] = list(data['kpi7'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi7'].unique()))
    return dic

def index(request):

    context['kpi1'] = fKPI1()
    context['kpi3'] = fKPI3()
    context['kpi4_did'] = fKPI4_did()
    context['kpi4'] = fKPI4()
    context['kpi5'] = fKPI5()
    context['kpi6'] = fKPI6()
    context['kpi7_did'] = fKPI7_did()
    context['kpi7'] = fKPI7()
    
    return render(request, 'index.html', context)
