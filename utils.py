import pyshorteners
import aiohttp
import shortzy

DROPLINK_API = "l95bCWl1VgbEwLc4O4mQut61T0u2"

shortz = shortzy.Shortzy(DROPLINK_API, "shareus.in")

####################  droplink  ####################
async def newlink(link):
    print(link)
    if LONG_DROPLINK_URL == "True" or LONG_DROPLINK_URL is True:
        return await shortz.get_quick_link(link, silently_fail=True)
    else:
        return await shortz.convert(link)
