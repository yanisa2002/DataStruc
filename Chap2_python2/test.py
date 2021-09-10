Input = 'Mr.Xz Yz,Age:21'
if Input.split('.')[0] == 'Mr': 
    Gender = 'Man'
else:
    Gender = 'Woman'
#ได้เพศละ ต่อไปก็ หาชื่อ
Fname = Input.split('.')[1].split(' ')[0] #เนื่องจากเราได้แบ่งด้วย'.' ตอนแรก เราก็จะได้'Xz Yz,Age:21' เราก็ต้องนำมาแบ่งหาอีก โดยสามารถ.split ต่อได้เลย
Lname = Input.split(' ')[1].split(',')[0]
Age = Input.split(':')[-1]
#ลองมา print ดูว่าถูกต้องหรือเปล่า
print('Gender = %s\nFname = %s\nLname = %s\nAge = %s' % (Gender, Fname, Lname, Age))