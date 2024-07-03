from base.models import BaseProjectTask
from django.views.generic import ListView, DetailView
from project.models import Project, Task


class BaseList(ListView):
    model = BaseProjectTask
    context_object_name = 'project'
    paginate_by = 3
    template_name = 'base/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'База знаний>'
        return context


class BaseProjectView(DetailView):
    model = BaseProjectTask
    context_object_name = 'base_task'
