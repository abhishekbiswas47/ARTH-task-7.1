import os

while True:
 os.system("clear")

 os.system("tput setaf 3")
 print("\t\t\tWelcome to my LVM Partition Menu !!")
 os.system("tput setaf 7")
 print("\t\t\t-----------------------------------")


 print("""
 \n
 Press 1: To create pv.
 Press 2: To create vg.
 Press 3: To create lv.
 Press 4: To extend the size of lv.
 Press 0: To exit.
 """)
 os.system("tput setaf 14")
 ch = input('Enter your choice: ')
 os.system("tput setaf 15")

 if '1' in ch:
   fdisk = os.system('sudo fdisk -l')
   print(fdisk)
   hdname = input('Enter the hardisk name: ')
   pv = os.system('sudo pvcreate {}'.format(hdname))
   print(pv)
   print('PV has been created successfully!!!')
   choice = input('Enter "d" to see the list of all the PV: ')
   if 'd' in choice:
     pvdisplay = os.system ('pvdisplay')
     print(pvdisplay)
   else:
     print('Wrong choice!!!')
 if '2' in ch:
   hdname = input('Enter the hardisk name whose pv is already created: ')
   vgname = input('Enter Vgname: ')
   vg = os.system('sudo vgcreate {}  {}'.format(vgname,hdname))
   print(vg)
 if '3' in ch:
   vgname = input('Enter Vgname from which you want to create LV: ')
   lvname = input('Enter LVname: ')
   lvsize = input('Enter the size of LV in G/M: ')
   os.system('sudo lvcreate --size {} --name {} {}'.format(lvsize,lvname,vgname))
   os.system('sudo mkfs.ext4 /dev/{}/{}'.format(vgname,lvname))
   print("Do you want to mount it? y/n")
   chr = input()
   if 'y' in chr:
       dir = input('Enter a name to create a directory  for mounting to lv: ')
       directory = os.system('sudo mkdir /{}'.format(dir))
       print(directory)
       os.system('sudo mount /dev/{}/{}  /{}'.format(vgname,lvname,dir))
   if 'n' in chr:
       exit()
   df = os.system('df -hT')
   print(df)
 if '4' in ch:
   size = input('Enter the size to increase(+) with G/M: ')
   lvdisplay =  os.system('lvdisplay')
   print(lvdisplay)
   lvm = input('Enter the lv name: ')
   os.system('lvextend --size {} /dev/{}'.format(size,lvm))
   os.system('sudo resize2fs {}'.format(lvm))
   dfht = os.system('df -hT')
   print(dfht)
 if '0' in ch:
     exit()

 input("Enter any Key to continue: ")
