
class Transport():
    def __init__(self,brand,number,speed,capacity):
        self.brand=brand
        self.number=number
        self.speed=speed
        self.capacity=capacity
    def info(self):
        print("\nCreated class CAR")
        print("Brand: {0},Number: {1},Speed: {2},Capacity: {3}".format(self.brand,self.number,self.speed,self.capacity))

class Motorbike(Transport):
    def __init__(self,brand,number,speed,capacity,stroller):
        super().__init__(brand,number,speed,capacity)
        self.stroller=stroller
    def info(self):
        Transport.info(self)
        print("Created podclass MOTORBIKE")
        print("Stroller: {0}".format(self.stroller))

class Truck(Transport):
    def __init__(self,brand,number,speed,capacity,trailer):
        super().__init__(brand,number,speed,capacity)
        self.trailer=trailer

    def info(self):
        Transport.info(self)
        print("Created podclass TRUCK")
        print("Trailer: {0}",format(self.trailer))
main=[]
n=int(input("Input num of transport: "))
for i in range(n):
   choose=input("Choose an element- 1)Car 2)Motorbike 3)Truck: ")
   if choose=="1":
       brand1=input("Input brand:")
       number1=int(input("Input number:"))
       speed1=int(input("Input speed:"))
       capacity1=int(input("Input capacity:"))
       spisok=[brand1,number1,speed1,capacity1]
       main.append(spisok)
       car=Transport(brand1,number1,speed1,capacity1)
       car.info()
       print()
   if choose=="2":
       stroller1=input("Have a stroller? 1)Yes 0)No ")
       if stroller1=="0":
           capacity1=0
       elif stroller1=="1": capacity1=input("Input capacity:")
       brand1=input("Input brand:")
       number1=int(input("Input number:"))
       speed1=int(input("Input speed:"))
       spisok=[brand1,number1,speed1,capacity1]
       main.append(spisok)
       moto=Motorbike(brand1,number1,speed1,capacity1,stroller1)
       moto.info()
       print()
   if choose=="3":
       brand1=input("Input brand:")
       number1=int(input("Input number:"))
       speed1=int(input("Input speed:"))
       capacity1=int(input("Input capacity:"))
       trailer1=input("Have a trailer? 1)Yes 0)No ")
       if trailer1=="1":
           capacity1*=2
       spisok=[brand1,number1,speed1,capacity1]
       main.append(spisok)
       trc=Truck(brand1,number1,speed1,capacity1,trailer1)
       trc.info()
       print()

print("Your list:\n")
for i in range (n):
    print("Element num: ",i)
    print(*main[i])

find_capacity=int(input("\nInput capacity: "))

print("Searched transport:\n")
for i in range(len(main)):
    if(main[i][3]>=find_capacity):
        print("Brand: ",main[i][0]," Number: ",main[i][1]," Speed: ",main[i][2],
              "Capacity: ",main[i][3])