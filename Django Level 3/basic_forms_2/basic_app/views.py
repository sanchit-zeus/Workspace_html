from django.shortcuts import render
from basic_app import forms
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def index2(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do something
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'basic_app/forms.html',{'form':form})
