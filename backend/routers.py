from rest_framework import routers

from .viewsets import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'backend', ArticleViewSet)
