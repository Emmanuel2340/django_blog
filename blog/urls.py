from django.urls import path
from blog.views import BlogHomeView,BlogDetailView

urlpatterns = [
    path('',BlogHomeView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail')
]