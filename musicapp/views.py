from django.contrib.auth import authenticate, login

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from musicapp.models import Artist, Favourite, Playlist, Resent, Songs
from django.db.models import Q
from musicapp.permissions import IsAdminUserOrReadOnly
from musicapp.serializers import ArtistSerializer, FavSerializer, LoginSerializer, PlaylistSerializer, ResentSerializer, SongSerializer, UserSerializer

from .utils import get_tokens_for_user
# Create your views here.


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        a = request.data
        if 'username' not in a or 'password' not in a:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = a['username']
        password = a['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(user)
            return Response({**auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class Register(generics.CreateAPIView):
    """
    Register a new account.
    """
    serializer_class = UserSerializer

class ArtistList(viewsets.ModelViewSet):
    """
    List of all Artist.
    """
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    permission_classes = [IsAuthenticated,
                          IsAdminUserOrReadOnly
                            ]

class SongsList(viewsets.ModelViewSet):
    """
    List of all Songs.
    """
    serializer_class = SongSerializer
    queryset = Songs.objects.all()
    permission_classes = [IsAuthenticated,
                          IsAdminUserOrReadOnly
                            ]

class CreatePlaylist(viewsets.ModelViewSet):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [
        IsAuthenticated, ]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CreateDeleteLikeView(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(user=self.request.user) & Q(song=self.request.data['song']))
        if subset.count() > 0:
            subset.first().delete()
            return
        serializer.save(user = self.request.user)
        
class ResentList(viewsets.ModelViewSet):
   
    serializer_class = ResentSerializer
    queryset = Resent.objects.all()
    permission_classes = [
        IsAuthenticated, ]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
