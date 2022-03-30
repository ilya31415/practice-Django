"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path

from calculator import views

urlpatterns = [
    path('ricipe-dish/omlet/<int:servings>', views.omlet, name='omlet'),
    path('ricipe-dish/pasta/<int:servings>', views.pasta, name='pasta'),
    path('ricipe-dish/buter/<int:servings>', views.buter, name='buter'),
    path('', views.home, name='home'),
    path('ricipe-dish/', views.dish_1, name='dish_1'),



]
