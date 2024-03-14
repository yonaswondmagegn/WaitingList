from rest_framework_nested import routers
from .views import FormViewSet


route = routers.DefaultRouter()
route.register('form',FormViewSet)

urlpatterns = route.urls