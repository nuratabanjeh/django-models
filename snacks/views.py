from django.views.generic import ListView, DetailView
from .models import snacks

class ThingListView(ListView):
    template_name = "snacks_list.html"
    model = snacks

class ThingDetailView(DetailView):
    template_name = "snacks_detail.html"
    model = snacks