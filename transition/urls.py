from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
# from .api import StateViewset, OrganizationViewset


urlpatterns = [
    path('states/', views.StateList.as_view(), name='state_list'),
    path('states/<int:pk>', views.StateDetail.as_view(), name='state_detail'),
    path('organizations/', views.OrganizationList.as_view(),
         name='organization_list'),
    path('organizations/<int:pk>', views.OrganizationDetail.as_view(),
         name='organization_detail')
]


# router = routers.DefaultRouter()
# router.register('api/states', StateViewset, 'states')
# router.register('api/states/<int:pk>', StateViewset, 'state_details')
# router.register('api/organizations', OrganizationViewset, 'organizations')

# urlpatterns = router.urls
