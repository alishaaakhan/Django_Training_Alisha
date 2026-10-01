from django.shortcuts import render, redirect
from .models import User, Student

def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html")

def saveuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html",
                          {"errormsg": "Username already exists. Please login."})

        User.objects.create(username=username, password=password, name=name)
        return redirect("login")

    return redirect("signup")

def login(request):
    return render(request, "login.html")

def loginvalidation(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username, password=password).first()

        if user:
            request.session["username"] = user.username
            return redirect("studentregistration")
        else:
            return render(request, "login.html",
                          {"errormsg": "Invalid username or password."})

    return redirect("login")

def studentregistration(request):
    if "username" not in request.session:
        return redirect("login")
    return render(request, "studentregistration.html")

def savestudent(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        student_id = request.POST.get("student_id")
        branch = request.POST.get("branch")

        Student.objects.create(
            student_name=student_name,
            student_id=student_id,
            branch=branch
        )
        return redirect("success")

    return redirect("studentregistration")

def success(request):
    return render(request, "success.html")

def logout(request):
    request.session.flush()
    return redirect("home")
