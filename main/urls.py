from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name=''),
    path('products', views.product, name='products'),
    path('category', views.categories, name='category'),
    path('news', views.news, name='news'),
    path('addnews', views.Adnewz.as_view(), name='addnews'),
    path('upnews/<int:pk>', views.Upnews.as_view(), name='upnews'),
    path('dltnwz/<int:pk>', views.Dltnews.as_view(), name='dltnwz'),


    path('fruits', views.fruits, name='fruits'),
    path('veggies', views.veggies, name='veggies'),
    path('pdetails/<int:id>', views.details, name='pdetails'),

    path('login', views.loginpage, name='login'),

    path('logout', views.logoutpage, name='logout'),
    path('profile', views.Profilepage, name='profile'),
    path('uprofile/<int:pk>', views.Proupdate.as_view(), name='uprofile'),
    path('register', views.registerpage, name='register'),
    path('addp', views.Adpro.as_view(), name='addp'),
    path('update/<int:pk>', views.ModifyV.as_view(), name='update'),
    path('delete/<int:pk>', views.Pdelete.as_view(), name='delete'),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
