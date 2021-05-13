from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from clustering import views

urlpatterns = [
    #path('collections/', views.collections.as_view()),
    path('faces/', views.faces.as_view()),
    #path('groups/', views.groups.as_view()),
    #path('group_detail/', views.group_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

