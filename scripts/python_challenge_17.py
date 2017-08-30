import urllib2, urllib
import cookielib
import bz2
import xmlrpclib

# Picture of cookies.. use EditThisCookie to inspect ours
# Have a cookie "info", value "you should have followed busynothing".  Go to challenge 4 and replace ..?nothing=.. with
# ..?busynothing=..

# We now notice the cookie value changes each time we jump a "busynothing" - need to keep track of these


def get_next_busynothing(current_busynothing):
    cookie_jar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
    urllib2.install_opener(opener)

    response = urllib2.urlopen(urllib2.Request("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + current_busynothing))
    html = response.read()
    print(html)
    for cookie in cookie_jar:
        print("Cookie name: {}, value: {}".format(cookie.name, cookie.value))
        if cookie.name == "info":
            cookie_value = cookie.value


    # Check for division by two statement
    if "Yes. Divide by two and keep going." in html:
        print(str(int(current_busynothing) / 2))
        return str(int(current_busynothing) / 2)
    next_busynothing = html.split(" ")[-1]
    print(next_busynothing)
    return next_busynothing, cookie_value

if __name__ == "__main__":
    # output_string = ""
    # current_busynothing = "12345"
    # for i in range(1000):
    #     current_busynothing, cookie_value = get_next_busynothing(current_busynothing)
    #     output_string += cookie_value
    #     # "That's it."
    #     if current_busynothing == "it.": break


    output_string = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
    print(output_string)
    # URL encoded

    print(bz2.decompress(urllib.unquote_plus(output_string)))

    # 'is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.'
    # mozart's father?
    # maybe go back to the phone thing from #13


s = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(s.phone("Leopold")) #555-VIOLIN

# http://www.pythonchallenge.com/pc/stuff/violin.php
# "it's me. what do you want?"
# Need to inform him the flowers are on their way
# Using EditThisCookie to set info cookie to "the+flowers+are+on+their+way" he now says "don't you dare forget the balloons"

# balloons

#http://www.pythonchallenge.com/pc/return/balloons.html