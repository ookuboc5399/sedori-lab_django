from django.views.generic import View
from django.shortcuts import render
from .forms import SearchForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'api/index.html', {
            'form': form
        })

class EbayView(View):
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, 'api/ebay.html', {
            'form': form
        })