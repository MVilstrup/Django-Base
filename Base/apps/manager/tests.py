# -*- coding: utf-8 -*-
from django.test import TestCase
 
from django.contrib.auth import get_user_model
from . import models, tasks
 
 
class TestProfileModel(TestCase):
 
    def test_profile_creation(self):
        User = get_user_model()
        # New user created
        user = User.objects.create(
            username="test_base", password="base_password")
        # Check that a Profile instance has been crated
        self.assertIsInstance(user.profile, models.Profile)
        # Call the save method of the user to activate the signal
        # again, and check that it doesn't try to create another
        # profile instace
        user.save()
        self.assertIsInstance(user.profile, models.Profile)

    def test_celery_add(self):
        """Test that the ``add`` task runs with no errors,
           and returns the correct result.
        """
        result = tasks.add.delay(8, 8)

        self.assertEquals(result.get(), 16)
        self.assertTrue(result.successful())
