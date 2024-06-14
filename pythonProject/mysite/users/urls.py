from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import profile_view

app_name = 'users'

urlpatterns = [
    path('login',views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),
    path('register', views.register_view, name="register"),
    path('profile/', views.profile_view, name='profile'),
    path('profile/change_password/', views.change_password_view, name='change_password'),

#path('home/',views.index),
#path('contacts/',views.contacts),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)