from django.conf.urls import url
from . import views

urlpatterns = [
   # url(r'^$', views.signup_list, name='signup_list'),
    url(r'^mainpage/$', views.main_view, name='main_view_list'),
    url(r'^make_account/$',  views.make_account_list, name="make_account_list"),
    url(r'^create_account_success/$',  views.create_account_success_list, name="create_account_success_list"),
    # url(r'^login_bank/(?P<account_no>[0-9]+)/(?P<price>[0-9]+)/$',  views.login_bank_list, name="login_bank_list"),
    url(r'^login_bank/$',  views.login_bank_list, name="login_bank_list"),
    url(r'^transaction/$',  views.transaction_list, name="transaction_list"),
    url(r'^transaction_fail/$',  views.transaction_list, name="transaction_fail_list"),
    url(r'^corrupt/$',  views.corrupt_list, name="corrupt_list"),
]
