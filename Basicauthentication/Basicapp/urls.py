from django.conf.urls import url,include
from Basicapp import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('emp_viewset',views.DataViewSet)

urlpatterns = [
	url(r'',include(router.urls))

]