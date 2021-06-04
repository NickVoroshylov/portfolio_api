from rest_framework.routers import SimpleRouter

from portfolios.views import PictureViewSet

router = SimpleRouter()
router.register(r'pictures', PictureViewSet, basename='pictures_feed')
