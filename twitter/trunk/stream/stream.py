import pycurl, json, urllib2, sys, sets
from dateutil.parser import parse
from mongomodel.crawl.twitter.models import *
import pymongo

#STREAM_URL = "https://stream.twitter.com/1/statuses/filter.json?locations=103.594154,1.199738,104.017814,1.471575"
STREAM_URL = "https://stream.twitter.com/1/statuses/filter.json?follow="
#STREAM_URL= "https://stream.twitter.com/1/statuses/sample.json"
URL = "https://api.twitter.com/1/users/lookup.json?include_entities=true&screen_name="

USER = "nypkenny"
PASS = "abc123$%^"

#user_names = ["3pommesvertes","acefacesays","ang_moh","Angelnang","angiefeimao","animus128","ArtiztikVizion","AshleyBenlove","ashleykristen","badhex","bobfromhuddle","boris_gorelik","brandontarzis","brett227","brettgreene","bry_wong","Cherry_Chan","chris_reed","CjBayesian","clareholmes","crystaljeanwest","deadash08","debbchia","Delphine_mz","DoctorZen","Drastician","dubikan","dyanysus1116","Elyw","ericasheff","fellofff","finiteattention","huiwens","inspiredchris","irfanali1","itstracyp","jaber70","Jenx0","jijoei12","jillelswick","KathieKatKate","kellywashere","KohCheeSiang","koolbenny","le_Hutin","Livsforfashion","Lizzzielou","LornaQuandt","M_town_dan","markpolinsky","mathewy","Mbenti","mclangan","meggan","merry30","mick_bailey","miken_bu","moichita","moonbunnychan","moralcompas","MsMayaLynn","muchworsegames","muteddragon","naomicher","newnukem","ozzi2011","pablochacin","PatVitsky","pixiebeanz","pixiedub","raisinglight","rekinder","RORO_STYLE","rrifae","rubberbandgirl2","saraannk","scalawag","Schmalll","sha_nichole","socialneuro","SoozyJ","Stuarte","suefolley","sunshinyday","swanny","sylvereapleanan","tangrae","tarandip","tlamarca","tompollak","trisected","tweetyourtummy","twirlsandswirls","vishakamantri","webprotech","yoyoyokatty"]


MAX_TERM_ALLOWED = 75

def split_list_by(l,n):
    rounds = len(l) / n
    result = []
    for i in range(0,rounds+1):
        if i*n < len(l):
            result.append(l[i*n:(i+1)*n])
    return result

def get_userids(usernames):
    batches = split_list_by(usernames, MAX_TERM_ALLOWED)
    userids = []
    for batch in batches:
        url = URL+','.join(batch)
        print url
        f = urllib2.urlopen(url)
        j = json.loads(f.read())
        userids = userids + map(lambda x:x['id'] ,j)
        found = sets.Set(map(lambda x:x['screen_name'].lower(), j))
        print "missing" + str(sets.Set(map(lambda x:x.lower(), usernames)) - found)
        f.close()
    print userids
    return userids

def get_userids_file(infile):
    inh = open(infile,'r')
    unames = []
    for ln in inh:
        s = ln.strip('\r\n"')
        unames.append(s)
    inh.close()
    uids = get_userids(unames)
    return uids

# user_ids = get_userids(user_names)



# user_ids = [112724745, 66958905, 85558811, 21880585, 82026749, 22798391, 18755371, 29181568, 1101741, 140475840, 17023494, 50838486, 32399360, 120392432, 16070608, 14519349, 15651494, 158696981, 183267802, 6974162, 156542043, 28254549, 26906684, 14510781, 259935923, 19460093, 7451022, 45339620, 80816333, 19686020, 133022087, 114845306, 191543365, 74078447, 16570722, 28056319, 22926660, 184095411, 44798253, 26437097, 53728344, 110593918, 231927744, 170677411, 128098218, 33845682, 48057990, 137902468, 17513474, 7582832, 16478966, 16567643, 264229360, 42363561, 172608608, 5547022, 207948843, 1095511, 49595173, 14137027, 70116209, 16486812, 17546014, 443902440, 72631850, 223527835, 17458866, 15423556, 16818221, 76963615, 248212400, 6166042, 42180543, 311845225, 79129072, 21424233, 54575173, 54946864, 17260140, 118083728, 25754814, 15045218, 20529038, 43837335, 8893282, 73100625, 37222477, 112231906, 280035308, 12970412, 18695966, 248171477, 107512786, 66904150] 


