from django.shortcuts import render
from .models import Post1

def index1(request):
    posts1 = Post1.objects.all().order_by('-pk')
    return render(
        request,
        'blog1/index1.html',
        {
            'posts1' : posts1
        }
    )
    
def index1_pages(request, pk):
    post = Post1.objects.get(pk=pk)
    return render(
        request,
        'blog1/index1_pages.html',
        {
            'post':post
        }
    )