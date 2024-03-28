#####################
# Base Custom mixins
#####################
from rest_framework.exceptions import ValidationError

from core.enums import Codes
from core.utils.exception import ResponseException
from core.utils.response import ApiResponse


class ResponseMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return ApiResponse.success(data=serializer.data)


class CreateSuccessResponseMixin:

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return ApiResponse.success(self.message if hasattr(self, "message") else "Successfully created")


class ValidateErrorMixin:

    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except ValidationError as e:
            key, value = next(iter(e.detail.items()))
            ResponseException(value[0], error_code=Codes.INVALID_PARAMETER_VALUE)
