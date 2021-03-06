#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf import settings

from opps.contrib.feeds.views import ContainerFeed, ChannelFeed
from opps.core.tags.views import TagList
from opps.core.cache import cache_page

from .views import ContainerList, ContainerDetail
from .views import ContainerAPIList, ContainerAPIDetail
from .views import Search


urlpatterns = patterns(
    '',
    url(r'^$', ContainerList.as_view(), name='home'),

    url(r'^(rss|feed)$', cache_page(settings.OPPS_CACHE_EXPIRE)(
        ContainerFeed()), name='feed'),

    url(r'^search/', Search(), name='search'),

    url(r'^tag/(?P<tag>[\w//-]+)$',
        cache_page(settings.OPPS_CACHE_EXPIRE)(
            TagList.as_view()), name='tag_open'),

    url(r'^(?P<long_slug>[\w\b//-]+)/(rss|feed)$',
        cache_page(settings.OPPS_CACHE_EXPIRE)(
            ChannelFeed()), name='channel_feed'),

    url(r'^(?P<channel__long_slug>[\w//-]+)/(?P<slug>[\w-]+).api$',
        cache_page(settings.OPPS_CACHE_EXPIRE_DETAIL)(
            ContainerAPIDetail.as_view()), name='open-api'),
    url(r'^(?P<channel__long_slug>[\w//-]+)/(?P<slug>[\w-]+)\.html$',
        cache_page(settings.OPPS_CACHE_EXPIRE_DETAIL)(
            ContainerDetail.as_view()), name='open'),

    url(r'^(?P<channel__long_slug>[\w\b//-]+).api$',
        cache_page(settings.OPPS_CACHE_EXPIRE_LIST)(
            ContainerAPIList.as_view()), name='channel-api'),
    url(r'^(?P<channel__long_slug>[\w\b//-]+)/$',
        cache_page(settings.OPPS_CACHE_EXPIRE_LIST)(
            ContainerList.as_view()), name='channel'),
)
