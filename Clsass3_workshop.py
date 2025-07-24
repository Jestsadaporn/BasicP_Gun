# เงื่อนไขซ้อนเงื่อนไข
# hasrice = True
# hasspoon = False

# if hasrice :
#     print ("มีข้าว")
#     if hasspoon :
#         print("มีช้อน")
#         print("กินข้าวได้")
#     else :
#         print("กินข้าวไม่ได้เพราะไม่มีช้อน")
    
# else :
#     print("กินไม่ได้ไม่มีข้าว")

# for loop 

# for i in range(2,22,2) :
#     print(i)

# for i in range(1,5,1):
#     print("hello_สวัสดี", i)

# โปรแกรมคำนวณผลรวม
# box = 0
# for i in range(10):
#     box = box+i
#     print(box)  

# print ("ค่าของ box : ", box)

# round = int(input("วนกี่รอบ :"))
# Start = 0
# for i in range (1,round+1,1) :
#     Start += i
#     print("รอบที่",i,"ผลรวมคือ" , Start )


#while loop 
# i = 0 
# while i < 5 :
#     print("hello")
#     i += 1 

# while True :
#    inp = int(input("input number : "))
#    if inp == 7 :
#       break
     
# i = 0 
# while i<5  :
#     i+=1
#     print(i)

print("plz create HP of monster ")
HPmonster = int(input("HP : "))
print ("plz create 3 power of atttools")
powerof_att1 = int(input("Power att of 1 atttools : "))
powerof_att2 = int(input("Power att of 2 atttools : "))
powerof_att3 = int(input("Power att of 3 atttools : "))



while int(input("fight what do you want to do fight (1) of exit(2) ")) != 2:

            Round = int(input("input round do you want to fight"))

            if HPmonster > 0 :
                for i in range (Round):

                    print("input atttools for round ",i+1 )

                    choseWep = int(input(" : "))
                    if choseWep == 1 :
                            HPmonster = HPmonster-powerof_att1
                            print ("you hit monster :" , powerof_att1 , "now monster HP " , HPmonster  )
                            if HPmonster == 0 :
                                print("monster die")
                                breakpoint
                            elif HPmonster < 0  :
                                print ("monter have Hp 20")
                                HPmonster = 20
                                    
                            elif 0 < HPmonster:
                                print("fihght next round")
                                     

                    elif choseWep == 2 :
                            HPmonster = HPmonster-powerof_att2
                            print ("you hit monster :" , powerof_att2 , "now monster HP " , HPmonster  )
                            if HPmonster == 0 :
                                print("monster die")
                                breakpoint

                            elif HPmonster < 0  :
                                print ("monter have Hp 20")
                                HPmonster = 20
                            elif 0 < HPmonster:
                                print("fihght next round")
                             

                    elif choseWep == 3 :
                            HPmonster = HPmonster-powerof_att3
                            print ("you hit monster :" , powerof_att3 , "now monster HP " , HPmonster  )
                            if HPmonster == 0 :
                                print("monster die")
                                # breakpoint

                            elif HPmonster < 0  :
                                print ("monter have Hp 20")
                                HPmonster = 20
                            elif 0 < HPmonster:
                                print("fihght next round")

                    else :
                         print("error input choseWep")

                if HPmonster > 0 :
                    print("you die")
