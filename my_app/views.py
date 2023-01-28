from django.shortcuts import render,redirect
from django.http import HttpResponse

from my_app.models import Customer

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        currentuser = Customer.objects.filter(username=username)

        if not currentuser:
            return HttpResponse("No user found")

        user = currentuser[0]

        if user.password == password:
            request.session['username'] = user.username
            return redirect(dashboard)
        else:
            return redirect(login)
    return render(request, 'Login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword =request.POST['confirmpass']

        if password == confirmPassword:
            currentuser = Customer.objects.create(username = username, email = email, password = password)
            currentuser.save()
            return redirect(login)
        else:
            return render(request, 'SignUp.html')
    return render(request, 'SignUp.html')

def dashboard(request):

    username = request.session.get('username')
    context = {'username':username}
    return render(request, 'dashboard.html', context=context)