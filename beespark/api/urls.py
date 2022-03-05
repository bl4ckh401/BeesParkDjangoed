from django.urls import path
from .views import CreateTableView, Reservetableview

urlpatterns = [
    path('/create', CreateTableView.as_view()),
    path('', Reservetableview.as_view()),
]
