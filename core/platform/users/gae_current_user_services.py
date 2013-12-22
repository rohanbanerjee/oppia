# coding: utf-8
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Provides a seam for user-related services."""

__author__ = 'Sean Lip'


from google.appengine.api import users
from google.appengine.ext import ndb


def create_login_url(slug):
    """Creates a login url."""
    return users.create_login_url(slug)


def create_logout_url(slug):
    """Creates a logout url."""
    return users.create_logout_url(slug)


def is_current_user_admin(request):
    """Checks whether the current user is an admin."""
    return users.is_current_user_admin()


def get_current_user(request):
    """Returns the current user."""
    return users.get_current_user()


class FakeUser(ndb.Model):
    _use_memcache = False
    _use_cache = False
    user = ndb.UserProperty(required=True)


def get_user_id_from_email(email):
    """Given an email address, returns a user id.

    Returns None if the email address does not correspond to a valid user id.
    """
    u = users.User(email)
    key = FakeUser(user=u).put()
    obj = FakeUser.get_by_id(key.id())
    user_id = obj.user.user_id()
    if user_id:
        return unicode(user_id)
    else:
        return None
