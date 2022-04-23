from django.views.generic import ListView, DetailView
from .models import Post2

class PostList(ListView):
    model = Post2
    ordering = '-pk'
    template_name = "blog2/index2.html"
    
class PostDetail(DetailView):
    model = Post2
    template_name = "blog2/index2_pages.html"