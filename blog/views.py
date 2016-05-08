from django.shortcuts import render, loader

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})