from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem


def index(request):
    latest_grocery_list = GroceryItem.objects.order_by('created_date')
    context = {'latest_grocery_list': latest_grocery_list}
    return render(request, 'grocerylist/index.html', context)


def add_item(request):
    if request.method == 'POST':
        add_item = request.POST['add_item']
        created_date = timezone.now()
        new_item = GroceryItem(text_description=add_item, created_date=created_date)
        new_item.save()
        return HttpResponseRedirect(reverse('grocerylist:index'))


def delete_item(request, pk):
    delete_item = get_object_or_404(GroceryItem, pk=pk)
    delete_item.delete()
    return HttpResponseRedirect(reverse('grocerylist:index'))