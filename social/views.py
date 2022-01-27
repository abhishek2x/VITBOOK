from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .forms import CreatePollForm

# from social.forms import MyPostForm

from .models import *

from django.views.generic.detail import DetailView
from django.db.models import Q

from django.views.generic.edit import (UpdateView,
                                        CreateView,
                                        DeleteView )

from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from django.views.generic import View
from django.http import JsonResponse

# from django.core.mail import send_mail

                                            # Create your views here.


# ----------------------------------------------------------------------------------------------------------------------
                                    # NOTIFICATIONS
# -----------------------------------------------------------------------------------------------------------------------


ALL_NOTICES = []
ALL_CODE = []
ALL_FOLLOWERS = []


def notification(request):
    context = {'notices': ALL_NOTICES, 'code': ALL_CODE, 'follow': ALL_FOLLOWERS}
    return render(request, 'social/notification.html', context)


# ----------------------------------------------------------------------------------------------------------------------
                                    # Home View
# -----------------------------------------------------------------------------------------------------------------------


@method_decorator(login_required, name="dispatch")    
class HomeView(ListView):

    template_name = "social/home.html"
    paginate_by = 7
    # global is_paginated = true

    def get_queryset(self):
        followedList = FollowUser.objects.filter(followed_by=self.request.user.myprofile)

        followedList2 = []
        for e in followedList:
            followedList2.append(e.profile)
        postList = MyPost.objects.filter(uploaded_by__in=followedList2).order_by("-id")

        # This was here for search query

        # si = self.request.GET.get("si")
        # if si == None:
            # si = ""
        # postList = postList.filter(Q(subject__icontains=si) | Q(msg__icontains=si)| Q(uploaded_by__name__icontains = si)).order_by("-id")

        LikeNoList = []
        for p1 in postList:
            p1.liked = False
            ob = PostLike.objects.filter(post=p1, liked_by=self.request.user.myprofile)
            if ob:
                p1.liked = True

            obList = PostLike.objects.filter(post=p1)
            p1.likedno = obList.count()
            
            LikeNoList.append(p1.likedno)

            p1.likelist = []
            for e in obList:
                p1.likelist.append(e.liked_by)

        mypost_list = postList
        return mypost_list

# ----------------------------------------------------------------------------------------------------------------------
                                 # Profile
# -----------------------------------------------------------------------------------------------------------------------


def profiling(request, pk):
    profileData = MyProfile.objects.get(id=pk)
    photos = MyPost.objects.filter(uploaded_by_id=pk)

    totalPhotos = photos.count()

    followersList = FollowUser.objects.filter(profile__id=pk)
    followersList2 = []
    for e in followersList:
        followersList2.append(e.followed_by)

    noOfFollowers = followersList.count()


    followingList = FollowUser.objects.filter(followed_by__id=pk)
    followingList2 = []
    for e in followingList:
        followingList2.append(e.profile)

    noOfFollowing = followingList.count()
    context = {'myprofile': profileData, 'photos': photos, 'totalPhotos': totalPhotos,
               'following': followingList2, 'followers': followersList2 ,
               'noOfFollowing': noOfFollowing, 'noOfFollowers': noOfFollowers}

    return render(request, 'social/profile_datail2.html', context)

# ----------------------------------------------------------------------------------------------------------------------
                                         # Others
# -----------------------------------------------------------------------------------------------------------------------


class welcome(TemplateView):
    template_name = "social/welcome.html"


class AboutView(TemplateView):
    template_name = "social/about.html"


class PrivacyView(TemplateView):
    template_name = "social/privacy.html"


class SupportView(TemplateView):
    template_name = "social/support.html"


@login_required
def ub(request):
    blg = AddConfession.objects.all().order_by("-id")
    paginator = Paginator(blg, 3) 
    page = request.GET.get('page', 1)
    blg = paginator.get_page(page)
    paginate_by = 6

    try:
        blg = paginator.page(page)
    except PageNotAnInteger:
        blg = paginator.page(1)
    except EmptyPage:
        blg = paginator.page(paginator.num_pages)


    return render(request, "social/ub.html", {'blg' : blg })

@login_required
def Ubupload(request):
    if request.method == 'POST':
        by = request.POST['by']
        to = request.POST['to']
        confession = request.POST['confession']
        real = request.user.username

        if by != '' or to != '':
            instance = AddConfession.objects.create(
                real=real,
                by=by, 
                to=to, 
                confession=confession)

            instance.save()

            # send_mail(
            #     'Your Accouncement is Uploaded Successfully',
            #     'Your Accouncement is Uploaded Successfully at Accouncement Panel, You may check it if required',
            #     'vitbook.smtp.team@gmail.com',
            #     [request.user.email],
            #     fail_silently=False
            # )

            ALL_NOTICES.append(instance)
            messages.success(request, 'Your Announcement has been successfully Uploaded!')
            return redirect('ub')
        else:
            messages.success(request, 'Oops!..Your Announcement has not been Uploaded!')
            return redirect('ub')
    else:
        print("failed to upload")
        messages.success(request, 'Oops!..Your Announcement has not been Uploaded!')
        return render(request, 'social/ub.html')


