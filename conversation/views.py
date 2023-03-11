from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk = item_pk)

    if item.created_by == request.user:
        return redirect('Dashboard:dashboard')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in = [request.user.id])

    # check if there is existing message with owner and logged in user
    if conversations:
        return redirect('conversationApp:detail', conversations.first().id)

    if request.method=='POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk = item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html',{
        'form': form
    }) 
    
@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in = [request.user.id])

    return render(request,'conversation/inbox.html',{
        'conversations': conversations,
    })

@login_required
def detail(request,pk):
    conversation = Conversation.objects.filter(members__in = [request.user.id]).get(pk=pk)

    # check if response is valid
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            
            return redirect('conversationApp:detail', pk=pk)
    # provide empty form
    else:
        form = ConversationMessageForm()
    return render(request, 'conversation/detail.html',{
        'conversation': conversation,
        'form':form
    })