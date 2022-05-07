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
]