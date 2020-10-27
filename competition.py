#the name of this code is health monitor by maxi code team
# by sai rishi and harshith
#@title Default title text
#this is an otp genrator and the page is accessed only when the correct otp is entered
import sys
import math,random
def generateOTP() : #
#otp generator
    OTP=random.randint(0000,9999)
    return OTP
OTP=generateOTP()   
#input your phone number
phone_number=(input("Enter your phone number : "))
if len(phone_number) != 10:
  print("Please enter valid number")
  sys.exit()
#otp will be recieved
print("OTP received on mobile :  ",OTP)
q = int(input("Enter OTP:  "))
if OTP == q:
  print("Fetching your health record...!")
  #inputyour other details
  name = (input("Please enter your name : "))
  age= int(input("Please enter your age : "))
  if age <=0 or age >=120:
    print("invalid input")
    sys.exit()
  gender = str(input("Enter your gender[male,female,others] : "))
  height = float(input("Enter Height in Metres : "))
  weight = float(input("Enter Weight in Kilograms : "))
else:
	print("You dont have access to health record ,please retry")
 #the weight of the obesity on a the human immune respone to vaccination
bmi = (weight/(height*height))
print("Your BMI is: %f"%(bmi))
if bmi < 18.5:
	print("Your BMI is Underweight")
elif bmi > 18.5 and bmi < 25 :
	print("Your BMI is Normal")
elif bmi >25 and bmi<30:
	print ("Your BMI is Overweight")
elif bmi >30 and bmi <40:
	print("Your BMI is Obese")
else:
	print("Your BMI is Extremely Obese")	
 #your inputs again
dads_height = float(input("PLease enter your fathers height in meters : "))
moms_height = float(input("Please enter your mothers height in metres : "))
#this is if you are a male
if gender == 'male' :
	future_height = ((moms_height + dads_height +.13) / (2))
	print("Your future height is : " + str(future_height))
 #this is if you are a female
elif gender == 'female' :
	future_height = ((moms_height + dads_height -.13) / (2))
	print("Your future height is : " + future_height)
 #this for others
else:
		future_height = ((moms_height + dads_height +.13) / (2))
		print("Your future height is : " + future_height)
months=int(input("enter your baby's age in months (0-15) : "))
print(months)
#definitions of certian diseases
#dictionary 
vaccine={"hepatities b":"Hepatitis B is a potentially life-threatening liver infection caused by the hepatitis B virus (HBV). It is a major global health problem. It can cause chronic infection and puts people at high risk of death from cirrhosis and liver cancer","rotavirus":"Rotavirus is a genus of double-stranded RNA viruses in the family Reoviridae. Rotaviruses are the most common cause of diarrhoeal disease among infants and young children. Nearly every child in the world is infected with a rotavirus at least once by the age of five.","influenza type b":"Influenza B virus is the only species in the genus Betainfluenzavirus in the virus family Orthomyxoviridae. Influenza B virus is only known to infect humans and seals."}
booster={"tetanus":"Overview. Tetanus is a serious disease caused by a bacterial toxin that affects your nervous system, leading to painful muscle contractions, particularly of your jaw and neck muscles. Tetanus can interfere with your ability to breathe and can threaten your life. Tetanus is commonly known as ","influenza type B":"Influenza B virus is the only species in the genus Betainfluenzavirus in the virus family Orthomyxoviridae. Influenza B virus is only known to infect humans and seals."}
super={"pneumcoccol conjucate ":"Pneumococcal conjugate vaccine (PCV) is a pneumococcal vaccine and a conjugate vaccine used to protect infants, young children, and adults against disease caused by the bacterium Streptococcus pneumoniae (pneumococcus).","inactive polio":"Inactivated polio vaccine (IPV) was developed in 1955 by Dr Jonas Salk. Also called the Salk vaccine IPV consists of inactivated (killed) poliovirus strains of all three poliovirus types. IPV is given by intramuscular or intradermal injection and needs to be administered by a trained health worker"}
#the particular vaccine and dosage are different for ech child and the list is below 
if months == 0 :
  print("hepatities b")
  print(vaccine["hepatities b"]) 
elif months == 1 :
  print("2nd dose of hepatitis b")
  print(vaccine["hepatities b"]) 
elif months == 2:
  print("2nd dose continuation of hepatitis b , rotavirus , tetanus,influenza type b,pneumococcal conjugate,inactive poliovirus")
  print(vaccine["hepatities b"])
  print(vaccine["rotavirus"])
  print(booster["tetanus"])
  print(booster["influenza type B"])
elif months == 3:
	print("no dosage/vaccine required")
elif months == 4:
  print("rotvirus 2nd dose , tetnus 2nd dose , influenza type b 2 nd dose , pneumcoccol conjucate 2nd dose,  inactive polio 2nd dose")
  print(vaccine["rotavirus"])
  print(booster["tetanus"])
  print(booster["influenza type B"])
  print(super["pneumcoccol conjucate "])
  print(super["inactive polio"])
elif months == 5:
	print("no vaccine")
elif months == 6:
  print("starting of third dose of hepatitis b , rotavirus third dose, tetanus third dose, pneumococcol conjugate third dose,polio third dose(starting)")
  print(vaccine["hepatities b"])
  print(vaccine["rotavirus"])
  print(booster["tetanus"])
  print(super["pneumcoccol conjucate "])
  print(super["inactive polio"])
elif months == 7:
  print("continuing of third dose of hepetitis and polio")
  print(vaccine["hepatities b"])
  print(super["inactive polio"])
elif months == 8:
  print("contiuation of third dose of hepatitis b anfd polio")
  print(vaccine["hepatities b"])
  print(super["inactive polio"])
elif months == 9:
  print("contuation of third dose of hepatitis b and polio")
  print(vaccine["hepatities b"])
  print(super["inactive polio"])
elif months == 10:
  print("No vaccine required")
elif months == 11:
  print("no vaccine required")
elif months == 12:
  print("third dose of hepatitis b , third or fourth dose of influenza type b,contiuation of third dose of inactived poliovirus")
  print(vaccine["hepatities b"])
  print(booster["influenza type B"])
  print(super["inactive polio"])
elif months == 13:
  print("contiuation of third dose of hepatitis b,fourth dose of tetanus,third or fourth dose of influenza type b , fourth dose pneumococccol conjugate,continuation of fourth dose of inactivated poliovirus ")
  print(vaccine["hepatities b"])
  print(vaccine["rotavirus"])
  print(booster["tetanus"])
  print(super["pneumcoccol conjucate "])
  print(super["inactive polio"])
elif months == 14:
  print(" fourth of tetanus, third or fourth dose of influenza type b ,contuation of fourth dose of pneumococcal conjugate, contuation of third dose of inactivated poliovirus  ")
  print(vaccine["hepatities b"])
  print(vaccine["rotavirus"])
  print(booster["tetanus"])
  print(super["pneumcoccol conjucate "])
  print(super["inactive polio"])
else:
  print("fourth dose of tetanus , third or fourth dose of influenza type b , continuation of fourth dose of pneumococcal conjugate , continuation of inactivated poliovirus")
  print(vaccine["hepatities b"])
  print(vaccine["rotavirus"])
  print(booster["tetanus"])
  print(super["pneumcoccol conjucate "])
  print(super["inactive polio"])