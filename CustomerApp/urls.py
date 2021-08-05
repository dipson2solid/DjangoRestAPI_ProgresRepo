from django.conf.urls import url
from CustomerApp import views


from django.conf import settings

urlpatterns=[
    url(r'^customer$',views.customerApi),
    url(r'^customer/([0-9]+)$',views.customerApi)

   
]