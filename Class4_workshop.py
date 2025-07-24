# กิจกรรมตั๋วหนัง 
# ---------------
# Key : ตั๋วหนังต้องแสดง ชื่อหนัง พากษ์ไทย / soundtrack ราคา

# Prosess : แบ่งการทำงานสองส่วน ระบบแสดงผล , ระบบซื้อตั๋วหนัง
#  ระบบแสดงผล -> ต้องดึงออกมาจากระบบส่วนกลาง ดึงข้อมูลเพื่อมาใช้แสดงผล {ใช้ def}
#  ระบบซื้อตั๋ว -> อ้างอิงราคาจากส่วนกลาง ต้องใช้ if elif กรองผู้ใช้ว่าจะดูหนังเรื่องนั้นได้มั้ย เลือกภาษา เช็ค if ว่าเป็นหนังแนวอะไร


# ระบบส่วนกลาง : เก็บชื่อหนัง ประเภทหนัง เรท  ภาษาที่มี ราคาเริ่มต้น(กรณีที่ไม่ใช่ fanta)
def moiveshow ():
    print("welcome to our cinema  this is our movive us have")


def moivelist():
    ourmoive = [
        {"name" : "Oppenheimer ", "type" :"Drama", "language" :"Thai , Soundtrack" , "prize" :" 140 B " }
        {"name" : "Dune part one ", "type" :"Sci-fi", "language" :"Thai , Soundtrack" , "prize" :" 140 B " }
        {"name" : "Avatar fire and ash", "type" :"d", "language" :"Thai , Soundtrack" , "prize" :" 140 B " }
        {"name" : "Oppenheimer", "type" :"drama", "language" :"Thai , Soundtrack" , "prize" :" 140 B " }
        {"name" : "Oppenheimer", "type" :"drama", "language" :"Thai , Soundtrack" , "prize" :" 140 B " }
    ]
moiveshow()





