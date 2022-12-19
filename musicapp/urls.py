from django.urls import path,include
from musicapp import views
from rest_framework .routers import DefaultRouter


router = DefaultRouter()
router.register('Artist', views.ArtistList,)
router.register('songs', views.SongsList,)
router.register('playlist', views.CreatePlaylist,)
router.register('resent', views.ResentList,)
router.register('fav', views.CreateDeleteLikeView,)
urlpatterns = [
    path("register/", views.Register.as_view(),name="register"),
    path("login/", views.LoginAPIView.as_view(),name="login"),
    path('',include(router.urls)),

]