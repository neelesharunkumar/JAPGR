import random
import datetime
from dateutil.relativedelta import relativedelta

from sqlalchemy import create_engine  # ***
import pandas as pd
from pprint import pprint

engine = create_engine('sqlite:///:memory:', echo=True)

query = '''CREATE TABLE Patients tag = et.SubElement(Parent, tagName, xmlAttributeDict)
    if tagText is None:
        tag.text = ''
    else:
        tag.text = str(tagText).replace(chr(160), ' ').strip()
    #print(tag.text)
    logging.info("{} tag is generated as {} or {}".format(str(tagName), tagText"

input()
names = ['Cecily Cluck','Marcellus Moreman','Lora Lowery','Shakira Striplin','Sofia Sleeth','Kanesha Kuyper','Freeda Fandel','Kassandra Keehn','Kathleen Kahn','Alvera Auger','Patrice Petters','Suzan Spearman','Maybell Morejon','Kathryne Kantor','Juliana Juan','Pauline Pegram','Erlinda Elser','Taylor Tabb','Eun Eliason','Shelli Speidel']
illnesses = ['8-bitten','Clamp','Floppy Discs','Headcrabbedness','Jest Infection','Lycanthrophy','Mucky Feet','Premature Mummification','Spontaneous Combustion','Animal Magnetism','Cubism','Flumps','Heart Throb','Jumbo DNA','Mime Crisis','Night Fever','Pudding Blood','Touch of Midas','Bed Face','Cross Bones','Freudian Lips','Humerus Injury','Lazy Bones','Misery Guts','Pandemic','Rock Bottom','Turtle Head','Boggled Mind','Decision Rash','Grey Anatomy','Hurty Leg','Leopard Skin','Mock Star','Pipe Organs','Shattered','Verbal Diarrhoea','Bogwarts','Denim Genes','Grout','Inflated Ego','Light Headed','Monobrow','Portishead','Shock Horror','Broken Face']

for name in names:
    patient_id = random.randint(10**(10-1),10**10-1 )
    illness = random.choice(illnesses)
    admit_date = datetime.date.today() - relativedelta(days = random.randint(1, 10))

    insert_query = f'''
    INSERT INTO Patients VALUES ({patient_id}, "{name}", "{admit_date}", "{illness}")
    '''
    engine.execute(insert_query) 

input()

query = '''SELECT * FROM Patients'''
for row in engine.execute(query):
    print(row)

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