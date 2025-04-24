from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.models import Post
from chirps.models import Post as Chirp
from blog.models import Blog
from shelf.models import Shelves
from groups.models import Group, Comment

from itertools import chain, groupby
from datetime import datetime
from operator import attrgetter
from django.utils import timezone
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import F

from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.



def profile_view(request, username):
	obj = Profile.objects.get(user=request.user)
	user = get_object_or_404(User, username=username)
	form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
	info = get_object_or_404(Profile, user=user)

	post = Post.objects.filter(user=user).order_by('created_at')
	chirp = Chirp.objects.filter(user=user).order_by('created_at')
	comment = Comment.objects.filter(user=user).order_by('created_at')
	shelf = Shelves.objects.filter(user=user).order_by('created_at')
	blog = Blog.objects.filter(user=user).filter(published_date__lte=timezone.now()).order_by('-published_date')

	activity_list = list(chain(post, chirp, comment, shelf, blog))

	sorted_objects = sorted(
		activity_list,
		key=lambda obj: obj.created_at if hasattr(obj, 'created_at') else datetime(1970, 1, 1),
		reverse=True
	)


	paginator = Paginator(sorted_objects, 80) 
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	if request.accepts('application/json'):
		if form.is_valid():
			instance.save()
			messages.success(request, 'Profile Updated')
			return JsonResponse({
				'user': instance.user.username,
				'picture': instance.picture,
				'bio': instance.bio,
			})




	context = {'obj': obj, 'form': form, 'user': user, 'page_obj': page_obj, 'info': info}

	return render(request, 'profiles/profiles.html', context)





