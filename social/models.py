from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator

# Create your models here.


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    email = models.EmailField(max_length=254, blank=False, null=False)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    gender = models.CharField(max_length=20, default="female", choices=(("male", "male"), ("female", "female")
                                                                        , ("other", "other")))
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=11, null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(("single", "single"), ("commited", "commited")
                                                                        , ("complicated", "complicated")))
    registration_no = models.CharField(max_length=12, null=True, blank=True)
    tagline = models.CharField(max_length=200, default="Hit me on Vitbook!")
    city = models.CharField(max_length=100, default="Vitland")
    college = models.CharField(max_length=100, choices=(("VIT Vellore", "VIT Vellore"), ("VIT Chennai", "VIT Chennai"),
                              ("VIT Bhopal", "VIT Bhopal"), ("VIT Amaravati",  "VIT Amaravati")),  default="VIT Bhopal")
    description = models.TextField(null=True, blank=True, default="Hi!, this is my default description.")
    # cov_pic = models.ImageField(null=True, blank=True, default='default_cover.jpeg')

    insta_profile = models.URLField(max_length=200, null=True, blank=True)
    facebook_profile = models.URLField(max_length=200, null=True, blank=True)
    linkedin_profile = models.URLField(max_length=200, null=True, blank=True)
    github_profile = models.URLField(max_length=200, null=True, blank=True)
    portfolio = models.URLField(max_length=200, null=True, blank=True)

    pic = models.ImageField(null=True, blank=True, default='default_profile.png')

    def __str__(self):
        return "%s" % self.user


class MyPost(models.Model):
    pic = models.ImageField(null=True, blank=True)
    subject = models.CharField(max_length = 200)# captions
    msg = models.TextField(null=True, blank=True)# desc
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)# Id of MyProfile

    def __str__(self):
        return "%s" % self.subject


class PostLike(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)# Id of MyPost
    liked_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)# Id of MyProfile
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.liked_by


class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="profile")# Id of MyProfile
    followed_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="followed_by")# Id of MyProfile

    def __str__(self):
        return "%s" % self.followed_by


class AddConfession(models.Model):
    by = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    confession = models.TextField(default="")
    real = models.CharField(max_length=200)
    confessioner = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)# Id of MyProfile

    def __str__(self):
        return "%s" % self.to


class Vithub(models.Model):
    title = models.CharField(max_length = 100)
    code = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)# Id of MyProfile
    language = models.CharField(max_length=50, default="Not provided", choices=(("C","C"), ("C++","C++"), ("Python","Python"), ("Javascript","Javascript"), ("HTML/CSS","HTML/CSS"), ("Java","Java"), ("Golang","Golang"), ("Ruby","Ruby"), ("Kotlin","Kotlin"), ("Solidity","Solidity"), ("Other","Other")))
    domain = models.CharField(max_length = 100, default="Not Provided", choices=(("Competitive Coding","Competitive Coding"), ("Web Development","Web Development"), ("App Development","App Development"), ("Blockchain", "Blockchain"), ("Scripting", "Scripting"), ("DSA", "DSA"), ("Others", "Others")))

    def __str__(self):
        return "%s" % self.title


class Contact(models.Model):
    by = models.CharField(max_length=70)
    branch = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    real_sender = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.by


class Chat(models.Model):
    message = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.sender


class Developer(models.Model):
    yname = models.CharField(max_length=70)
    branch = models.CharField(max_length=50)
    skills = models.TextField()
    suggestion = models.TextField()
    real_sender = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.real_sender


class Poll(models.Model):
    created_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, default=1)
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count

    def __str__(self):
        return "%s" % self.id


class PollVoted(models.Model):
    voted_on = models.ForeignKey(to=Poll, on_delete=CASCADE, related_name="voted_on")
    voted_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="voted_by")

    def __str__(self):
        return "%s" % self.voted_by