def insert_to_mongo(data):
    db = init()
    try:
        data_json = json.loads(data)
        if data_json.has_key("user"):
            user = data_json["user"]
            u = None
            if user.has_key("id") and user.has_key("name"):
                exists =  User.objects.filter(uid = user["id"])
                if exists:
                    u = exists[0]
                    print "user exists"
                else:
                    u = User(uid = user["id"], name = user["name"])
                if user.has_key("favourites_count"):
                    u.favourites_count = user["favourites_count"]
                if user.has_key("friends_count"):
                    u.favorites_count = user["friends_count"]
                if user.has_key("following"):
                    u.following = user["following"]
                if user.has_key("followers_count"):
                    u.followers_count = user["followers_count"]
                if user.has_key("profile_image_url"):
                    u.profile_image_url = user["profile_image_url"]
                if user.has_key("contributors_enabled"):
                    u.contributors_enabled = user["contributors_enabled"]
                if user.has_key("geo_enabled"):
                    u.geo_enabled = user["geo_enabled"]
                if user.has_key("created_at"):
                    u.created_at = parse(user["created_at"])
                if user.has_key("description"):
                    u.description = user["description"]
                if user.has_key("listed_count"):
                    u.listed_count = user["listed_count"]
                if user.has_key("follow_request_sent"):
                    u.follow_request_sent = user["follow_request_sent"]
                if user.has_key("time_zone"):
                    u.time_zone = user["time_zone"]
                if user.has_key("url"):
                    u.url = user["url"]
                if user.has_key("verified"):
                    u.verified = user["verified"]
                if user.has_key("default_profile"):
                    u.default_profile = user["default_profile"]
                if user.has_key("show_all_inline_media"):
                    u.show_all_inline_media = user["show_all_inline_media"]
                if user.has_key("is_translator"):
                    u.is_translator = user["is_translator"]
                if user.has_key("notifications"):
                    u.notifications = user["notifications"]
                if user.has_key("protected"):
                    u.protected = user["protected"]
                if user.has_key("location"):
                    u.location = user["location"]
                if user.has_key("statuses_count"):
                    u.statuses_count = user["statuses_count"]
                if user.has_key("default_profile_image"):
                    u.default_profile_image = user["default_profile_image"]
                if user.has_key("lang"):
                    u.lang = user["lang"]
                if user.has_key("utc_offset"):
                    u.utc_offset = user["utc_offset"]
                if user.has_key("screen_name"):
                    u.screen_name = user["screen_name"]
                u.save()
            else:
                pass

            if data_json.has_key("id") and u:
                exists = Tweet.objects.filter( tid = data_json["id"])
                if exists:
                    print "tweet exists"
                    pass
                else:
                    t = Tweet(tid = data_json["id"])
                    t.user = u
                    if data_json.has_key("contributors"):
                        t.contributors = data_json["contributors"]
                    if data_json.has_key("place"):
                        t.place = data_json["place"]
                    if data_json.has_key("in_reply_to_screen_name"):
                        t.in_reply_to_screen_name = data_json["in_reply_to_screen_name"]
                    if data_json.has_key("text"):
                        t.text = data_json["text"]
                    if data_json.has_key("favorited"):
                        t.favorited = data_json["favorited"]
                    if data_json.has_key("coordinates"):
                        t.coordinates = data_json["coordinates"]
                    if data_json.has_key("geo"):
                        t.geo = data_json["geo"]
                    if data_json.has_key("retweet_count"):
                        t.retweet_count = data_json["retweet_count"]
                    if data_json.has_key("created_at"):
                        t.created_at = parse(data_json["created_at"])
                    if data_json.has_key("source"):
                        t.source = data_json["source"]
                    if data_json.has_key("in_reply_to_user_id"):
                        t.in_reply_to_user_id = data_json["in_reply_to_user_id"]
                    if data_json.has_key("in_reply_to_status_id"):
                        t.in_reply_to_status_id = data_json["in_reply_to_status_id"]
                    if data_json.has_key("retweeted"):
                        t.retweeted = data_json["retweeted"]
                    if data_json.has_key("truncated"):
                        t.truncated = data_json["truncated"]
                    if data_json.has_key("entities"):
                        t.entities = data_json["entities"]
                    t.save()
            else:
                pass
    except ValueError,e:
        print "Value Error"


    if pymongo.version == '2.0.1':
        db.connection.disconnect()
    else:
        db.disconnect()

        


def on_receive(data):
    #data_json = json.loads(data)
    print data    
    insert_to_mongo(data)

