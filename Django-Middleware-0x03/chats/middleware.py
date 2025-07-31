# middleware.py
import logging
from datetime import datetime
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        return self.get_response(request)
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # Allow access only between 6 PM (18) and 9 PM (21), inclusive
        if current_hour < 18 or current_hour > 21:
            return HttpResponseForbidden("Access denied: Outside allowed hours (6PM–9PM)")
        return self.get_response(request)
