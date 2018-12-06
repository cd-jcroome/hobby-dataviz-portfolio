from django.urls import path

from . import views

app_name = 'vizzes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(r'<int:pk>/', views.VizView.as_view(), name='viz'),
    path(r'<int:pk>/VizData', views.VizData, name='VizData'),
    # path('ingest', views.IngestView, name='ingest'),
]