import hashlib
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from account.models import CustomUser
from messenger.models import Message
from django.views.generic import ListView


class MessengerView(ListView):
    context_object_name = 'messenger'
    template_name = 'messenger/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        custom_user = CustomUser.objects.get(user=self.request.user)
        users = CustomUser.objects.exclude(user=self.request.user)
        chat = Message.objects.filter(
            Q(sender=self.request.user) | Q(recipient=self.request.user)
        )
        context['chat'] = chat
        context['users'] = users
        context['username'] = self.request.user.username
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        context['middle_name'] = custom_user.middle_name
        context['photo'] = custom_user.photo
        context['department'] = custom_user.department
        context['role'] = custom_user.role
        context['title'] = 'Мессенджер'
        return context

    def get_queryset(self):
        queryset = CustomUser.objects.exclude(user=self.request.user)
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(middle_name__icontains=query) |
                Q(department__icontains=query) |
                Q(role__icontains=query)
            )
        queryset = queryset.exclude(user=self.request.user)
        return queryset


def get_conversation_id(user1, user2):
    user_ids = [str(user1.id), str(user2.id)]
    sorted_user_ids = '-'.join(sorted(user_ids))
    return hashlib.sha256(sorted_user_ids.encode()).hexdigest()


def load_messages(request, user_id):
    if request.user.is_authenticated:
        recipient = get_object_or_404(User, id=user_id)
        conversation_id = get_conversation_id(request.user, recipient)
        messages = Message.objects.filter(conversation_id=conversation_id).order_by('timestamp')
        messages_data = [
            {
                'sender': message.sender.username,
                'recipient': message.recipient.username,
                'content': message.content,
                'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
            for message in messages
        ]
