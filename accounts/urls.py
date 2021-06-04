from rest_framework.routers import SimpleRouter

from accounts.views import ProfileViewSet

router = SimpleRouter()
router.register(r'profile', ProfileViewSet, basename='user_profile')
