from __future__ import absolute_import

from celery import task

@task
def add(a, b):
    return a + b
