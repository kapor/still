# aaa/middleware.py



class ReferralMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_paths = ['/login/', '/signup/', '/logout/']  #
        if request.path not in excluded_paths and 'referral_url' not in request.session and request.META.get('HTTP_REFERER') and not request.user.is_authenticated:
            request.session['referral_url'] = request.META['HTTP_REFERER']
        response = self.get_response(request)
        return response