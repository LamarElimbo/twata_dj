# twata/views.py
from django.shortcuts import render
#import getGraphScript
import datetime

def graph(request):

    #neg_scores, neg_height = getGraphScript.getNegScript()
    #pos_scores, pos_height = getGraphScript.getPosScript()
    #x_keys = getGraphScript.getXCats()

    neg_scores = [1, 3, 5]
    neg_height = 10
    pos_scores = [2, 4, 6]
    pos_height = 10
    x_keys = ['Miami', 'Montreal', 'Toronto']

    return render(request, 'twata/graph.html', {'css_source': 'static/app.css', 'date': 'Tuesday, November 3, 2017', 'neg_latest_scores_ordered': neg_scores, 'neg_graph_height': neg_height, 'pos_latest_scores_ordered': pos_scores, 'pos_graph_height': pos_height, 'x_cats': x_keys})
