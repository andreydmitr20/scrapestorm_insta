import os
from datetime import datetime, timedelta, timezone

from django.db import IntegrityError
from django.db.models import F, Q
from django.shortcuts import get_object_or_404, render
from django.views import View
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import serializers, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from tasks.news.mylib.log import log
# from tasks.news.mylib.twilio_lib import MESSAGE_SID_LENGTH, send_sms
# from tasks.news.news import news_scraper
from utils.views_functions import (
    API_TEXT_SEARCH,
    API_TEXT_SHORT,
    delete_simple,
    filter_params_simple,
    filter_simple,
    get_int_request_param,
    insert_simple,
    order_simple,
    pagination_simple,
    print_query,
    search_simple,
    select_simple,
    to_int,
    update_simple,
    is_serializer_error_duplicate_value,
)

from config import config

# from .models import Clients
from .serializers import EmptySerializer


@extend_schema(tags=["check ok"])
class CheckView(GenericAPIView):
    """check ok"""

    permission_classes = [AllowAny]
    queryset = []
    serializer_class = EmptySerializer

    @extend_schema(
        description="check ok",
        # parameters=[
        #     OpenApiParameter("url", description='url'),
        # ],
    )
    def get(self, request, format=None):
        # result = get_page(request.GET.get("url"))
        return Response([{"api_status": "ok"}], status=status.HTTP_200_OK)
