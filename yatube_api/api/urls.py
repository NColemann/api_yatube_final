from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

router = SimpleRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='post=comments-list',
)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
