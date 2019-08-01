from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse


# Create your views here.


def list(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'billboard/list.html', {'posts': posts})


def add(request):
    item = request.GET.get('item', '')
    status = 409
    if item in posts:
        msg: "post exists"
    else:
        posts.append(item)
        msg: "post created"
        status = 201
    return JsonResponse({"msg": msg}, status=status)


def get(request):
    item = request.GET.get('item', '')
    if item in posts:
        return HttpResponse(item)
    else:
        raise Http404("No such item")

def login (request):
    if request.POST:
        username= request.POST["username"]
        password= request.POST["password"]
        user = authenticate (request, username= username,password= password)
        if user is not None:
                return render(request, "billboard/success.html")
        else:
            return HttpResponse("<h1>You are not registered.</h1>")

    else:
        return render(request, 'billboard/login.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
    return render(request,
        "billboard/register.html",
        { "form": form }
    )

