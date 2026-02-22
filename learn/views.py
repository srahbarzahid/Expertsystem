import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

TEMPLATES = {
    'introduction': 'learn/introduction.html',
    'pandas': 'learn/pandas.html',
    'numpy': 'learn/numpy.html',
    'matplotlib': 'learn/matplotlib.html',
    'classification': 'learn/classification.html',
    'encoding': 'learn/encoding.html',
    'svm': 'learn/svm.html',
    'regression': 'learn/regression.html',
    'missing-values': 'learn/missing_values.html',
    'decision-tree': 'learn/decision_tree.html',
    'clustering': 'learn/clustering.html',
    'scaling': 'learn/scaling.html',
    'random-forest': 'learn/random_forest.html',
}


@login_required
def index(request):
    return redirect('chapter', chapter='introduction')


@login_required
def chapter_view(request, chapter):
    template = TEMPLATES.get(chapter)
    if template:
        return render(request, template, {'chapters': TEMPLATES})
    return redirect('chapter', 'introduction')
