from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .serializers import FilmSerializer, FilmFullSerializer
from .models import Film

class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    authentication_classes = (TokenAuthentication, )

    def retrieve(self, request, *args, **kwargs):
        film = self.get_object()
        serializer = FilmFullSerializer(film)
        return Response(serializer.data)