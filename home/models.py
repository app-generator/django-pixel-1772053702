# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    fav_movie = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Movie(models.Model):

    #__Movie_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    #__Movie_FIELDS__END

    class Meta:
        verbose_name        = _("Movie")
        verbose_name_plural = _("Movie")


class Review(models.Model):

    #__Review_FIELDS__
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    #__Review_FIELDS__END

    class Meta:
        verbose_name        = _("Review")
        verbose_name_plural = _("Review")


class Comment(models.Model):

    #__Comment_FIELDS__
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    #__Comment_FIELDS__END

    class Meta:
        verbose_name        = _("Comment")
        verbose_name_plural = _("Comment")



#__MODELS__END
