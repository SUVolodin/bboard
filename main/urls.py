from .views import DeleteUserView
from .views import ChangeUserInfoView
from .views import other_page
from .views import user_activate, by_rubric
from django.urls import path

from .views import BBPasswordChangeView
from .views import BBLoginView
from .views import BBLogoutView, detail
from .views import index
from .views import profile
from .views import RegisterUserView, RegisterDoneView

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sing>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('account/password/change', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('account/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]
