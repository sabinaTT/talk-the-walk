from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    # STACK MODEL
    path('stacks/', views.ListStacks.as_view(), name='list_stacks'),
    path('stacks/new/', views.Create_Stack.as_view(), name='create_stack'),
    path('stacks/<int:pk>/', views.StackDetail.as_view(), name='stack_detail'),
    path('stacks/<int:pk>/update', views.Update_Stack.as_view(), name='update_stack'),
    path('stacks/<int:pk>delete', views.DeleteStack.as_view(), name='delete_stack'),
    # QUESTION MODEL
    # path('questions/', views.questions_index, name='question_index'),
    path('questions/<int:question_id>', views.questions_show, name='question_show'),
    path('questions/create/', views.Create_Question.as_view(), name='question_form'),
    path('questions/<int:pk>/update/', views.Update_Question.as_view(), name='question_update'),
    path('questions/<int:pk>/delete/', views.Delete_Question.as_view(), name='question_confirm_delete'),
    path('user/<username>', views.profile, name='list_stacks'),
    # AUTH
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]