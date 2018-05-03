from __future__ import absolute_import

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from ._django import apply_http_methods, create_handler


def api_view(injector):
    """Create DRF class-based API view from injector class."""

    handler = create_handler(APIView)
    apply_http_methods(handler, injector)
    return handler


def generic_api_view(injector):
    """Create DRF generic class-based API view from injector class."""

    handler = create_handler(GenericAPIView)
    apply_http_methods(handler, injector)
    apply_generic_view_methods(handler, injector)
    return handler


def apply_generic_view_methods(handler, injector):

    handler.queryset = injector.queryset
    handler.serializer_class = injector.serializer_cls
    if "lookup_field" in injector:
        handler.lookup_field = injector.lookup_field
    if "lookup_url_kwarg" in injector:
        handler.lookup_url_kwarg = injector.lookup_url_kwarg
    if "filter_backends" in injector:
        handler.filter_backends = injector.filter_backends
    if "filter_cls" in injector:
        handler.filter_class = injector.filter_cls
    if "pagination_cls" in injector:
        handler.pagination_class = injector.pagination_cls


# TODO:
#
# APIView.renderer_classes
# APIView.parser_classes
# APIView.authentication_classes
# APIView.throttle_classes
# APIView.permission_classes
# APIView.content_negotiation_class
# APIView.metadata_class
# APIView.versioning_class
#
# TODO: Protect from usage `pagination_class` instead of
# `pagination_cls`.
