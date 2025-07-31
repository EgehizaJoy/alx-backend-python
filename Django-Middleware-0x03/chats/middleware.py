# middleware.py
import logging
from datetime import datetime
from django.http import HttpResponseForbidden
from django.utils.timezone import now
from django.http import HttpResponseForbidden
from collections import defaultdict, deque
import time

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
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Store timestamps of requests per IP
        self.request_logs = defaultdict(deque)
        self.time_window = 60  # seconds
        self.message_limit = 5

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/api/'):  # Apply to API POSTs
            ip = self.get_client_ip(request)
            current_time = time.time()
            timestamps = self.request_logs[ip]

            # Remove timestamps older than 60 seconds
            while timestamps and current_time - timestamps[0] > self.time_window:
                timestamps.popleft()

            if len(timestamps) >= self.message_limit:
                return HttpResponseForbidden("Rate limit exceeded: Max 5 messages per minute.")

            timestamps.append(current_time)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
