from django.urls import path

from .views import signup_view,login_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('check-username/', check_username_view, name='check-username'),
]