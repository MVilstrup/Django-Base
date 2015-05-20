# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate 

class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        activate('en')
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)
    
    def test_h1_css(self):
        activate('en')
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), 
                         "rgba(200, 50, 255, 1)")
    
    def test_home_files(self):
        activate('en')
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)

    def test_internationalization(self):
        for lang, h1_text in [('en', 'Welcome to 23Video!'), 
                              ('da', 'Velkommen til 23Video!')]:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h1 = self.browser.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, h1_text)
