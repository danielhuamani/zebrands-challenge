from rest_framework import routers
from apps.products.apis import BrandViewSet, ProductViewSet, ChannelViewSet

router = routers.SimpleRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'channels', ChannelViewSet)

urlpatterns = router.urls
