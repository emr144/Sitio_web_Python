# chatapp/views.py

from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.username = request.user.username
            message.save()
            return redirect('chat')
    else:
        form = MessageForm()

    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chat.html', {'form': form, 'messages': messages})
