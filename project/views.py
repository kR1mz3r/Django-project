from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Task


class ProjectTaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Задачи'
        return context
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assigned_to=user)


def update_files(request, pk):
    if request.method == 'POST' and request.FILES.get('file'):
        task = Task.objects.get(id=pk)
        task.updated_files = request.FILES['file']
        task.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


class ViewProject(DetailView):
    model = Task
    context_object_name = 'project_item'



