from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
def home(request):
    if request.method=="POST":
        form=ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Item Has Beenn Added To List")
    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})
def delete(request,list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    print(List.objects.all)
    messages.success(request, ("Item Has Beenn Deleted"))
    return redirect( 'home.html')
