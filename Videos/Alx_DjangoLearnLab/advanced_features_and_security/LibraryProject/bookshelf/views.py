from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import ExampleModel
from .forms import ExampleForm 
def book_list(request):
  books = Book.objects.all()
  return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('app_name.can_view', raise_exception=True)
def view_item(request, pk):
    item = get_object_or_404(ExampleModel, pk=pk)
    return render(request, 'view_item.html', {'item': item})

@permission_required('app_name.can_create', raise_exception=True)
def create_item(request):
    if request.method == 'POST':
        form = ExampleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ExampleModelForm()
    return render(request, 'create_item.html', {'form': form})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_item(request, pk):
    item = get_object_or_404(ExampleModel, pk=pk)
    if request.method == 'POST':
        form = ExampleModelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=pk)
    else:
        form = ExampleModelForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_item(request, pk):
    item = get_object_or_404(ExampleModel, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'confirm_delete.html', {'item': item})


