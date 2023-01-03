from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete, AppLogin, SignUp
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signin/', AppLogin.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),


    path('', TodoList.as_view(), name='todos'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo'),
    path('todo-create/', TodoCreate.as_view(), name='todo-create'),
    path('todo-update/<int:pk>/', TodoUpdate.as_view(), name='todo-update'),
    path('todo-delete/<int:pk>/', TodoDelete.as_view(), name='todo-delete'),

    path('changePassword/', auth_views.PasswordResetView.as_view(template_name='todo_app/changePassword.html'),
         name='reset_password'),
    path('resetPasswordSent/', auth_views.PasswordResetDoneView.as_view(template_name='todo_app/resetPasswordSent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('resetPasswordComplete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
