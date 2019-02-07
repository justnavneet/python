import requests,json
""" enter your search querey for palces it show you a list and then  choose your option 
Its show name,address,rating and a image of place"""
api_key=''# add your api key
url="https://maps.googleapis.com/maps/api/place/textsearch/json?"
image="https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="
name=input("enter name of Places ")
page = requests.get(url + 'query=' + name +'&key=' + api_key)#  requests for palces
data=page.json()
search=data['results']
for i in range(len(search)):
    print(i+1,'\t',search[i]['name'])
no=int(input("enter your choice "))
print("Name:\t"+data['results'][no-1]['name']+"\nAddress:\t"+data['results'][no-1]['formatted_address']+"\nRating:\t",data['results'][no-1]['rating'])
photo=requests.get(image+search[no-1]["photos"][0]['photo_reference']+'&key='+api_key)# requests for image
f  = open('temp.jpeg','wb')
f.write(photo.content)
f.close()
import matplotlib.pyplot as plt
with open('temp.jpeg','rb') as fp :#write a image with name 'temp.jpeg in pwd'
    img = plt.imread(fp)
    fp.close()
plt.imshow(img)
plt.show()