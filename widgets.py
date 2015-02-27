from dashing.widgets import NumberWidget
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from core.models import Campaign, AdGroup
from accounts.models import GoogleAccount


class UserCards(NumberWidget):
    title = 'New users'

    def get_more_info(self):
        today = datetime.today()
        first_day_of_month = datetime(today.year, today.month, 1)
        return '%d users this month' % User.objects.exclude(date_joined__lt=first_day_of_month).count()

    def get_updated_at(self):
        return 'updated at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_value(self):
        return '%d' % User.objects.exclude(date_joined__lt=datetime.today()-timedelta(days=7)).count()

    def get_detail(self):
        return '%d total users' % User.objects.count()


class CampaignCards(NumberWidget):
    title = 'Campaigns Created'

    def get_more_info(self):
        return '%d campaigns' % Campaign.objects.count()

    def get_updated_at(self):
        return 'updated at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_value(self):
        return '%d' % Campaign.objects.count()

    def get_detail(self):
        return '%d total campaigns' % Campaign.objects.count()


class AdGroupCards(NumberWidget):
    title = 'AdGroups Created'

    def get_more_info(self):
        return '%d ad groups' % AdGroup.objects.count()

    def get_updated_at(self):
        return 'updated at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_value(self):
        return '%d' % AdGroup.objects.count()

    def get_detail(self):
        return '%d total ad groups' % AdGroup.objects.count()


class GoogleAccountCards(NumberWidget):
    title = 'Google Accounts Managed'

    def get_more_info(self):
        return '%d google accounts' % GoogleAccount.objects.count()

    def get_updated_at(self):
        return 'updated at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_value(self):
        return '%d' % GoogleAccount.objects.count()

    def get_detail(self):
        return '%d total google accounts' % GoogleAccount.objects.count()
