#!/usr/bin/env python
# -*- coding: utf-8 -*
import LoadRssFeed
import chart_build
#Call our 'LoadRssFeed' function.
data = LoadRssFeed.get_all_rss_dates('http://www.packtpub.com/rss.xml')
chart_build.generate_chart(data)
