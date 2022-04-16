from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  (WatchListApiView, WatchListDetailApiView, StreamPlatformListAV, StreamPlatformDetailAv, ReviewList, ReviewDetail,ReviewCreate, StreamPlatformViewSet)

router = DefaultRouter()
router.register('stream', StreamPlatformViewSet, basename='streamplatform')


urlpatterns = [
    # path('list/', movie_list, name="movie_list"),
    # path('<int:pk>/', movie_detail, name="movie_detail")
    path('watchlist/', WatchListApiView.as_view(), name="movie_list"),
    path('watchlist/<int:pk>/', WatchListDetailApiView.as_view(), name='movie_detail'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformListAV.as_view(), name="stream-list"),

    # path('stream/<int:pk>/', StreamPlatformDetailAv.as_view(), name="streamplatform-detail"),
    # path('stream/1/review/', ReviewList.as_view(), name='review-list'), 
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'), 
    # path('review', ReviewList.as_view(), name='review-list')

    path('<int:pk>/reviews', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
     
    

]
