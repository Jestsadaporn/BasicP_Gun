# # กิจกรรมตั๋วหนัง 
# # ---------------
# # Key : ตั๋วหนังต้องแสดง ชื่อหนัง พากษ์ไทย / soundtrack ราคา

# # Prosess : แบ่งการทำงานสองส่วน ระบบแสดงผล , ระบบซื้อตั๋วหนัง
# #  ระบบแสดงผล -> ต้องดึงออกมาจากระบบส่วนกลาง ดึงข้อมูลเพื่อมาใช้แสดงผล {ใช้ def} (ใข้ lopp ดึงมาทีละตัว) print(ourmoive[0])
# #  ระบบซื้อตั๋ว -> อ้างอิงราคาจากส่วนกลาง ต้องใช้ if elif กรองผู้ใช้ว่าจะดูหนังเรื่องนั้นได้มั้ย เลือกภาษา เช็ค if ว่าเป็นหนังแนวอะไร


# # ระบบส่วนกลาง : เก็บชื่อหนัง ประเภทหนัง เรท  ภาษาที่มี ราคาเริ่มต้น(กรณีที่ไม่ใช่ fantacy)
# ourmoive = [
#     {"name" : "Oppenheimer ", "type" :"Drama", "language" :"Thai , Soundtrack" , "rate" : "R" ,"prize" :" 140 B " },
#     {"name" : "Dune part one ", "type" :"Sci-fi", "language" :"Thai , Soundtrack" ,"rate" : "G" , "prize" :" 140 B " },
#     {"name" : "Avatar fire and ash", "type" :"fatacy", "language" :"Soundtrack" ,"rate" : "G" , "prize" :" 190 B " },
#     {"name" : "F1", "type" :"action", "language" :" Soundtrack " ,"rate" : "G" , "prize" :" 140 B " },
#     {"name" : "เชย", "type" :"romance", "language" :"Thai , Soundtrack" ,"rate" : "G" , "prize" :" 140 B " }
#     ]

# def showourmoive():
#     print(" ")
#     print ("We have moive :")
#     print("<<---------------->>")
#     print(" ")
#     for i in range(5) :
#         print(ourmoive[i])
#         print("-----------")
# # ------------------------------
# def buyticket():

#     def moivesystem():
#         ageuser = input(("check your age plz input age >> "))
#         langofmoive = input("thai(1) or Soundtrack(2) ")
#         if langofmoive == 1 :
#             langofmoive == "thai"
#         elif langofmoive == 2 :
#             langofmoive == "Soundtrack"
#         else :
#             print("error")

#     def processlogic (userCmoive):
#         if userCmoive == "Oppenheimer" :
#             print ("-> you will buy ticket moive Oppenheimer ")
#             print(ourmoive[0])
#             moivesystem()
#             if ageuser < "20" :
#                 print("you can not watch this")
#             else:
#                 print("your ticket : ")
#                 print("----------------")
#                 print(ourmoive[0]["name"], langofmoive , ourmoive[0]["prize"])
#         elif userCmoive == "Dune part one " :
#             print(ourmoive[1])
#             moivesystem()
#             print("your ticket : ")
#             print("----------------")
#             print(ourmoive[1]["name"], langofmoive , ourmoive[1]["prize"])

#         elif userCmoive == "Avatar fire and ash" :
#             print(ourmoive[2])
#             moivesystem()
#             print("your ticket : ")
#             print("----------------")
#             print(ourmoive[2]["name"], langofmoive , ourmoive[2]["prize"])
#         elif userCmoive == "F1" :
#             print(ourmoive[3])
#             moivesystem()
#             print("your ticket : ")
#             print("----------------")
#             print(ourmoive[3]["name"], langofmoive , ourmoive[3]["prize"])
#         elif userCmoive == "เชย" :
#             print(ourmoive[4])
#             moivesystem()
#             print("your ticket : ")
#             print("----------------")
#             print( ourmoive[4]["name"], langofmoive , ourmoive[4]["prize"])
        

        
#     print("what moive do you want to do")
#     moive = input("input Name of moive ->>> ")
#     processlogic()
 
# # ------------------------------
# showourmoive()
# buyticket()

