from django.views.generic import TemplateView, View


from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = 'home.html'

class SearchView2(View):
    def get(self, request, key):
        from .aedlocation_repository import AedlocationRepository
        import json

        repository = AedlocationRepository()
        searched_aed = repository.select_aedlocation_by_name(key)
        json_aed = json.dumps(searched_aed, ensure_ascii=False)
        return HttpResponse(json_aed, content_type="application/json")