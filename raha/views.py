from django.shortcuts import render
from django.http import HttpResponse
from  .  models import Topic

def index(request):
    topics =  Topic.objects.all().order_by('-id')
    context ={'topics':topics}
    return render(request,'index.html',context)

def contact(request):
    topics = Topic.objects.all().order_by('-id')[:2]
    context = {'topics':topics}
    return render(request,'contact.html',context)

def  about(request):
    return  render(request,'about.html')

from django.shortcuts import render, redirect
from .models import Topic

def submit(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment:
            # Assuming you have a logged-in user, you can associate the comment with the current user
            topic = Topic.objects.create(user=request.user, comment=comment)
            return redirect('contact')  # Redirect to the index page after successful submission
    return render(request, 'index.html')