from dependencies import Injector, this
from dependencies.contrib.rest_framework import api_view, generic_api_view
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .commands import UserOperations
from .filtersets import UserFilter
from .serializers import UserSerializer


@api_view
class UserAction(Injector):

    get = this.command.do
    command = UserOperations


@api_view
class UserLogin(Injector):

    get = this.command.login
    command = UserOperations

    permission_classes = (IsAuthenticated,)


@generic_api_view
class UserRetrieveView(Injector):

    get = this.command.retrieve
    command = UserOperations

    queryset = User.objects.all()
    serializer_cls = UserSerializer
    lookup_field = "username"
    lookup_url_kwarg = "nick"


@generic_api_view
class UserListView(Injector):

    get = this.command.list
    command = UserOperations

    queryset = User.objects.all()
    serializer_cls = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_cls = UserFilter
    pagination_cls = LimitOffsetPagination
