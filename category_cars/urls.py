from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.CategoryViewSet, basename='category')

urlpatterns = [
    # path('', views.CreateCategory.as_view()),
    # path('list/', views.ListCategory.as_view()),
    # path('detail/<int:pk>', views.UpdateCategory.as_view()),
    path('', include(router.urls)),
]