if len(sys.argv) < 1:
    print "Usage: stream.py <user_id file>"
    sys.exit(1)

user_ids = get_userids_file(sys.argv[1])

conn = pycurl.Curl()
conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
conn.setopt(pycurl.URL, STREAM_URL+','.join(map(str,user_ids)))
conn.setopt(pycurl.WRITEFUNCTION, on_receive)
conn.perform()

s1 = '{"in_reply_to_status_id_str":null,"contributors":null,"place":null,"in_reply_to_screen_name":null,"text":"Test","favorited":false,"in_reply_to_user_id_str":null,"coordinates":null,"geo":null,"retweet_count":0,"created_at":"Fri Jul 13 09:38:00 +0000 2012","source":"web","in_reply_to_user_id":null,"in_reply_to_status_id":null,"retweeted":false,"id_str":"223712876576260096","truncated":false,"user":{"favourites_count":10,"friends_count":42,"profile_background_color":"C6E2EE","following":null,"profile_background_tile":false,"profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme2\/bg.gif","followers_count":38,"profile_image_url":"http:\/\/a0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","contributors_enabled":false,"geo_enabled":false,"created_at":"Tue Sep 23 03:08:29 +0000 2008","profile_sidebar_fill_color":"DAECF4","description":"Circos.com, Computer Science, Phd, National University of Singapore","listed_count":1,"follow_request_sent":null,"time_zone":"Singapore","url":"http:\/\/sites.google.com\/site\/luzhuomi\/","verified":false,"profile_sidebar_border_color":"C6E2EE","default_profile":false,"show_all_inline_media":false,"is_translator":false,"notifications":null,"profile_use_background_image":true,"protected":false,"profile_image_url_https":"https:\/\/si0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","location":"Singapore","id_str":"16414559","profile_text_color":"663B12","name":"Kenny","statuses_count":199,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme2\/bg.gif","id":16414559,"default_profile_image":false,"lang":"en","utc_offset":28800,"profile_link_color":"1F98C7","screen_name":"luzm"},"id":223712876576260096,"entities":{"user_mentions":[],"urls":[],"hashtags":[]}}'

s2 = '{"in_reply_to_status_id_str":null,"contributors":null,"place":null,"in_reply_to_screen_name":"luzm","text":"@luzm http:\/\/t.co\/0yzHGZnT #test abc","favorited":false,"in_reply_to_user_id_str":"16414559","coordinates":null,"geo":null,"retweet_count":0,"created_at":"Fri Jul 13 16:03:07 +0000 2012","source":"web","in_reply_to_user_id":16414559,"in_reply_to_status_id":null,"possibly_sensitive_editable":true,"retweeted":false,"id_str":"223809793016598528","truncated":false,"possibly_sensitive":false,"user":{"favourites_count":10,"friends_count":42,"profile_background_color":"C6E2EE","following":null,"profile_background_tile":false,"profile_background_image_url_https":"https:\/\/si0.twimg.com\/images\/themes\/theme2\/bg.gif","followers_count":38,"profile_image_url":"http:\/\/a0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","contributors_enabled":false,"geo_enabled":false,"created_at":"Tue Sep 23 03:08:29 +0000 2008","profile_sidebar_fill_color":"DAECF4","description":"Circos.com, Computer Science, Phd, National University of Singapore","listed_count":1,"follow_request_sent":null,"time_zone":"Singapore","url":"http:\/\/sites.google.com\/site\/luzhuomi\/","verified":false,"profile_sidebar_border_color":"C6E2EE","default_profile":false,"show_all_inline_media":false,"is_translator":false,"notifications":null,"profile_use_background_image":true,"protected":false,"profile_image_url_https":"https:\/\/si0.twimg.com\/profile_images\/60558692\/KennyMugShot_normal.jpg","location":"Singapore","id_str":"16414559","profile_text_color":"663B12","name":"Kenny","statuses_count":198,"profile_background_image_url":"http:\/\/a0.twimg.com\/images\/themes\/theme2\/bg.gif","id":16414559,"default_profile_image":false,"lang":"en","utc_offset":28800,"profile_link_color":"1F98C7","screen_name":"luzm"},"id":223809793016598528,"entities":{"user_mentions":[{"indices":[0,5],"name":"Kenny","id_str":"16414559","id":16414559,"screen_name":"luzm"}],"urls":[{"display_url":"google.com","indices":[6,26],"url":"http:\/\/t.co\/0yzHGZnT","expanded_url":"http:\/\/www.google.com"}],"hashtags":[{"text":"test","indices":[27,32]}]}}'

