# def hello ():
#     print("hello")
# hello()
# ------------------
# def sum (a,b,):
#     print(a+b)

# sum(10,20)
# ------------------
# def add(a,b):
#     return a+b
# add(1,2)
# add (20,-20)
# # นิยมเอาตัวแปรเข้าฟังชัน
# x = 15
# y = 15
# add(x,y)
# -------------------
# def introduction (Dname):
    
#     print ("my name is " , Dname)
#     tellage ()

# # introduction("Gunner")
# introduction(input("plz input your name : "))
# ----------------------------------------
# โจทย์ปัญหาาาาา !!!!
# age
# input 
# your age is 
# tell age
# ต้องเรียกฟังชัน 
# ---------------------------------------------
# def tellage () :
#     yourage = (input("input your age "))
#     print("your age is " ,  yourage)



# introduction(input("input your name "))

# ----------------------------------------

# def spamm(numofloop):
#     for i in range (5) :
#         print(numofloop)
    
# spamm((input("input str >> ")))

#------------------------------------------

# list  ชุดข้อมูลหลายค่า เก็บในตัวแปรเดียว
#ใช้ [] เก็ยข้อมูลหลายชนิด

# สร้าง list และแสดงผล
# x = ["gun","net",1,2,500]
#  print (x[3])
# sum = x[2] + x[3]
# print (sum)
# ----------------------------------------
# แก้ไข list 
# x [2] = "ton"
# x [3] = 4
# x [4] = 5
# print(x[2])
# ----------------------------------------

# เพิ่มข้อมูลใหม่เข้าไปใน list 

# x.append("best")
# x.append(500)
# print(x)

# e = 100
# x.append(e)

# print(x)

# ---------------------------------
# ลบข้อมูลออกจาก list 
# x.pop(1)
# print(x)

# ---------------
# เพิ่มเติม
# x.remove("gun")
# print(x)

# x.clear()
# print(x)
# --------------

# for loop and list 
# for i  in x:
#     if i == 2 :
#          print(i)
# --------------------------

# dict_a = {
#     "A" : 80,
#     "B" :70,
#     "sword" : 100,
#     "gun" : 300
# }
# # dict_a["gun"] = 70  แก้ไขค่าในคีย์
# print(dict_a)
# # print(dict_a["gun"]) ค้นห่าค่าในคีย์

# # dict_a["bow"] =  40 เพิ่มเติมค่าใน key 
# # print(dict_a)

# manager_list = [
#         {"name" : "Gun" , "ig" : "Jgun" , "number" :"001"},
#         {"name" : "netnogame" , "ig" : "zzg" , "number" :"002"},
#         {"name" : "Peezeedjeezjardd" , "ig" : "PInwZa" , "number" :"003"}
# ]

# for i  in manager_list:
#     print(i["name"])

def checkmonney (list_of_students):
    for student in list_of_students:
        if student["money"] > 500 :
            return "เงินมากกว่า 500 "
        else :
            return "เงินน้อยกว่า 500"
student = [
    {"name" : "Pangpong",  "money" : 400},
    {"name" : "Ton",  "money" : 1000},
    {"name" : "P", "money" : 10000000},
    {"name" : "Pin", "money" : 1000000000000000000}

]
checkmonney(student)
print (student[2])