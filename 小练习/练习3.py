#Author:ZJF
import time
a = time.localtime()
mon_list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
print(a)
print(a[1])
print("current date and time is",mon_list[a[1]],time.strftime(" %d , %Y %H:%M:%S",a))
