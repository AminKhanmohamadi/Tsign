import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic import View

from .forms import FileUploadForm
from .models import File, Folder


class FolderListView(LoginRequiredMixin, ListView):
    model = Folder
    template_name = 'core/folder_list.html'
    context_object_name = 'folders'

    def get_queryset(self):
        parent_id = self.request.GET.get('folder')
        return Folder.objects.filter(

            parent_id=parent_id
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_id = self.request.GET.get('folder')
        context['files'] = File.objects.filter(
            folder_id=parent_id
        )
        if parent_id:
            folder = get_object_or_404(Folder, id=parent_id)
            context['breadcrumbs'] = folder.get_path()
        return context


class FileUploadView(LoginRequiredMixin, CreateView):
    model = File
    form_class = FileUploadForm
    template_name = 'core/partial/file_upload.html'
    success_url = reverse_lazy('folder_list')

    def form_valid(self, form):
        folder_id = self.request.POST.get('folder')
        if folder_id:
            folder = get_object_or_404(Folder, id=folder_id)
            form.instance.folder = folder
        return super().form_valid(form)


class FolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder
    fields = ['name']
    template_name = 'core/partial/folder_create.html'
    success_url = reverse_lazy('folder_list')


class FolderDeleteView(LoginRequiredMixin, DeleteView):
    model = Folder
    success_url = reverse_lazy('folder_list')

    def delete(self, request, *args, **kwargs):
        folder = self.get_object()
        folder.delete()
        return JsonResponse({'success': True})


class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = File
    success_url = reverse_lazy('folder_list')

    def delete(self, request, *args, **kwargs):
        file = self.get_object()
        file.delete()
        return JsonResponse({'success': True})


class FolderUpdateView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            folder_id = data.get('folder_id')
            new_name = data.get('name')

            folder = Folder.objects.get(id=folder_id)
            folder.name = new_name
            folder.save()

            return JsonResponse({'success': True, 'new_name': folder.name})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


class FileUpdateView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            file_id = data.get('file_id')
            new_name = data.get('name')
            print(file_id, new_name)

            file = File.objects.get(id=file_id)
            file.name = new_name
            print(file.name)
            file.save()
            return JsonResponse({'success': True, 'new_name': file.name})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


class FileSearchView(LoginRequiredMixin, ListView):
    model = File
    template_name = 'core/partial/search_results.html'
    context_object_name = 'files'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('search', '').strip()
        folder_id = self.request.GET.get('folder')

        if not query:
            return File.objects.none()
        lookups = Q(name__icontains=query)
        if folder_id:
            lookups &= Q(folder_id=folder_id)
        return File.objects.filter(lookups).order_by('-datetime_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('search', '')
        context['current_folder'] = self.request.GET.get('folder')
        return context

        results = []
        for file in files:
            results.append({
                'id': file.id,
                'name': file.name,
                'type': file.file_type,
                'size': file.size,
                'created': file.datetime_created.strftime('%Y/%m/%d')
            })

        return JsonResponse({'files': results})
