from django.shortcuts import render, redirect
from . models import Productss, UsrProfile, Newsfeed
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, DeleteView, UpdateView
from .forms import AdminProduct, Adnewz

from django.db.models import Q
# Create your views here.


def home(request):
    return render(request, 'index.html')


def categories(request):
    return render(request, 'categories.html')


def fruits(request):
    fruits = Productss.objects.filter(Category=1)
    print(fruits)
    return render(request, 'fruits.html', {'fruit': fruits})


def veggies(request):
    veg = Productss.objects.filter(Category=2)
    print(veg)
    return render(request, 'veggies.html', {'veg': veg})


def details(request, id):
    pro = Productss.objects.get(id=id)
    return render(request, 'details.html', {'pro': pro})


def product(request):
    search_this = ''
    if request.GET.get('search_this'):
        search_this = request.GET.get('search_this')
        print(search_this)

    prod = Productss.objects.filter(
        Q(name__icontains=search_this) | Q(description__icontains=search_this))
    # prod = Productss.objects.all()
    return render(request, 'productpage.html', {'prod': prod})


def registerpage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            # to create an instance of user so that we can do operations with it
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was created')
            # login(request,user)
            # return redirect('list')
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exists')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'username/password incorrect')
    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    messages.error(request, 'user loged out')
    return redirect('/')


@login_required(login_url='login')
def Profilepage(request):
    profile = request.user
    ad = UsrProfile.objects.get(user=profile)
    bd = Newsfeed.objects.filter(usr=profile)
    return render(request, 'profile.html', {'profile': ad, 'post': bd})


def news(request):
    vnew = Newsfeed.objects.all()
    return render(request, 'news.html', {'vn': vnew})


class Proupdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = UsrProfile
    template_name = 'update_profile.html'
    fields = ['name', 'email', 'email', 'proimg']
    context_object_name = 'form'
    success_url = reverse_lazy('profile')


class Adpro(CreateView):
    form_class = AdminProduct
    template_name = 'addproduct.html'
    context_object_name = 'form'

    success_url = reverse_lazy('products')


class ModifyV(UpdateView):
    model = Productss
    template_name = 'addproduct.html'
    fields = '__all__'
    success_url = reverse_lazy('products')


class Pdelete(DeleteView):
    model = Productss
    template_name = 'del.html'
    context_object_name = 'dlt'
    success_url = reverse_lazy('products')


class Adnewz(CreateView, LoginRequiredMixin):
    login_url = 'login'
    model = Newsfeed
    fields = '__all__'
    template_name = 'addnews.html'
    context_object_name = 'nwz'
    success_url = reverse_lazy('news')


class Upnews(UpdateView, LoginRequiredMixin):
    login_url = 'login'
    model = Newsfeed
    fields = '__all__'
    template_name = 'addnews.html'
    success_url = reverse_lazy('news')


class Dltnews(DeleteView, LoginRequiredMixin):

    model = Newsfeed
    template_name = 'deleteprof.html'
    context_object_name = 'dlt'
    success_url = reverse_lazy('profile')
