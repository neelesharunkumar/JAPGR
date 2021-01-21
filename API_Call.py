import requests

url = 'https://lk425hka04.execute-api.us-east-2.amazonaws.com/capstone_mmx/capstone-mmx-resource'
for i in range(1):
    myobj = {"true": i}

    x = requests.post(url, json = myobj)

    #print(x.text)

    lis = x.text.split(" ")


    print(lis)
    """ if(lis[3]=='high'):
        print(i)
        break """
    print(lis)

