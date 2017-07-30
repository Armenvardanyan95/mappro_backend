from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, User
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'patch')
    permission_classes = (IsAuthenticated,)



