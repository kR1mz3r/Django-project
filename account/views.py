from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.shortcuts import redirect
from account.models import CustomUser
from django.http import JsonResponse


class UserView(TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = CustomUser.objects.get(user=self.request.user)
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        context['middle_name'] = custom_user.middle_name
        context['photo'] = custom_user.photo
        context['department'] = custom_user.department
        context['role'] = custom_user.role
        context['title'] = 'Личный кабинет'
        return context


def upload_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        user = request.user
        custom_user, created = CustomUser.objects.get_or_create(user=user)
        custom_user.photo = request.FILES['avatar']
        custom_user.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def user_logout(request):
    logout(request)
    return redirect('login')


