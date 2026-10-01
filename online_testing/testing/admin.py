from django.contrib import admin

from .models import (
    Student,
    Test,
    Question,
    TestAttempt
)


admin.site.register(Student)

admin.site.register(Test)

admin.site.register(Question)

admin.site.register(TestAttempt)