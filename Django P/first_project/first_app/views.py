from django.shortcuts import render
from first_app.models import User

# Create your views here.
def index(request):
    return render(request,'first_app/index.html')

def list(request):
    users_list = User.objects.order_by('first_name')
    users_dict = {'users':users_list}
    return render(request,'first_app/list.html',context=users_dict)
