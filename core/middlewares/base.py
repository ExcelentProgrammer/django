from django.http.response import JsonResponse

from core.exceptions import BreakException


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except BreakException as e:
            return self.process_exception(request, e)
        return response

    def process_exception(self, request, e):
        if isinstance(e, BreakException):
            error_data = {
                'message': e.message,
                "data": e.data,
                "errors": [
                    e.args.__str__(),
                ]
            }
            return JsonResponse(error_data)
