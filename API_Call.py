import requests

for i in range(1):
    myobj = {"true": i}

    x = requests.post(url, json = myobj)
    
    @exception
def createSubElementText(Parent, tagName, xmlAttributeDict, tagText=None):
    
    tag = et.SubElement(Parent, tagName, xmlAttributeDict)
    if tagText is None:
        tag.text = ''
    else:
        tag.text = str(tagText).replace(chr(160), ' ').strip()
    #print(tag.text)
    logging.info("{} tag is generated as {} or {}".format(str(tagName), tagText, str(xmlAttributeDict.values())))
    return tag

    #print(x.text)

    lis = x.text.split(" ")


    print(lis)
    """ if(lis[3]=='high'):
        print(i)
        break """

