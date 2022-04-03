from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('add_news', add_news, name='add_news')
]