def ContactView(request):
    return render(request, "social/contact.html")


def ContactViewUpload(request):
    if request.method == 'POST':
        by = request.POST['by']
        subject = request.POST['subject']
        branch = request.POST['branch']
        description = request.POST['description']
        real_sender = request.user.username
        
        instance = Contact.objects.create(real_sender=real_sender,
                                         by=by,
                                         branch=branch,
                                         subject=subject, 
                                         description=description)
        instance.save()
        # send_mail(
        #     'Your Form is Successfully Submitted',
        #     'Your Form is Uploaded Successfully, We may check it soon.',
        #     'vitbook.smtp.team@gmail.com',
        #     [request.user.email],
        #     fail_silently=False
        # )
        messages.success(request, 'Your form has been successfully submitted!')
        return redirect('contact')

    else:
        print("failed to upload")
        messages.success(request, 'Oops!..Your form has not been submitted!')
        return render(request, 'social/contact.html')


def JoinView(request):
    return render(request, "social/join.html")


def JoinViewUpload(request):
    if request.method == 'POST':
        skills = request.POST['skills']
        branch = request.POST['branch']
        suggestions = request.POST['suggestions']
        yname = request.POST['yname']
        real_sender = request.user.username
        
        instance = Developer.objects.create(real_sender=real_sender,
                                         yname=yname,
                                         skills=skills,
                                         branch=branch, 
                                         suggestion=suggestions)
        instance.save()
        # send_mail(
        #     'Your Form is Successfully Submitted',
        #     'Your Form is Uploaded Successfully, We may check it soon.',
        #     'vitbook.smtp.team@gmail.com',
        #     [request.user.email],
        #     fail_silently=False
        # )
        messages.success(request, 'Your form has been successfully submitted!')
        return redirect('developer')

    else:
        print("failed to upload")
        messages.success(request, 'Oops!..Your form has not been submitted!')
        return render(request, 'social/join.html')


# ----------------------------------------------------------------------------------------------------------------------
                                            # MyProfile
# -----------------------------------------------------------------------------------------------------------------------


# @method_decorator(login_required, name="dispatch")
# class MyProfileDetailView(DetailView):
#     model = MyProfile


@method_decorator(login_required, name="dispatch")
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ["name", "age", "gender", "city", "college", "registration_no", "status",
              "phone_no", "description", "tagline", "pic", "linkedin_profile",
              "facebook_profile", "insta_profile", "github_profile", "portfolio"]
    # messages.success(request, 'Your Profile has been successfully Updated!')


@method_decorator(login_required, name="dispatch")
class MyProfileListView(ListView):
    model = MyProfile
    paginate_by = 8
    def get_queryset(self):
        si = self.request.GET.get("si")

        if si == None:
            si = ""

        profList = MyProfile.objects.filter(Q(name__icontains=si) | Q(gender__icontains=si) | Q(status__icontains=si)).order_by("name")

        for p1 in profList:
            p1.followed = False
            ob = FollowUser.objects.filter(profile=p1, followed_by=self.request.user.myprofile)
            if ob:
                p1.followed = True
            obList = FollowUser.objects.filter(profile = p1)
            p1.followers = obList.count()

            followingList = FollowUser.objects.filter(followed_by=p1)
            p1.following = followingList.count()

        return profList

# ---------------------------------------------------------------------------------------------------------------------
                                             # MyPost
# -----------------------------------------------------------------------------------------------------------------------

# PROFILE
# Presenting the profile and adding search option


@method_decorator(login_required, name="dispatch")
class MyPostListView(ListView):
    model = MyPost
    paginate_by = 12

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MyPost.objects.filter(Q(uploaded_by__name__icontains = si)).order_by("-id")
 

# To upload a new post
@method_decorator(login_required, name="dispatch")    
class MyPostCreate(CreateView):
    model = MyPost
    fields = ["subject", "msg", "pic"]

    def form_valid(self, form):

        self.object = form.save()
        self.object.uploaded_by = self.request.user.myprofile
        self.object.save()
        # send_mail(
        #     'Your Post is Successfully Uploaded',
        #     'Your Post has been Uploaded Successfully, You may check it by following the Link.',
        #     'vitbook.smtp.team@gmail.com',
        #     [MyPost.uploaded_by.user.email],
        #     fail_silently=False
        # )
        # messages.success(self, 'Your post has been successfully uploaded!')
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")
class MyPostDetailView(DetailView):
    model = MyPost


