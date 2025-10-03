from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Message

def user_list(request):
    query = request.GET.get("q")
    users = User.objects.all()
    if query:
        users = users.filter(username__icontains=query)
    return render(request, "chat/user_list.html", {"users": users})

def private_chat(request, username):
    other_user = get_object_or_404(User, username=username)
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by("timestamp")
    return render(request, "chat/private_chat.html", {
        "other_user": other_user,
        "messages": messages,
    })
