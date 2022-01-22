from django.urls import path
from . import views

app_name='polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),   # /polls/5/
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'), # /polls/5/reesults/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]



    ### Before conversion to generic views
    # path('', views.index, name = 'index'),
    # path('<int:question_id>/', views.detail, name="detail"),   # /polls/5/
    # path('<int:question_id>/results', views.results, name='results'), # /polls/5/reesults/
    # path('<int:question_id>/vote/', views.vote, name='vote'),