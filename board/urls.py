from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comment/', CommentListCreateView.as_view(), name='comment-list-create'),
]
