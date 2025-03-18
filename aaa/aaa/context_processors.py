# aaa/context_processors.py




def referral_url(request):
	return {'referral_url': request.session.get('referral_url', None)}