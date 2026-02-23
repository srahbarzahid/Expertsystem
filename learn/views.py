import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

TEMPLATES = {
    'introduction': 'learn/introduction.html',
    'steps': 'learn/steps.html',
    'preprocessing': 'learn/preprocessing.html',
    'numpy': 'learn/numpy.html',
    'pandas': 'learn/pandas.html',
    'visualization': 'learn/matplotlib.html',
    'knn': 'learn/knn.html',
    'classification_metrics': 'learn/classification_metrics.html',
    'decision_tree': 'learn/decision_tree.html',
    'naive_bayes': 'learn/naive_bayes.html',
    'linear_regression': 'learn/linear_regression.html',
    'regression_metrics': 'learn/regression_metrics.html',
    'kmeans': 'learn/kmeans.html',
    'svm': 'learn/svm.html',
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
