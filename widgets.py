from dashing.widgets import NumberWidget
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class UserCards(NumberWidget):
    title = 'New users'

    def get_more_info(self):
        return '500 open'

    def get_updated_at(self):
        return 'updated at ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_value(self):
        return '%d' % User.objects.exclude(date_joined__gt=datetime.today()-timedelta(days=7)).count()

    def get_detail(self):
        return '%d total users' % User.objects.count()
