from .views import ChangeUserInfoView
from .views import other_page
from django.urls import path

from .views import BBPasswordChangeView
from .views import BBLoginView
from .views import BBLogoutView
from .views import index
from .views import profile

app_name = 'main'
urlpatterns = [
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('account/password/change', BBPasswordChangeView.as_view(), name='password_change'),
    path('account/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]
