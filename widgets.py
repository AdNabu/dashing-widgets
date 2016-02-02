from dashing.widgets import NumberWidget
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from core.models import Campaign, AdGroup
from accounts.models import AdwordsAccount


class NumberWidgetMonth(NumberWidget):
    today = datetime.today()
    first_day_of_month = datetime(today.year, today.month, 1)

    def get_updated_at(self):
        return 'updated at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class UserCards(NumberWidgetMonth):
    title = 'New users'

    def get_more_info(self):
        return '%d users this month' % User.objects.exclude(date_joined__lt=self.first_day_of_month).count()

    def get_value(self):
        return '%d' % User.objects.exclude(date_joined__lt=datetime.today()-timedelta(days=7)).count()

    def get_detail(self):
        return '%d total users' % User.objects.count()


class CampaignCards(NumberWidgetMonth):
    title = 'Campaigns Created'

    def get_more_info(self):
        return '%d campaigns this month' % Campaign.objects.filter(is_external=False).exclude(
            created_on__lt=self.first_day_of_month).count()

    def get_value(self):
        return '%d' % Campaign.objects.filter(is_external=False).exclude(
            created_on__lt=datetime.today() - timedelta(days=7)).count()

    def get_detail(self):
        return '%d total campaigns' % Campaign.objects.filter(is_external=False).count()


class AdGroupCards(NumberWidgetMonth):
    title = 'AdGroups Created'

    def get_more_info(self):
        return '%d ad groups this month' % AdGroup.objects.exclude(created_on__lt=self.first_day_of_month).count()

    def get_value(self):
        return '%d' % AdGroup.objects.exclude(created_on__lt=datetime.today() - timedelta(days=7)).count()

    def get_detail(self):
        return '%d total ad groups' % AdGroup.objects.count()


class AdwordsAccountCards(NumberWidgetMonth):
    title = 'New Adwords Accounts'

    def get_more_info(self):
        return '%d adwords accounts this month' % AdwordsAccount.objects.exclude(
            created_on__lt=self.first_day_of_month).count()

    def get_value(self):
        return '%d' % AdwordsAccount.objects.exclude(created_on__lt=datetime.today() - timedelta(days=7)).count()

    def get_detail(self):
        return '%d total adwords accounts' % AdwordsAccount.objects.count()
