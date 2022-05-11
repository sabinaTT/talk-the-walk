from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('stacks/', views.ListStacks.as_view(), name='list-stacks'),
    path('stacks/new/', views.Create_Stack.as_view(), name='create-stack'),
    path('stacks/<int:pk>/', views.StackDetail.as_view(), name='stack_detail'),
    path('stacks/<int:pk>/update', views.Update_Stack.as_view(), name='update-stack'),
    # path('stacks/<int:pk>delete', views.DeleteStack.as_view(), name='delete-stack'),
    path('questions/', views.list_questions, name='list_questions'),
    path('questions/<int:question_id>', views.view_question, name='view_question'),
    path('questions/create/', views.Create_Question.as_view(), name='create_question'),
    path='questions/<int:pk>/update/', views.Update_Question.as_view(), name='update_question'),
    path='questions/<int:pk>/delete/', views.Delete_Question.as_view(), name='Delete_Question'),
]