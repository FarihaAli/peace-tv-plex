# -*- coding: utf-8 -*-
PREFIX = '/video/peacetv'

PEACETV_LIVE = 'http://www.peacetv.in/live_peacetv.html'

PEACETV = 'www.peacetv.in'

NAME= 'Peace TV'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0'


TITLE = L('PeaceTV')
ART = 'art-default.png'
ICON = 'icon-default.png'
PEACE_SWF = 'http://www.peacetv.in/swf/player.swf'
PLAYER = 'rtmp://peace.fms.visionip.tv/live/'
APP = 'live/'
PLAYPATHCLIP = 'b2b-peace_usa-live-25f-4x3-sdh_1'
rurl = 'rtmp://peace.fms.visionip.tv/live/b2b-peace_usa-live-25f-4x3-sdh_1'
####################################################################################################
def Start():

# Setup the default breadcrumb title for the plugin
    ObjectContainer.art = R(ART)
    ObjectContainer.title1 = NAME
    
# This main function will setup the displayed items.
# Initialize the plugin

#######################################################################
@handler(PREFIX, NAME, R(ART), R(ICON))
def MainMenu():

    oc = ObjectContainer()    
   # oc.add(DirectoryObject(key=Callback(ChannelMenu), title="Live"))

    Log(' --> RTMPDump test command line: rtmpdump -r "%s" -y "%s" -W "%s" -o output.flv' % (PLAYER, PLAYPATHCLIP, PEACE_SWF))
   
    #oc.add(VideoClipObject(
            
          # key = RTMPVideoURL(url=PLAYER, clip=PLAYPATHCLIP, app=APP, swf_url=PEACE_SWF, live=True),
        #key = RTMPVideoURL(url=rurl,live=True),
        #rating_key=5.0,
        #title = NAME,
        #thumb = R(ART)
       #))
    
    
    oc.add(CreateVideoClipObject(
            rurl = rurl,
            title = NAME,
            thumb = R(ART),
            summary = NAME
        ))
    
    
    
    return oc
 
 ##################################################
@route(PREFIX + '/createvideoclipobject')
def CreateVideoClipObject(rurl, title, thumb, summary = None, container = False):
    vco = VideoClipObject(
        key = Callback(CreateVideoClipObject, rurl = rurl, title = title, thumb = thumb, summary = summary, container = True),
        rating_key = 5.0,
       # url = rurl,
        title = title,
        thumb = thumb,
        summary = summary,
        items = [
            MediaObject(
                #container = Container.MP4,     # MP4, MKV, MOV, AVI
                #video_codec = VideoCodec.H264, # H264
                #audio_codec = AudioCodec.AAC,  # ACC, MP3
                #audio_channels = 2,            # 2, 6
                parts = [
                    PartObject(
                        key = GetVideoURL(rurl = rurl)
                    )
                ],
                optimized_for_streaming = True
            )
        ]
    )
    if container:
        return ObjectContainer(objects = [vco])
    else:
        return vco
    return vco
 
 
 
 
 
 
 #######################################
def GetVideoURL(rurl, live = True):
    if rurl.startswith('rtmp'):
        #Log.Debug('*' * 80)
        #Log.Debug('* url before processing: %s' % url)
        #if url.find(' ') > -1:
        #    playpath = GetAttribute(url, 'playpath', '=', ' ')
        #    swfurl = GetAttribute(url, 'swfurl', '=', ' ')
        #    pageurl = GetAttribute(url, 'pageurl', '=', ' ')
        #    url = url[0:url.find(' ')]
        #    Log.Debug('* url_after: %s' % RTMPVideoURL(url = url, playpath = playpath, swfurl = swfurl, pageurl = pageurl, live = live))
        #    Log.Debug('*' * 80)
        #    return RTMPVideoURL(url = url, playpath = playpath, swfurl = swfurl, pageurl = pageurl, live = live)
        #else:
        #    Log.Debug('* url_after: %s' % RTMPVideoURL(url = url, live = live))
        #    Log.Debug('*' * 80)
        #    return RTMPVideoURL(url = url, live = live)
        #Log.Debug('* url after processing: %s' % RTMPVideoURL(url = url, live = live))
        #Log.Debug('*' * 80)
        #return RTMPVideoURL(url=PLAYER, clip=PLAYPATHCLIP, app=APP, swf_url=PEACE_SWF, live=True)
        return RTMPVideoURL(url=rurl, live=True)
    #elif url.startswith('mms') and Prefs['mms']:
    #    return WindowsMediaVideoURL(url = url)
    else:
        return HTTPLiveStreamURL(url = rurl)
