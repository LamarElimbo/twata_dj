# twata/views.py
from django.shortcuts import render
from twata import getGraphScript
import datetime
import os


def home(request):
    return render(request, 'twata/home.html', {'css_source': '../static/home2_static/app.css', 'activeTab': 'home'})


def graph(request):
    print('current dir: ', os.getcwd())

    neg_scores, neg_height = getGraphScript.getNegScript()
    pos_scores, pos_height = getGraphScript.getPosScript()
    x_keys = getGraphScript.getXCats()

    return render(request, 'twata/graph.html', {'css_source': 'static/twata_static/app.css', 'date': 'Tuesday, November 3, 2017', 'neg_latest_scores_ordered': neg_scores, 'neg_graph_height': neg_height, 'pos_latest_scores_ordered': pos_scores, 'pos_graph_height': pos_height, 'x_cats': x_keys})
