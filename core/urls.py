from django.urls import path

from core.views import *

urlpatterns = [
    path('' , FolderListView.as_view(), name='folder_list'),
    path('folder_create/' , FolderCreateView.as_view(), name='folder_create'),
    path('upload_file/', FileUploadView.as_view(), name='upload_file'),
    path('delete-folder/<int:pk>/', FolderDeleteView.as_view(), name='delete_folder'),
    path('delete-file/<int:pk>/', FileDeleteView.as_view(), name='delete_file'),
    path('folder/update_name/', FolderUpdateView.as_view(), name='folder_update_name'),
    path('file/update/', FileUpdateView.as_view(), name='file_update'),
]

