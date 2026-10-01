from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import Test, Question, TestAttempt, Student

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        user = User.objects.create_user(username=username, password=password, first_name=name)
        Student.objects.create(user=user, name=name)
        return redirect('signup_success')
    return render(request, 'signup.html')

def signup_success(request):
    return render(request, 'signup_success.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    tests = Test.objects.all()
    return render(request, 'dashboard.html', {'student': request.user, 'tests': tests})

def start_test(request, test_id):
    if not request.user.is_authenticated:
        return redirect('login')
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(test=test)

    if request.method == "POST":
        correct = 0
        wrong = 0
        points = 0

        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            if selected_answer:
                if selected_answer == question.correct_option:
                    correct += 1
                    points += question.points
                else:
                    wrong += 1

        total_questions = questions.count()
        previous_attempts = TestAttempt.objects.filter(user=request.user, test=test).count()
        attempt_number = previous_attempts + 1

        TestAttempt.objects.create(
            user=request.user,
            test=test,
            total_questions=total_questions,
            correct=correct,
            wrong=wrong,
            points=points,
            attempt_number=attempt_number
        )

        return render(request, 'result.html', {
            'test': test,
            'total_questions': total_questions,
            'correct': correct,
            'wrong': wrong,
            'points': points,
            'attempt_number': attempt_number
        })

    return render(request, 'test.html', {'test': test, 'questions': questions})

def test_history(request):
    if not request.user.is_authenticated:
        return redirect('login')

    history = TestAttempt.objects.filter(user=request.user).order_by('-attempted_at')
    total_tests = history.count()
    total_questions = 0
    total_correct = 0
    total_wrong = 0
    total_points = 0

    for item in history:
        total_questions += item.total_questions
        total_correct += item.correct
        total_wrong += item.wrong
        total_points += item.points

    return render(request, 'test_history.html', {
        'history': history,
        'student': request.user,
        'total_tests': total_tests,
        'total_questions': total_questions,
        'total_correct': total_correct,
        'total_wrong': total_wrong,
        'total_points': total_points
    })

def logout(request):
    auth_logout(request)
    return redirect('home')

