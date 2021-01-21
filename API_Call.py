import requests

url = 'https://lk425hka04.execute-api.us-east-2.amazonaws.com/capstone_mmx/capstone-mmx-resource'
for i in range(1):
    myobj = {"true": i}

    x = requests.post(url, json = myobj)

    #print(x.text)

    lis = x.text.split(" ")

#hello world making  a change
tag = et.SubElement(Parent, tagName, xmlAttributeDict)
    if tagText is None:
        tag.text = ''
    else:
        tag.text = str(tagText).replace(chr(160), ' ').strip()
    #print(tag.text)
    logging.info("{} tag is generated as {} or {}".format(str(tagName))
    print(lis)

