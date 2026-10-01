from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
import joblib

def home(request):
    return render(request, "home.html")

def studentregister(request):
    if request.method == "POST":
        student_id = request.POST['student_id']
        name = request.POST['name']
        password = request.POST['password']
        branch = request.POST['branch']
        student_number = request.POST['student_number']
        email = request.POST['email']

        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists.")
            return render(request, "studentregister.html")

        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "studentregister.html")

        Student.objects.create(
            student_id=student_id, name=name, password=password,
            branch=branch, student_number=student_number, email=email
        )
        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "studentregister.html")

def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        student = Student.objects.filter(name=name, password=password).first()

        if student:
            request.session['student_id'] = student.student_id
            request.session['student_name'] = student.name
            return redirect("prediction")
        else:
            messages.error(request, "Invalid student name or password.")
            return render(request, "login.html")

    return render(request, "login.html")

def prediction(request):
    if 'student_id' not in request.session:
        return redirect("login")
    return render(request, "prediction.html")

def result(request):
    if 'student_id' not in request.session:
        return redirect("login")

    scaler = joblib.load('scalermodel.pkl')
    mlmodel = joblib.load('mlmodel.pkl')

    cgpa = float(request.GET['cgpa'])
    iq = float(request.GET['iq'])
    profile_score = float(request.GET['profile_score'])
    lis = [cgpa, iq, profile_score]

    scaled_input = scaler.transform([lis])
    ans = mlmodel.predict(scaled_input)[0]

    if ans == 1:
        result_message = "Congratulations! You're Placed 🎉"
        result_description = "Your profile indicates a positive placement prediction."
    else:
        result_message = "You Need to Study More 📚"
        result_description = "Keep improving your skills, CGPA and overall profile."

    return render(request, "result.html", {
        'ans': ans,
        'lis': lis,
        'result_message': result_message,
        'result_description': result_description
    })

