
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from user.models import User

# Create your views here.
def index(request):
  return render(request,'index.html')


def user(request) :
  user_list = User.objects.order_by('first_name')
  user_dict = {"users":user_list}
  return render(request,'user.html', context=user_dict)
