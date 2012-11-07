from dateutil.parser import parse
from mongomodel.crawl.twitter.models import *
import pymongo


''' pre-cond : db must be init'''
def mk_user_obj(user):
    exists = User.objects.filter(uid = user.id)
    if exists:
        print "user exists"
        u = exists[0]
        return u
    else:
        u = User(uid = user.id, name = user.name)
        u.favourites_count = user.favourites_count
        u.favorites_count = user.friends_count
        if hasattr(user, 'following'):
            u.following = user.following
        u.followers_count = user.followers_count
        u.profile_image_url = user.profile_image_url
        u.contributors_enabled = user.contributors_enabled
        u.geo_enabled = user.geo_enabled
        u.created_at = parse(user.created_at)
        u.description = user.description
        u.listed_count = user.listed_count
        if hasattr(user, 'follow_request_sent'):                
            u.follow_request_sent = user.follow_request_sent
        u.time_zone = user.time_zone
        u.url = user.url
        u.verified = user.verified
        if hasattr(user, 'default_profile'):                
            u.default_profile = user.default_profile
        if hasattr(user, 'show_all_inline_media'):
            u.show_all_inline_media = user.show_all_inline_media
        if hasattr(user, 'is_translator'):
            u.is_translator = user.is_translator
        u.notifications = user.notifications
        u.protected = user.protected
        u.location = user.location
        u.statuses_count = user.statuses_count
        if hasattr(user, 'default_profile_image'):
            u.default_profile_image = user.default_profile_image
        u.lang = user.lang
        u.utc_offset = user.utc_offset
        u.screen_name = user.screen_name
        u.save()
        return u


def read_usernames_from_file(file):
    user_file = open(file,'r')
    users=[]
    for ln in user_file:
        users = users + ln.strip('\r\n').split(',')
    return users


def add_users_by_name(api,user_names):
    users = []
    for user_name in user_names:
        try:
            user = api.GetUser(user_name)
            u = mk_user_obj(user)
            users.append(u)
        except TwitterError, e:
            pass
    return users
