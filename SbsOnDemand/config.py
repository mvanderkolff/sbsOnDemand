## @namespace SbsOnDemand::config
# Module for setting configuration variables and storing global constants such as urls

# User-specified constants

## Manual proxy specification (can be used for debugging)
#
# Set to None for default (system) proxy
#
# Should be a dict object, such as {'http': '127.0.0.1:8080'}
PROXY = None

# Constants - don't change
API_BASE = "http://www.sbs.com.au/api/video_feed"
MENU_URI = "http://www.sbs.com.au/ondemand/js/video-menu"
LOGIN_URI = "http://my.sbs.com.au/go/login/onesiteSignIn"
LOGOUT_URI = "http://www.sbs.com.au/api/Member/logout"
ONDEMAND_UI_BASE_URI = "http://www.sbs.com.au/ondemand/video/"
RELEASE_URL_KEY = 'http://resources.sbs.com.au/vod/theplatform/core/current/swf/flvPlayer.swf?releaseUrl'
ONDEMAND_UI_VIDEO_CSS_QUERY = 'meta[property="og:video"]'
MPX_FEEDID = "dYtmxB"
SEARCH_FEEDID = "search"
ALLDATA_FEEDID = "CxeOeDELXKEv"
DEFAULT_FEEDS = [
    {"name": "Programs", "feedId": "section-programs"},
    {"name": "Clips", "feedId": "section-clips"},
    {"name": "Events", "feedId": "section-events"},
    {"name": "Last Chance", "feedId":"videos-lastchance"},
    {"name": "Featured Programs", "feedId":"featured-programs-prod"},
    {"name": "Featured Clips", "feedId":"featured-clips"}
]
