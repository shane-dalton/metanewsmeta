from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BaseTestView(TemplateView):
    template_name = 'sentiment_analysis/test_template.html'
