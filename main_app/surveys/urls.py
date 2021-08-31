from django.urls import path
from . import views
  
urlpatterns = [
    path('surveys/<int:pk>/', views.survey_detail),
    path('surveys/<str:status>/', views.surveys_by_status),
    path('surveys/', views.survey_index), 
    

    # the URLs for the APIs s
    url(r'^survey$', SurveyViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
    url(r'^survey/all$', SurveyViewSet.as_view(
        {
            'get': 'list',
        }
    )),
]