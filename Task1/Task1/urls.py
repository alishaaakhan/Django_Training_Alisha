"""
URL configuration for Task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# from sistec import views as s1
# from aids import views as a1
# from cs import views as c1
urlpatterns = [
    path("sistec/",include('sistec.urls')),
    path("aids/",include('aids.urls')),
    path("cs/",include('cs.urls')),
    # path("home/",s1.home),
    # path("aboutaids", a1.aboutAids),
    # path("aboutcs",c1.aboutCs),
    # path("admin/", admin.site.urls),
]
