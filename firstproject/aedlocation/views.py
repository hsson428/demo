from django.shortcuts import render

from django.views.generic import View, TemplateView

from django.http import HttpResponse, JsonResponse


from django.core import serializers

# Create your views here.

class HomeView(TemplateView):
    # template_name = 'stocks/home.html'        # ORM객체를 사용하는 화면
    template_name = 'aedlocation/home2.html'

class SearchView2(View):
    def get(self, request, key):
        from .aedlocation_repository import AedlocationRepository
        import json

        repository = AedlocationRepository()
        searched_aed = repository.select_aedlocation_by_name(key)
        json_aed = json.dumps(searched_aed, ensure_ascii=False)
        return HttpResponse(json_aed, content_type="application/json")

class StocksDetailView2(View):
    def get(self, request, pk):

        from .aedlocation_repository import AedlocationRepository
        import json

        repository = AedlocationRepository()
        searched_aed = repository.select_aedlocation_by_num(pk)
        json_aed = json.dumps(searched_aed, ensure_ascii=False)
        return HttpResponse(json_aed, content_type="application/json")