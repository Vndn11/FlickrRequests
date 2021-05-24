import requests
api_key = 'bd1df74633ade1306cc7c9866df7ee1c'
user_id = '193040150%40N05'
format1 = 'json'
r = requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key={api_key}&user_id={user_id}&format={format1}&nojsoncallback=1'.format(api_key=api_key,user_id=user_id,format1=format1))

print(r.content)
#bd1df74633ade1306cc7c9866df7ee1c
#2132639adab9eb49