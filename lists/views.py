from django.shortcuts import render, redirect,reverse,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishListItem
from .forms import WishListItemForm
from django.conf import settings
import os
import requests
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.files.base import ContentFile



# Create your views here.
def jameslist(request):
    person='james'
    order_by = request.GET.get('order_by', '-id')
    listitems = WishListItem.objects.filter(person='james').order_by(order_by)
    
    context = { 
        'listitems': listitems,
        'current_order_by': order_by,
        'person':person,
    }
    return render(request, 'lists/index.html', context)


def orlalist(request):
    person='orla'
    order_by = request.GET.get('order_by', 'price')
    listitems= WishListItem.objects.filter(person='orla').order_by(order_by)
    context={
        'listitems': listitems,
        'current_order_by': order_by,
        'person':person
    }
    return render(request,'lists/index.html',context)

def jacklist(request):
    person='jack'
    order_by = request.GET.get('order_by', 'price')
    listitems= WishListItem.objects.filter(person='jack').order_by(order_by)
    context={
        'listitems': listitems,
        'current_order_by': order_by,
        'person':person,
    }
    return render(request,'lists/index.html',context)

def flatlist(request):
    person='flat'
    order_by = request.GET.get('order_by', 'price')
    listitems= WishListItem.objects.filter(person='flat').order_by(order_by)
    context={
        'listitems': listitems,
        'current_order_by': order_by,
        'person':person,
    }
    return render(request,'lists/index.html',context)





@login_required
def add_to_wish_list(request):
    if request.method == 'POST':
        form = WishListItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            user_email=request.user.email
            username= request.user.username
            item_url= item.url
            
            if user_email==settings.EMAIL_HOST_USER:
                send_mail(
                f"{username} added something to their Wish List",
                f"I wished a wish,see what it is---- {item_url}",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_SECONDARY_USER],
                fail_silently=False,
                )
            else:
                send_mail(
                f"{username} added something to their Wish List",
                f"I wished a wish,see what it is---- {item_url}",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
                )
                    
             
         

            return redirect('home')
    else:
        form = WishListItemForm()
    return render(request, 'lists/add_to_wish_list.html', {'form': form})

@login_required
def delete_wish_list_item(request, item_id):
    item = get_object_or_404(WishListItem, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'lists/delete_wish_list_item.html', context)
