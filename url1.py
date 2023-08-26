import pyshorteners

url = input("ENTER THE URL :")

def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shortenurl(url)
