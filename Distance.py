import requests,json,os
def searchId(name):
    """string --> seachId() --> list i.e ['place_id','place_name'] 
    it show search results and ask your choice"""
    api_key=''# add yor api key
    url="https://maps.googleapis.com/maps/api/place/textsearch/json?"
    page = requests.get(url + 'query=' + name +'&key=' + api_key)
    data=page.json()
    search=data['results']
    for i in range(len(search)):
        print(i+1,'\t',search[i]['name'])
    no=int(input("enter your choice "))
    os.system('cls')
    return [data['results'][no-1]['place_id'],data['results'][no-1]['name']]
def start():# main function
    """ find distance between two palces and travel time with car"""
    id1=searchId(input('serch for origin place '))
    id2=searchId(input('search for destinations place '))

    url='https://maps.googleapis.com/maps/api/distancematrix/json?'
    api_key=''# add your api key
    page=requests.get(url+'origins=place_id:'+id1[0]+'&destinations=place_id:'+id2[0]+'&key='+api_key)
    data=page.json()
    print("origin\t",id1[1],'\ndestination\t',id2[1])
    print("diatance\t",data['rows'][0]['elements'][0]['distance']['text'],"duration\t",data['rows'][0]['elements'][0]['duration']['text'])
start()