from django.urls import path
from .views import ArticlePostListView, ArticlePostDetailView, CasinoListView, CasinoDetailView, GameSupplierListView, GameSupplierDetailView

urlpatterns = [
    path('article/', ArticlePostListView.as_view()),
    path('article/<slug>/', ArticlePostDetailView.as_view()),

    path('casino/', CasinoListView.as_view()),
    path('casino/<slug>/', CasinoDetailView.as_view()),
    path('gamesupplier/', GameSupplierListView.as_view()),
    path('gamesupplier/<slug>/', GameSupplierDetailView.as_view()),
]
