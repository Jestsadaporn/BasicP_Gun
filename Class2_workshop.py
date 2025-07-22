print("ระบบคำนวณรายจ่ายค่าขนส่ง")

distand = int(input("input ระยะทาง :"))

if  distand>=5 and distand <=50 :
    print("ค่าขนส่ง : 10 B")
elif  distand>=51 and distand <=100 :
    print("ค่าขนส่ง : 15 B")
elif  distand>=101 and distand <=300 :
    print("ค่าขนส่ง : 25 B")
elif  distand>=301 and distand <=500 :
    print("ค่าขนส่ง : 35 B")
elif  distand> 500 :
    print("ค่าขนส่ง : 45 B")

else :
    print("eror")
