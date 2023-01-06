from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('depart',views.department,name='depart'),
    path('doctors',views.doctors,name='doctors'),
    path('booking',views.booking,name='booking'),

]