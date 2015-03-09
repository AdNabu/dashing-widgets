from django.conf.urls import url
from widgets import UserCards, CampaignCards, AdwordsAccountCards, AdGroupCards

urlpatterns = [
    url(r'^users', UserCards.as_view(), name='users_widget'),
    url(r'^campaigns', CampaignCards.as_view(), name='campaigns_widget'),
    url(r'^ad/groups', AdGroupCards.as_view(), name='ad_groups_widget'),
    url(r'^google/accounts', AdwordsAccountCards.as_view(), name='adwords_accounts_widget'),
]