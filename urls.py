from django.conf.urls import url
from widgets import UserCards, CampaignCards, GoogleAccountCards, AdGroupCards

urlpatterns = [
    url(r'^users', UserCards.as_view(), name='users_widget'),
    url(r'^campaigns', CampaignCards.as_view(), name='campaigns_widget'),
    url(r'^ad/groups', AdGroupCards.as_view(), name='ad_groups_widget'),
    url(r'^google/accounts', GoogleAccountCards.as_view(), name='google_accounts_widget'),
]