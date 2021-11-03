from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('location/', views.location, name = 'location'),
    path('add_biz/', views.add_biz, name = 'add_biz'),
    path('Post/<int:id>/create-post/',views.Post, name='post'),

    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('EditProfile/<username>/',views.EditProfile,name = 'EditProfile'),
    path('estate/<int:id>/', views.estate, name = 'each-hood'),
    path('search/', views.search, name = 'search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)