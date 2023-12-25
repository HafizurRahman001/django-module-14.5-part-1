from django.shortcuts import render
from . forms import contactForm

# Create your views here.
def home(request):
    return render (request,'first_app/home.html')

def modelForm(request):
    form = contactForm()
    return render(request,'first_app/modelform.html',{'form':form})
