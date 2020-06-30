from django.contrib import admin

from social.models import *

from django.contrib.admin.options import ModelAdmin

admin.site.site_header = 'Vitbook Administration'                     # default: "Django Administration"
admin.site.index_title = 'Vitbook Database Structure'                 # default: "Site administration"
admin.site.site_title = 'Vitbook Site Admin'                          # default: "Django site admin"


class FollowUserAdmin(ModelAdmin):
    list_display = ["profile", "followed_by"]
    search_fields = ["profile", "followed_by"]
    list_filter = ["profile", "followed_by"]


admin.site.register(FollowUser, FollowUserAdmin)


class MyPostAdmin(ModelAdmin):
    list_display = ["subject", "cr_date", "uploaded_by"]
    search_fields = ["subject", "msg", "uploaded_by"]
    list_filter = ["cr_date", "uploaded_by"]


admin.site.register(MyPost, MyPostAdmin)


class MyProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "status", "phone_no"]
    list_filter = ["status", "gender"]


admin.site.register(MyProfile, MyProfileAdmin)


class PollAdmin(ModelAdmin):
    list_display = ["question"]
    search_fields = ["question"]
    list_filter = ["question"]


admin.site.register(Poll, PollAdmin)


class PostLikeAdmin(ModelAdmin):
    list_display = ["post", "liked_by"]
    search_fields = ["post", "liked_by"]
    list_filter = ["cr_date"]


admin.site.register(PostLike, PostLikeAdmin)


class AddConfessionAdmin(ModelAdmin):
    list_display = ["by", "to"]
    search_fields = ["by", "to"]
    list_filter = ["by", "to"]


admin.site.register(AddConfession, AddConfessionAdmin)


class VithubAdmin(ModelAdmin):
    list_display = ["title", "uploaded_by"]
    search_fields = ["language", "domain", "title", "uploaded_by"]
    list_filter = ["title", "uploaded_by"]


admin.site.register(Vithub, VithubAdmin)


class ContactAdmin(ModelAdmin):
    list_display = ["description", "subject"]
    search_fields = ["name", "description"]
    list_filter = ["subject", "description"]


admin.site.register(Contact, ContactAdmin)


class ChatAdmin(ModelAdmin):
    list_display = ["sender"]
    search_fields = ["sender"]
    list_filter = ["sender"]


admin.site.register(Chat, ChatAdmin)


class DeveloperAdmin(ModelAdmin):
    list_display = ["yname", "skills", "real_sender"]
    search_fields = ["branch", "skills", "real_sender"]
    list_filter = ["branch", "skills", "real_sender"]


admin.site.register(Developer, DeveloperAdmin)