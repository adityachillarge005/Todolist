from django.urls import path
from .import views
urlpatterns=[
    path("",views.Todos.as_view()),
    path('tododetails/<int:id>/',views.TodosDetails.as_view()),
]