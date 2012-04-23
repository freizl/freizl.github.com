#!/usr/bin/python

import urllib, urllib2, cookielib, json, httplib
import re
import time
import getpass
from xml.etree.ElementTree import ElementTree, fromstring

""" TODO
1. logger instead of print
3. use print() function / parameter instead of str concat
4. multiple user login
5. much better to only steal avaiable
"""

class Kaixin(object):
    def __init__(self, username, passwd):
        self.email = username
        self.password = passwd
        self.share_farm = ('6','7','10','12','15')
        #open('kaixin.coockie','wb').write('')
        self.cj = cookielib.LWPCookieJar()  
        try:  
           self.cj.revert('kaixin.coockie')  
        except:  
            None  
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))  
        urllib2.install_opener(self.opener)  

    def signin(self):
        r = self.opener.open('http://www.kaixin001.com/home/')
        if r.geturl() == 'http://www.kaixin001.com/home/':
            print 'user: ' + self.email + ' already login'
            return True
        if r.geturl() == 'http://www.kaixin001.com/?flag=1&url=%2Fhome%2F':  
            print 'Need logging on! with account: ' + self.email
            params = {'email':self.email, 'password':self.password, 'remember':1}  
            req = urllib2.Request(  
                'http://www.kaixin001.com/login/login.php',
                urllib.urlencode(params)  
            )
            r = self.opener.open(req)  
            home_page_len = 30
            if r.geturl()[:30] == 'http://www.kaixin001.com/home/':  
                print 'Logged on successfully!'  
                self.cj.save('kaixin.coockie')
                return True
            else:
                print 'failed to login.. try debug the reason'
                return False

    def monitor(self):
        if self.signin() == False:
            return
  
        self._set_verify_code()

        is_monitoring = 1
        while is_monitoring > 0:
            print time.strftime('%y/%m/%d %H:%M:%S')  
            req = urllib2.Request(  
                'http://www.kaixin001.com/house/garden/getfriendmature.php',  
                urllib.urlencode({'_':'','verify':self.verify})
                )  
            
            r = self.opener.open(req)  
            self.data = json.loads(r.read())  

            if len(self.data['friend']) == 0:
                print 'No stolable friends found'
                return

            self._do_steal()
            is_monitoring = is_monitoring - 1
        time.sleep(2)
    
    def _set_verify_code(self):
        r = self.opener.open('http://www.kaixin001.com/app/app.php?aid=1062&url=garden/index.php')  
        m = re.search('var g_verify = "(.+)";', r.read())  
        self.verify = m.group(1)

    def _do_steal(self):
        test_uid = self.data['friend']
        for item in test_uid:
            for farm_id in self._get_available_farms(item['uid']):
                try:
                    print item['realname'], farm_id
                    r = self.opener.open('http://www.kaixin001.com/!house/!garden/havest.php?farmnum=' + farm_id + '&fuid=' + str(item['uid']))
                    print r.read()
                except httplib.BadStatusLine:
                    print ">>>error.. when steal"
                    print '>>>name:', item['realname'], 'index:', farm_id, '>>>', r.read()
            time.sleep(3)

    def _get_friend_farm_config(self, uid):
        r = self.opener.open('http://www.kaixin001.com/!house/!garden//getconf.php?verify=' + self.verify + '&fuid=' + str(uid))
        return r.read()

    def _get_available_farms(self, uid):
        try:
            doc = fromstring(self._get_friend_farm_config(uid))
        except:
            print "parse config error of friend:", uid
            return []

        result = []
        for e in doc.getiterator('item')[0:15]:
            if len(e.getiterator("crops")) == 1:
                if re.search('font.*font', e.getiterator("crops")[0].text) is None:
                    result.append(e.getiterator("farmnum")[0].text)
        tmp = [item for item in result if item not in self.share_farm]
        return tmp


if __name__ == '__main__':
    username = 'freizl@gmail.com'
    password = getpass.getpass("user " + username + ":" )
    k = Kaixin(username, password)
    k.monitor()
#    print list_intersection([1,2,3,4],[2,3])
#    print k._get_available_farms('12033834')
