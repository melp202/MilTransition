from rest_framework import routers
from .api import StateViewset, OrganizationViewset

router = routers.DefaultRouter()
router.register('api/states', StateViewset, 'states')
router.register('api/organizations', OrganizationViewset, 'organizations')

urlpatterns = router.urls