from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from f4people import views

urlpatterns = [
    path('collections/', views.collections.as_view()),
    path('faces/', views.faces.as_view()),
    path('face_groups/', views.groups.as_view()),
    path('group_detail/', views.group_detail.as_view()),
    path('search/', views.search_group.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

