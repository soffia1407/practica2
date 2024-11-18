from django.shortcuts import render, redirect
from .models import Request, Category
from .forms import RequestForm, CategoryForm


def home(request):
    requests = Request.objects.filter(status='done').order_by('-created_at')[:4]
    return render(request, 'core/home.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.status = 'new'
            form.save()
            return redirect('core:home')
    else:
        form = RequestForm()
    return render(request, 'core/create_request.html', {'form': form})

def view_requests(request):
    requests = Request.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/view_requests.html', {'requests': requests})

def delete_request(request, pk):
    request = Request.objects.get(pk=pk)
    request.delete()
    return redirect('core:view_requests')

def change_request_status(request, pk):
    request = Request.objects.get(pk=pk)
    if request.status == 'new':
        request.status = 'in_progress'
        request.save()
    elif request.status == 'in_progress':
        request.status = 'done'
        request.save()
    return redirect('core:admin_panel')

def admin_panel(request):
    requests = Request.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request,'core/admin_panel.html', {'requests': requests, 'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:admin_panel')
    else:
        form = CategoryForm()
    return render(request, 'core/add_category.html', {'form': form})

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('core:admin_panel')

