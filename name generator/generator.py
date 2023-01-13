import random as rand


def GenerateName():
    femaleNamesFile = open("femaleNames.txt",'r')
    maleNamesFile = open("maleNames.txt",'r')
    lastNamesFile = open("lastNames.txt",'r')

    femaleNames=[]
    maleNames = []
    lastNames = []

    while (femaleNamesFile.readline() != ""):
        femaleNames.append(femaleNamesFile.readline())
        
    while (maleNamesFile.readline() != ""):
        maleNames.append(maleNamesFile.readline())

    while (lastNamesFile.readline() != ""):
        lastNames.append(lastNamesFile.readline())

    male = rand.randint(0,1)

    if male==0:
        return(maleNames[rand.randint(0,len(maleNames)-1)].strip('\n')+ lastNames[rand.randint(0,len(lastNames)-1)].strip('\n'))

    else:
        return(femaleNames[rand.randint(0,len(femaleNames)-1)].strip('\n') + lastNames[rand.randint(0,len(lastNames)-1)].strip('\n'))
		
def GenerateMaleName():
    maleNamesFile = open("maleNames.txt",'r')
    lastNamesFile = open("lastNames.txt",'r')

    maleNames = []
    lastNames = []

    while (maleNamesFile.readline() != ""):
        maleNames.append(maleNamesFile.readline())

    while (lastNamesFile.readline() != ""):
        lastNames.append(lastNamesFile.readline())

    return(maleNames[rand.randint(0,len(maleNames)-1)].strip('\n')+ lastNames[rand.randint(0,len(lastNames)-1)].strip('\n'))


def GenerateFemaleName():
    femaleNamesFile = open("femaleNames.txt",'r')
    lastNamesFile = open("lastNames.txt",'r')

    femaleNames = []
    lastNames = []

    while (femaleNamesFile.readline() != ""):
        femaleNames.append(femaleNamesFile.readline())

    while (lastNamesFile.readline() != ""):
        lastNames.append(lastNamesFile.readline())

    return(femaleNames[rand.randint(0,len(femaleNames)-1)].strip('\n') + lastNames[rand.randint(0,len(lastNames)-1)].strip('\n'))

    
    
def GenerateDateOfBirth():
    year = str(rand.randint(1943,1994))
    month = str(rand.randint(1,12))
    day = str(rand.randint(1,28))

    return(year+"/"+month+"/"+day)

def GenerateAppointmentDateTime():

    year = "2020"
    month = str(rand.randint(1,12))
    day = str(rand.randint(1,28))
    hour = str(rand.randint(8,20))
    minute = rand.randint(0,1)
    if minute==0:
        minute = "30"
    else:
        minute = "00"

    return(year+"/"+month+"/"+day+" "+hour+":"+minute+":00")
def GenerateAddress():
    lastNamesFile = open("lastNames.txt",'r')
    lastNames = []
    while (lastNamesFile.readline() != ""):
        lastNames.append(lastNamesFile.readline())

    city = lastNames[rand.randint(0,len(lastNames)-1)].strip('\n')+" City"

    block = chr(rand.randint(65,90))

    road = str(rand.randint(0,30))

    building = str(rand.randint(0,35))

    appartment= str(rand.randint(0,30))+chr(rand.randint(65,70))

    return(city+", Block: "+block+", Road: "+road+", Building: "+building+", Apparment Number: "+ appartment)

def GenerateNRIC():
    return(str(rand.randint(334210,913290)))

def GenerateOccupation():
    jobs= []
    jobsFile = open("jobs.txt",'r')

    while(jobsFile.readline() != ""):
        jobs.append(jobsFile.readline())

    return(jobs[rand.randint(0,len(jobs)-1)].strip('\n'))

def GenerateIngredients():
    ingList = []
    ingredientsFile = open("ingredients.txt",'r')

    while(ingredientsFile.readline() != ""):
        ingList.append(ingredientsFile.readline().strip('\n'))

    number = rand.randint(2,4)
    exitString = ""
    for r in range(number):
        exitString += ingList[rand.randint(0,len(ingList)-1)]
        if r!=number-1:
            exitString += ", "

    return(exitString)

def GeneratePhone():
    return("+60 "+str(rand.randint(10000000,98221229)))

def GenerateBloodType():

    types = ["A+","A-","B+","B-","AB+","AB-","O-","O+"]

    return(types[rand.randint(0,7)])

def GenerateBloodPressure():
    systolic = str(rand.randint(80,140))
    diastolic = str(rand.randint(50,100))

    return(systolic+"/"+diastolic+"mmHg")

def GenerateHeartRate():

    return(rand.randint(40,110))

def GenerateWeight():

    return(rand.randint(45,140))

def GeneratePatientID():
    return (str(rand.randint(1,100)))
def GenerateDoctorID():
    return(str(rand.randint(1,20)))

def GenerateSpecialization():

    specializations = []
    specializationsFile = open("specializations.txt",'r')

    while(specializationsFile.readline() != ""):
        specializations.append(specializationsFile.readline())
    return(specializations[rand.randint(0,len(specializations)-1)].strip('\n'))
    
