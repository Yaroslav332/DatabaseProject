from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:news_item_id>/', views.detail, name='detail'),
    path('<int:news_item_id>/comments', views.comments, name='comments'),
    path('<int:news_item_id>/leave_comment', views.leave_comment, name='leave-comment')
]