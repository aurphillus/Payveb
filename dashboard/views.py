from django.shortcuts import render
from django.http import HttpResponse
from .forms import DealerInfo
# Create your views here.

def add_dealer(request):
    # profile = request.user.userprofile
    form = DealerInfo()
    if request.method == 'POST':
        form = DealerInfo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved')

    context={
    'form':form,
    }
    return render(request,'dashboard/add_dealer.html',context)
