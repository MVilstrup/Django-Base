# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from django.contrib.auth.models import User

class TestHomePage(TestCase):
    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        self.client.login(username='temporary', password='temporary')
        activate('en')
        response = self.client.get(reverse("home"), follow=True)
        self.assertTemplateUsed(response, "base/index.html")

    def test_uses_base_template(self):
        self.client.login(username='temporary', password='temporary')
        activate('en')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")

