from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('news/',views.news, name='news'),
    path('news/<str:pk>/', views.newsdetail, name='newsdetail'),
    path('addnews/',views.addnews, name='addnews'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('causes/',views.causes, name='causes'),
    path('environ/', views.environ, name='environ'),
    path('health/', views.health, name='health'),
    path('leadership/', views.leader, name='leader'),
    path('peace/', views.peace, name='peace'),
    path('smart/', views.smart, name='smart'),
    path('other_activities/', views.others, name='others'),
    path('membercsv/', views.member_csv, name='membercsv' ),
    path('search/', views.search, name='search'),
    path('search_result/<search_result>/', views.search_result, name='result'),
    path('register/',views.register, name='register'),
    path('login/',views.signin, name='login'),
    path('logout/', views.signout, name='signout'),
    path('subscribe', views.subscribe, name='subscribe'),
    path("newsletter", views.newsletter, name="newsletter"),
    path('contactcsv/', views.contact_csv, name='contactcsv' ),

    
]


