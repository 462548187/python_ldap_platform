import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

logger = logging.getLogger('sso')


@login_required
def index(request):
    return render(request, 'index.html')
