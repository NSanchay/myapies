from django.urls import path
from .views import Myapis, MyapiDetail, MyapiCreate, MyapiUpdateDelete


urlpatterns = [
    path('', Myapis.as_view()),
    path('<int:pk>/',MyapiDetail.as_view()),
    path('create/', MyapiCreate.as_view()),
    path('detail/<int:pk>/', MyapiUpdateDelete.as_view()),
]
