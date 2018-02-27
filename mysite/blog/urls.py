from django.conf.urls import url
from . import views  # импорт файлов представлений из текущей папки

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]