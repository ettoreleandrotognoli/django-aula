from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from sample.models import Movement
from django.urls import path
from django.urls import reverse_lazy


class MovementViewMixin():
    model = Movement
    fields = '__all__'
    success_url = reverse_lazy('movement-list')
    template_name = "base/form.html"

class MovementListView(MovementViewMixin,ListView):
    template_name = "movement/list.html"

class MovementCreateView(MovementViewMixin,CreateView):
    pass

class MovementUpdateView(MovementViewMixin,UpdateView):
    pass

# Create your views here.
urlpatterns = [
    path('movement/',MovementListView.as_view(),name="movement-list"),
    path('movement/create/',MovementCreateView.as_view(),name="movement-create"),
    path('movement/<int:pk>/',MovementUpdateView.as_view(),name="movement-update"),
]