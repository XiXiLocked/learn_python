#!/usr/bin/env python 
# -*- coding: utf-8 -*
import urllib2, time
from xml.etree import ElementTree
from collections import defaultdict

def get_all_rss_dates(url_address):
    month_count = defaultdict(int)

    try:    
        #Open the file via HTTP.
        response = urllib2.urlopen(url_address)
        tree = ElementTree.parse(response)
        root = tree.getroot()

        #List of post dates.
        news_post_date = root.findall("channel//pubDate")
        '''Iterate in all our searched elements and print the inner text for each.'''    
        for date in news_post_date:
            month_count[date.text[8:11]]+=1
            #datestr_array = date.text.replace(",","").split(" ")
            #formatted_date = "{0} {1}, {2}, {3}".format(
            #    datestr_array[2], datestr_array[1], datestr_array[3],
            #    datestr_array[4])
            #blog_datetime = time.strptime(formatted_date, "%b %d, %Y, %H:%M:%S")
            #month_count.append(blog_datetime.tm_mon)

        #Finally, close our open network.
        response.close()
    except Exception as e:    
        #If we have an issue show a message and alert the user.
        #print(e)
        throw

    return list(month_count.items())

if __name__ == '__main__':
    print (get_all_rss_dates('http://www.packtpub.com/rss.xml'))
