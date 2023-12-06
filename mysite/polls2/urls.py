from django.urls import path
from . import views

app_name = 'polls2'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('results/', views.ResultsView.as_view(), name='results'),
    # path('vote/', views.VoteView.as_view(), name='vote_list'),
]