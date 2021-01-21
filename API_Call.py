import requests

url = 'https://lk425hka04.execute-api.us-east-2.amazonaws.com/capstone_mmx/capstone-mmx-resource'
for i in range(1):
    myobj = {"true": i}

    x = requests.post(url, json = myobj)

    #print(x.text)

    lis = x.text@exception
def createSubElementText(Parent, tagName, xmlAttributeDict, tagText=None):
    
    tag = et.SubElement(Parent, tagName, xmlAttributeDict)
    if tagText is None:
        tag.text = ''
    else:
        tag.text = str(tagText).replace(chr(160), ' ').strip()
    #print(tag.text)
    logging.info("{} tag is generated as {} or {}".format(str(tagName), tagText, str(xmlAttributeDict.values())))
    return tag


    print(lis)
    """ if(lis[3]=='high'):
        print(i)
        break """

