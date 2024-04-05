import requests
import http.cookiejar

# Create a MozillaCookieJar object
cookie_jar = http.cookiejar.MozillaCookieJar('cookies.txt')

# Send a request to Roblox.com
response = requests.get('https://www.roblox.com', cookies=cookie_jar)

# Add the cookies from the response to the CookieJar
for cookie in response.cookies:
    cookie_jar.set_cookie(cookie)

# Save the cookies to a file
cookie_jar.save()
