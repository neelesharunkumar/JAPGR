import random
import datetime
from dateutil.relativedelta import relativedelta

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date, select
from sqlalchemy.ext.declarative import declarative_base  # ***
from sqlalchemy.orm import sessionmaker  # ***
import pandas as pd
from pprint import pprint

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'Patients'
    
    PatientID = Column(Integer, primary_key=True)
    FullName = Column(String)
    AdmissionDate = Column(Date)
    Illness= Column(String)
    
    def __repr__(self):
        return f"<Patient(PatientID='{self.PatientID}', FullName='{self.FullName}', AdmisisonDate='{self.AdmissionDate}', Illness='{self.Illness}')"


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)

session = Session()

names = ['Cecily Cluck','Marcellus Moreman','Lora Lowery','Shakira Striplin','Sofia Sleeth','Kanesha Kuyper','Freeda Fandel','Kassandra Keehn','Kathleen Kahn','Alvera Auger','Patrice Petters','Suzan Spearman','Maybell Morejon','Kathryne Kantor','Juliana Juan','Pauline Pegram','Erlinda Elser','Taylor Tabb','Eun Eliason','Shelli Speidel']
illnesses = ['8-bitten','Clamp','Floppy Discs','Headcrabbedness','Jest Infection','Lycanthrophy','Mucky Feet','Premature Mummification','Spontaneous Combustion','Animal Magnetism','Cubism','Flumps','Heart Throb','Jumbo DNA','Mime Crisis','Night Fever','Pudding Blood','Touch of Midas','Bed Face','Cross Bones','Freudian Lips','Humerus Injury','Lazy Bones','Misery Guts','Pandemic','Rock Bottom','Turtle Head','Boggled Mind','Decision Rash','Grey Anatomy','Hurty Leg','Leopard Skin','Mock Star','Pipe Organs','Shattered','Verbal Diarrhoea','Bogwarts','Denim Genes','Grout','Inflated Ego','Light Headed','Monobrow','Portishead','Shock Horror','Broken Face']

for name in names:
    patient_id = random.randint(10**(10-1),10**10-1 )
    illness = random.choice(illnesses)
    admit_date = datetime.date.today() - relativedelta(days = random.randint(1, 10))

    new_patient = Patient(PatientID=patient_id, FullName=name, AdmissionDate=admit_date, Illness=illness)
    session.add(new_patient)

session.commit()

df = pd.read_sql('SELECT * FROM Patients', con=engine)

pprint(df)
