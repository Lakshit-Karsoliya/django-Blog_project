from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import blog

# Create your views here.
def index(request):
    blogs=blog.objects.all()
    return render(request,'index.html',{'blogs':blogs})

def fullblog(request,s):
    blogs=blog.objects.get(id=s)
    if request.POST.get('DEL'):
        b=blog.objects.get(id=s)
        b.delete()
        return redirect('/')
    else:
        return render(request,'fullblog.html',{'blogs':blogs})

def addblog(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        content = request.POST['content']
       
        b=blog.objects.create(heading=heading,content=content)
        messages.Info(request,'added sucessfully')
        return redirect('/')
    else:
        return render(request,'addblog.html')