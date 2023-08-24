from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CarView

router = DefaultRouter()
router.register("car", CarView)


urlpatterns = [
    # path('auth/', include('dj_rest_auth.urls')),
    # path('register/',RegisterView.as_view()),
]
urlpatterns += router.urls