def GenerateSex():
    m = rand.randint(0,1)
    if m==1:
        return 'M'
    else:
        return 'F'
def GenerateShift():
    startHour = str(rand.randint(8,16))
    endHour = str(rand.randint(int(startHour)+4,23))

    return("'"+startHour+":00:00"+"',\n"+"'"+endHour+":00:00"+"'")

def GeneratePatients(count):
    file = open("patients.sql",'w')
    file.write(
        "INSERT INTO patient (name,address,nric,drug_id,date_of_birth,sex,occupation,phone)\n")
    file.write("VALUES\n")
    for r in range(count):
        gend = rand.randint(0,1)
        if gend == 0:
            file.write("(")
            file.write("'"+GenerateFemaleName()+"',")
            file.write("'"+GenerateAddress()+"',")
            file.write("'"+GenerateNRIC()+"',")
            file.write(str(rand.randint(0,1))+",")
            file.write("'"+GenerateDateOfBirth()+"',")
            file.write("'F',")
            file.write("'"+GenerateOccupation()+"',")
            file.write("'"+GeneratePhone()+"'")
            if r!=count-1:
                file.write("),\n")
            else:
                file.write(");")
        else:
            file.write("(")
            file.write("'"+GenerateMaleName()+"',")
            file.write("'"+GenerateAddress()+"',")
            file.write("'"+GenerateNRIC()+"',")
            file.write(str(rand.randint(0,1))+",")
            file.write("'"+GenerateDateOfBirth()+"',")
            file.write("'M',")
            file.write("'"+GenerateOccupation()+"',")
            file.write("'"+GeneratePhone()+"'")
            if r!=count-1:
                file.write("),\n")
            else:
                file.write(");")
    file.close()
            
            
        

def GenerateDoctors(count):

    file = open("doctors.sql","w")
    file.write(
        "INSERT INTO doctor (name,date_of_birth,sex,specialization)\n")
    file.write("VALUES\n")
    for r in range(count):
        gend = rand.randint(0,1)
        if gend==0:
            file.write("(")
            file.write("'"+GenerateFemaleName()+"',")
            file.write("'"+GenerateDateOfBirth()+"',")
            file.write("'F',")
            file.write("'"+GenerateSpecialization()+"'")
            if r!=count-1:
                file.write("),")
            else:
               file.write(");")
        else:
            file.write("(")
            file.write("'"+GenerateMaleName()+"',")
            file.write("'"+GenerateDateOfBirth()+"',")
            file.write("'M',")
            file.write("'"+GenerateSpecialization()+"'")
            if r!=count-1:
                file.write("),\n")
            else:
               file.write(");")
    file.close()


def GeneratePatientData(count):
    file = open("patientdata.sql",'w')
    file.write("INSERT INTO patient_data(patient_ref_id,doctor_id,record_date,blood_type,blood_pressure,heart_rate,weight,depression_indicators,status)\n")
    file.write("VALUES\n")
    for r in range(1,count+1):
        file.write("(")
        file.write(str(r)+",")
        file.write(str(rand.randint(1,10))+",")
        file.write("NOW(),")
        file.write("'"+GenerateBloodType()+"',")
        file.write("'"+GenerateBloodPressure()+"',")
        file.write(str(GenerateHeartRate())+",")
        file.write(str(GenerateWeight())+",")
        file.write(str(rand.randint(0,1))+",")
        file.write("'Active'")
        if r!=count:
            file.write("),\n")
        else:
            file.write(");")
    file.close()

def GenerateSecretaries(count):
	file = open("secretaries.sql",'w')
	file.write("INSERT INTO secretary(secretary_id,name,address)\n")
	file.write("VALUES\n")
	for r in range(1,count+1):
		file.write("(")
		x=str(r)+","
		file.write(x)
		file.write("'"+GenerateName()+"',")
		file.write("'"+GenerateAddress()+"'")
		if r!=count:
		    file.write("),\n")
		else:
		    file.write(");")
	file.close()

def GenerateAppointments(count):
    file = open("appointments.sql",'w')
    file.write("INSERT INTO appointment(doctor_id,patient_id,time,status)\n")
    file.write("VALUES\n")
    for r in range(count):
        file.write("(")
        file.write(GeneratePatientID(),",")
        file.write("'"+GenerateAppointmentDateTime()+"',")
        file.write("'Pending'")
        if r!=count-1:
            file.write("),\n")
        else:
            file.write(");")
    file.close()
        
def GenerateNurses(count):
    file = open("nurses.sql",'w')
    file.write("INSERT INTO nurse(name,address,date_of_birth,nric,shift_start,shift_end)\n")
    file.write("VALUES\n")
    for r in range(count):
        file.write("(")
        file.write("'"+GenerateName()+"',")
        file.write("'"+GenerateAddress()+"',")
        file.write("'"+GenerateDateOfBirth()+"',")
        file.write("'"+GenerateNRIC()+"',")
        file.write(GenerateShift())
        if r!=count-1:
            file.write("),\n")
        else:
            file.write(");")


        
