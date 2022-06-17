from django.urls import path
from .views import MobileDeviceView

urlpatterns = [

	path('mobile-devices/', MobileDeviceView.as_view()),
	path('mobile-devices/<int:id>', MobileDeviceView.as_view())
]