from rest_framework import routers
from apps.products.apis import BrandViewSet, ProductViewSet

router = routers.SimpleRouter()
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
