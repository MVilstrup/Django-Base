# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, "base/index.html", {})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

