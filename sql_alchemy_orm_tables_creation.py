from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from pprint import pprint
import random
import datetime
from dateutil.relativedelta import relativedelta

Base = declarative_base()

class Patients(Base):
    __tablename__ = 'Patients'

    PatientID = Column(Integer, primary_key=True)
    FullName = Column(String)
    AdmissionDate = Column(Date)
    Illness = Column(String)

    def __repr__(self):
        return f"<Patient(PatientID='{self.PatientID}', FullName='{self.FullName}', AdmissionDate='{self.AdmissionDate}', Illness='{self.Illness}')"

class Staff(Base):
    __tablename__ = 'Staff'

    StaffID = Column(Integer, primary_key=True)
    FullName = Column(String)
    Role = Column(String)
    ExperienceLevel = Column(Integer)

    def __repr__(self):
        return f"<Staff(StaffID='{self.StaffID}', FullName='{self.FullName}', Role='{self.Role}', ExperienceLevel='{self.ExperienceLevel}')"

class Departments(Base):
    __tablename__ = 'Departments'

    DepartmentID = Column(Integer, primary_key=True)
    DepartmentName = Column(String)
    Type = Column(String)
    StaffInCharge = Column(String)

    def __repr__(self):
        return f"<Departments(DepartmentID='{self.DepartmentID}', DepartmentName='{self.DepartmentName}', Type='{self.Type}', StaffInCharge='{self.StaffInCharge}')"

class PatientRecords(Base):
    __tablename__ = 'PatientRecords'

    PatientID = Column(Integer, ForeignKey(Patients.PatientID))
    RecordID = Column(Integer, primary_key=True)
    DepartmentVisited = Column(Integer, ForeignKey(Departments.DepartmentID))
    ConsultingStaffID = Column(Integer, ForeignKey(Staff.StaffID))
    TreatmentUpdate = Column(String)
    NextReferral = Column(Integer, ForeignKey(Departments.DepartmentID))

    def __repr__(self):
        return f"<PatientRecords(PatientID='{self.PatientID}', RecordID='{self.RecordID}', DepartmentVisited='{self.DepartmentVisited}', ConsultingStaffID='{self.ConsultingStaffID}', TreatmentUpdate='{self.TreatmentUpdate}', NextReferral='{self.NextReferral}')"

engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

#Patient Detail Insertion
names = ['Cecily Cluck','Marcellus Moreman','Lora Lowery','Shakira Striplin','Sofia Sleeth','Kanesha Kuyper','Freeda Fandel','Kassandra Keehn','Kathleen Kahn','Alvera Auger','Patrice Petters','Suzan Spearman','Maybell Morejon','Kathryne Kantor','Juliana Juan','Pauline Pegram','Erlinda Elser','Taylor Tabb','Eun Eliason','Shelli Speidel']
illnesses = ['8-bitten','Clamp','Floppy Discs','Headcrabbedness','Jest Infection','Lycanthrophy','Mucky Feet','Premature Mummification','Spontaneous Combustion','Animal Magnetism','Cubism','Flumps','Heart Throb','Jumbo DNA','Mime Crisis','Night Fever','Pudding Blood','Touch of Midas','Bed Face','Cross Bones','Freudian Lips','Humerus Injury','Lazy Bones','Misery Guts','Pandemic','Rock Bottom','Turtle Head','Boggled Mind','Decision Rash','Grey Anatomy','Hurty Leg','Leopard Skin','Mock Star','Pipe Organs','Shattered','Verbal Diarrhoea','Bogwarts','Denim Genes','Grout','Inflated Ego','Light Headed','Monobrow','Portishead','Shock Horror','Broken Face']

for name in names:
    patient_id = random.randint(10**(10-1),10**10)
    illness = random.choice(illnesses)
    admit_date = datetime.date.today() - relativedelta(days = random.randint(1, 10))
    new_patient = Patients(PatientID=patient_id, FullName=name, AdmissionDate=admit_date, Illness=illness)
    session.add(new_patient)

session.commit()

df = pd.read_sql('SELECT * FROM Patients', con=engine)

pprint(df)

#Staff Detail Insertion
s_names = ['Leon Fairley','Gretchen Lockhart','Zella Nall','Eric Farren','Richard Rohde','Adelaide Rister','Donnie Donald','Kaitlin Beddingfield','Chauncey Piermarini','Hye Byars','Valorie Hager','Kirstin Domenick','Marietta Masker','Arleen Maltby','Jeni Mcmunn','Ruben Vanpatten','Alexia Borgman','Alica Popovic','Tricia Brockett','Leesa Anding']
roles = ['Senior Doctor','Trainee Doctor','Doctor','Senior Nurse','Junior Nurse','Nurse']
levels = [1,2,3,4,5,6]


for name in s_names:
    staff_id = random.randint(10**(10-4),10**10-3)
    role = random.choice(roles)
    level = random.choice(levels)
    new_staff = Staff(StaffID=staff_id, FullName=name, Role=role, ExperienceLevel=level)
    session.add(new_staff)

session.commit()

df = pd.read_sql('SELECT * FROM Staff', con=engine)

pprint(df)

#Department Table Insertion
d_names = ["Emergency", "Cardiology", "Oncology", "Neurology"]
staffs_incharge = {"Emergency":'Leon Fairley',"Cardiology":'Gretchen Lockhart',"Oncology":'Zella Nall',"Neurology":'Eric Farren'}

for name in d_names:
    d_id = random.randint(10**2,1000)
    type = "Internal"
    st_incharge = staffs_incharge[name]
    new_department = Departments(DepartmentID=d_id, DepartmentName=name, Type=type, StaffInCharge=st_incharge)
    session.add(new_department)

session.commit()

df = pd.read_sql('SELECT * FROM Departments', con=engine)

pprint(df)
