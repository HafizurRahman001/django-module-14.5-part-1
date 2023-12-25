from django.shortcuts import render
from . forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'first_app/home.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request,'first_app/djangoform.html',{'form':form})