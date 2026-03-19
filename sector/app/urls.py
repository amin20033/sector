from django.urls import path
from .views import AnalyzeSectorView,RegisterView,LogoutView

urlpatterns = [
    path('analyze/<str:sector>/', AnalyzeSectorView.as_view()),
    path("register/",RegisterView.as_view()),
    path("logout/",LogoutView.as_view(),name="logout"),
]