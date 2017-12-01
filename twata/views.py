# twata/views.py
from django.views.generic import TemplateView
import sys
sys.path.append("./scripts/")
import getGraphScript
import datetime


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class GraphPageView(TemplateView):
    template_name = 'graph.html'


def get_context_data(self, **kwargs):
    context = super(GraphPageView, self).get_context_data(**kwargs)

    neg_scores, neg_height = getGraphScript.getNegScript()
    pos_scores, pos_height = getGraphScript.getPosScript()
    x_keys = getGraphScript.getXCats()

    current_date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

    context['date'] = current_date
    context['neg_latest_scores_ordered'] = neg_scores
    context['neg_graph_height'] = neg_height
    context['pos_latest_scores_ordered'] = pos_scores
    context['pos_graph_height'] = pos_height
    context['x_cats'] = x_keys
    return context
