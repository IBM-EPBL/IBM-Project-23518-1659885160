from numpy import random
while(1):
    temp=random.uniform(1,100)
    humidity=random.uniform(40,100)
    if(temp>=18 and temp<=30 and humidity>=60 and humidity<=80):
        print("Temperature is normal")
    elif(temp>=30):
        print("Temperature is HIGH !!")
    elif(humidity>=80):
        print("Temperature is HIGH !!")
