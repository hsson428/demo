
from django.urls import path

from .views import HomeView, SearchView2, StocksDetailView2

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search2/<str:key>', SearchView2.as_view(), name='search'),
    path('detail2/<str:pk>', StocksDetailView2.as_view(), name='detail'),
]
