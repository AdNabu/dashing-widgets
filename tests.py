from django.core.urlresolvers import reverse
from django.test import TestCase


class DashingWidgetsViewsTestCase(TestCase):
    def test_users(self):
        resp = self.client.get(reverse('dashing_widgets:users_widget'))
        self.assertEqual(resp.status_code, 200)

    def test_campaigns(self):
        resp = self.client.get(reverse('dashing_widgets:campaigns_widget'))
        self.assertEqual(resp.status_code, 200)

    def test_google_accounts(self):
        resp = self.client.get(reverse('dashing_widgets:google_accounts_widget'))
        self.assertEqual(resp.status_code, 200)

    def test_ad_groups(self):
        resp = self.client.get(reverse('dashing_widgets:ad_groups_widget'))
        self.assertEqual(resp.status_code, 200)