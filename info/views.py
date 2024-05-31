from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Notice
from lms.models import Course

def homeview(request):
    courses = Course.objects.all().order_by('-id')
    context = {'courses':courses}
    return render(request, 'info/home.html', context)


def contactview(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        print('POST METHOD CALLED')  
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.instance.full_name},Your form submitted successfully!!!We will contact you shortly.')
            return redirect('info:contact')
        
    cform = ContactForm
    context ={
        'form':cform
        }
    return render(request, 'info/contact.html',context)



def noticeview(request):
    notices = Notice.objects.all().order_by('-id')
    context = {'notices':notices}
    return render(request, 'info/notice.html', context)

