from django.urls import path

from core.views import FolderListView

urlpatterns = [
    path('' , FolderListView.as_view(), name='folder-list'),
]