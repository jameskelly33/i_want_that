from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    send_mail(
        "Subject here",
    "Here is the message.",
    "jameskelly33@gmail.com",
    ["jameskelly33@gmail.com"],
    fail_silently=False,
    )
    
    return render(request,'home/index.html')



