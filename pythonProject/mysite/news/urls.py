from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import NewsSearchView, ArticleListView

#app_name = 'news'

urlpatterns = [
    path('', ArticleListView.as_view(), name='news'),
    path('create/',views.create, name='create'),
    path('<int:pk>/',views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update',views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete',views.NewsDeleteView.as_view(), name='news_delete'),
    path('<int:pk>/add_comment', views.CommentCreateView.as_view(), name='add_comment'),
    path('search/', NewsSearchView.as_view(), name='search'),
#path('home/',views.index),
#path('contacts/',views.contacts),

]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)