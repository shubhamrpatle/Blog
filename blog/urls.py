from django.urls import path
from .views import BlogSubmissionView,BlogSearchView

urlpatterns = [
    path('submit/', BlogSubmissionView.as_view(), name='blog_submit'),
     path('search/', BlogSearchView.as_view(), name='blog_search'),
]
