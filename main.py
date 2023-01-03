import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# Example: shorten the URL "https://github.com/KlaidasMar"
short_url = shorten_url("https://github.com/KlaidasMar")
print(short_url)
