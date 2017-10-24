# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home_page(request):
# 	return HttpResponse("<html><title>To-Do lists</title></html>")
# home_page = None

from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html')

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})