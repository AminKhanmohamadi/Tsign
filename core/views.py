from django.shortcuts import render
from django.views.generic import ListView

from core.models import Folder


# Create your views here.
class FolderListView(ListView):
    model = Folder
    template_name = 'core/folder_list.html'
    context_object_name = 'folders'