@method_decorator(login_required, name="dispatch")
class MyPostDeleteView(DeleteView):
    model = MyPost


# ----------------------------------------------------------------------------------------------------------------------
                                         # VITHUB
# -----------------------------------------------------------------------------------------------------------------------


@method_decorator(login_required, name="dispatch")
class VithubListView(ListView):
    model = Vithub
    paginate_by = 8

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Vithub.objects.filter(Q(title__icontains = si) | Q(title__icontains = si)).order_by("-id")


@method_decorator(login_required, name="dispatch")
class VithubCreate(CreateView):
    model = Vithub
    fields = ["title", "code", "language", "domain","description"]

    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.myprofile
        self.object.save()
        # send_mail(
        #     'Your Project snippet is Successfully Uploaded',
        #     'Your Project snippet has been Uploaded Successfully, You may check it by following the Link.',
        #     'vitbook.smtp.team@gmail.com',
        #     [Vithub.uploaded_by.user.email],
        #     fail_silently=False
        # )
        ALL_CODE.append(self.object)
        # messages.success(request, 'Your code has been successfully uploaded!')
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")
class VithubDetailView(DetailView):
    model = Vithub


@method_decorator(login_required, name="dispatch")    
class VithubDeleteView(DeleteView):
    model = Vithub


# ----------------------------------------------------------------------------------------------------------------------
                                            #CHAT
# -----------------------------------------------------------------------------------------------------------------------


@method_decorator(login_required, name="dispatch") 
class ChatView(ListView):
    model = Chat
    template_name = '/static/chat_list.html'
    context_object_name = 'msgs'


class CreateChatUser(View):

    def get(self, request):
        sender1 = request.user.username
        message1 = request.GET.get('message', None)

        obj = Chat.objects.create(
            sender=sender1,
            message=message1,
        )

        user = {
                'id':obj.id,
                'sender':obj.sender,
                'message':obj.message,
                'cr_date': obj.cr_date,
                }

        data = {
            'user': user
        }
        return JsonResponse(data)


# ----------------------------------------------------------------------------------------------------------------------
                                        # LIKE/FOLLOW/ATTENDENCE/GRADES
# -----------------------------------------------------------------------------------------------------------------------


def like(request, pk, page, *args, **kargs):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.create(post=post, liked_by = request.user.myprofile)
    return redirect('/home/' + "?page=" + page + '#' + str(pk))


def unlike(req, pk, page, *args, **kargs):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.filter(post=post, liked_by = req.user.myprofile).delete()
    return redirect('/home/' + "?page=" + page + '#' + str(pk))


def follow(req, pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user, followed_by=req.user.myprofile)


    ALL_FOLLOWERS.append(user)
    # noti.follower = req.user.myprofile
    # noti.followed = user

    return HttpResponseRedirect(redirect_to="/profile")


def unfollow(req, pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user, followed_by=req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to="/profile")


@login_required
def attendance(request):
    context = {}
    return render(request, 'social/attendance.html', context)


@login_required
def grades(request):
    context = {}
    return render(request, 'social/grades.html', context)


# ----------------------------------------------------------------------------------------------------------------------
                                        # POLL
# -----------------------------------------------------------------------------------------------------------------------


@login_required
def poll_home(request):
    polls = Poll.objects.all().order_by("-id")
    context = {
        'polls': polls
    }
    return render(request, 'social/poll.html', context)


@login_required
def poll_create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            # send_mail(
            #     'Your Poll is Successfully Created',
            #     'Your Poll has been Created Successfully, You may check it by following the Link.',
            #     'vitbook.smtp.team@gmail.com',
            #     [request.user.email],
            #     fail_silently=False
            # )
            return redirect('poll_home')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'social/poll_create.html', context)

@login_required
def poll_vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        else:
            return HttpResponse(400, 'Invalid form')


        poll.save()

        pollId = Poll.objects.get(pk=poll_id)
        PollVoted.objects.create(voted_on=pollId, voted_by=request.user.myprofile)

        return redirect('poll_results', poll.id)

    voted = PollVoted.objects.filter(voted_by=request.user.id, voted_on=poll_id)
    has_voted = False
    if voted:
        has_voted = True
    else:
        has_voted = False

    context = {
        'poll': poll,
        'has_voted': has_voted
    }
    return render(request, 'social/poll_vote.html', context)


@login_required
def poll_results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'social/poll_results.html', context)

