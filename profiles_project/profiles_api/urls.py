from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
#여기서 첫번째 parameter인 'hello-viewset'은 
# localhost:8000/api 에서 hello-viewset을 선택했을 때 url접미사가 hello-viewset이 됨
#basename은 해당 url의 이름 (templete에서 쓰이지 않을까)
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
#UserProfileViewset에 queryset이 있기때문에 basename을 안정해줘도 됨 
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
