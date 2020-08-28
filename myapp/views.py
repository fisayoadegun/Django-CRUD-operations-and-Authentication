from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Flower
from .forms import MyForm
from django.db.models import Q
from django.contrib.auth.decorators import permission_required,login_required
#Create your views here.
def index(request):
    q = request.GET.get('q', None)
    items = ''
    flowers = Flower.objects.all()
    if q is not None:
        flowers = flowers.filter(Q(title__contains=q)|
                                Q(description__contains=q)
                                )
    return render(request, 'myapp/index.html', {'flowers': flowers})

# def index(request):  # new
#     query = request.GET.get('query')
#     object_list = Flower.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
#     return render(request, 'myapp/index.html', object_list)

@permission_required('myapp.add_flower')
def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'myapp/create.html', {'form':form})

# @permission_required('myapp.change_flower')
# def edit(request, pk=None):
#     flower = get_object_or_404(Flower, pk=pk)
#     if request.method == 'POST':
#         form = MyForm(request.POST, request.FILES, instance=flower)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = MyForm(instance=flower)
#     return render(request, 'myapp/edit.html', {'form':form})
#
# @permission_required('myapp.delete_flower')
# def delete(request, pk=None):
#     flower = get_object_or_404(Flower, pk=pk)
#     if request.method=='POST':
#         flower.delete()
#         return redirect('index')
#     return render(request, 'myapp/confirm_delete.html', {'flower':flower})
#

    # flower.delete()
    # return redirect('myapp/index.html')

def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'myapp/index.html', {'flowers': flowers})


def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'myapp/detail.html', {'flower':flower})
