from django.urls import path

from .views import HomePageView,aboutPageView,dashboardPageView,signupPageView,loginPageView,contactPageView


urlpatterns = [
        path("", HomePageView.as_view(), name="home.html"),
        path("dashboard", dashboardPageView.as_view(), name="dashboard.html"),
        path('About/',aboutPageView.as_view(), name='about.html'),
         path('contact/',contactPageView.as_view(), name='contact.html'),
       path('login/',loginPageView.as_view(), name='login.html'),
       path('signup/',signupPageView.as_view(), name='signup.html'),
       
]