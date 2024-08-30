from django.shortcuts import render

# Create your views here.
def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']