from django.urls import path

from core.erp.views import myfirstview

app_name = 'erp'
urlpatterns = [
    path('home/', myfirstview, name='vista1')
]
