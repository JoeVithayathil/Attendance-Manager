#Prototype 76



import requests
from bs4 import BeautifulSoup
import string
import socket
import os
from lxml import html
import time
from tabulate import tabulate
from datetime import datetime
from datetime import date,timedelta





#To check for internet connection
def i_connect():
   try:
      host=socket.gethostbyname("www.google.com")
      s=socket.create_connection((host, 80), 10)
   except:
      print("\n\n\n\n\t\tNo internet connection. Try again later.")
      exit()



#To Enter details of new user
def det_new_user(uid,pas):
   i_connect()
   os.system('cls')
   d=datetime.date(datetime.now())
   y=d.year
   payload={'user':uid,'pass':pas}
   with requests.Session() as s:
      p=s.post('https://www.rajagiritech.ac.in/stud/parent/varify.asp', data=payload)
      q=s.get('https://www.rajagiritech.ac.in/stud/KTU/Parent/Home.asp')
      r=s.get('https://www.rajagiritech.ac.in/stud/KTU/Parent/Leave.asp')
   soup=BeautifulSoup(q.text,"lxml")
   l=[] 
   for i in soup.findAll('strong'):
      l.append(i.text)
   name=str(l[0])
   print("\t\t\tWELCOME ",name," TO 76.")
   os.system('cls')
   soup=BeautifulSoup(r.text,"lxml")
   l=[] 
   for i in soup.findAll('option'):
      l.append(i.text)
   print("\n\nSelect your class code:\n")
   for i in range(len(l)):
      print (i+1,": ",str(l[i]))
   c=-1
   print 
   while c<0 or c>len(l):
      c=input("Enter Your option: ")
   code=str(l[c-1])
   if string.upper(conf)=='Y':
      t=(uid,pas,code)
      f1=open(uid+".txt","w")
      f1.write(uid+"\n")
      f1.write(code+"\n")
      s_limit='0'
      while s_limit<'75' or s_limit>'100':
         s_limit=raw_input("\nEnter a safe limit value(>75): ")
      f1.write(s_limit+"\n")
      f1.write("")
      f1.close()
      return t
   else:
      login_()



#To check if user has previously loged in or not
def check_user(u,p):
   i=0
   l=[]
   l2=[]
   code=""
   f=open(u+".txt","r")
   i=0
   while True:
      l=f.readline()
      if not l:
         break
      else:
         l2.append(l)
         i=i+1
   if i<8:
      t=det_new_user(u,p)
   else:
      c=l2[1]
      for i in range(0,len(c)-1):
         code=code+c[i]
      t=(u,p,code)
   return t   
   f.close()
   




#To login
def login_():
   fl=0
   while True:
      while True:
         os.system('cls')
         if fl==1:
            print ("\n\n\n\t\tWrong Login ID or Password.")
         else:
            pass
         uid=raw_input("\n\n\n\n\t\tUser ID  : ")
         uid=string.upper(uid)
         pas=raw_input("\n\n\t\tPassword : ")
         con='x'
         payload={'user':uid,'pass':pas}
         while string.upper(con)!='Y' and string.upper(con)!='N':
            con=raw_input("\n\n\t\tConfirm(Y/N): ")
         if string.upper(con)=='Y':
            break
         else:
            pass
      with requests.Session() as s:
         i_connect()
         p=s.post('https://www.rajagiritech.ac.in/stud/parent/varify.asp', data=payload)
      u='https://www.rajagiritech.ac.in/stud/KTU/Parent/Home.asp'
      if p.url==u:
         break
      else:
         fl=1
   t=check_user(uid,pas)
   return t
         

      
         
      
#To Enter the time table
def time_table(u,code,ls,lc,number=[0,1,2,3,4,5,6],dt={}):
   os.system('cls')
   ld=[]
   t_t={}
   t_table={}
   ldays=['Monday','Tuesday','Wednesday','Thursday','Friday']
   f=open(u+'.txt','a')
   f2=open(code+'.txt','a')
   print ("Enter Time Table:\n(Enter the subject code)\n")
   for i in number:
      print ("\n\n",ldays[i],":")
      print
      ld=[]
      for j in range(len(ls)):
         print (ls[j]," = ",lc[j])
      print
      for j in range(7):
         print (j+1,": ",)
         s1=raw_input()
         s1=string.upper(s1)
         while True:
            if s1 not in lc:
               print("\nInvalid Subject code\n")
               print (j+1,": ",)
               s1=raw_input()
               s1=string.upper(s1)
            else:
               ld.append(s1)
               break
         else:
            print ("Invalid Subject code")
      dt[i]=ld
   os.system('cls')
   print ("\n\nTime Table:")
   print ("---------- \n")
   k=0
   for i in range(7):
      l=[]
      for j in range(5):
        l.append(dt[j][i])
      t_t[i]=l
   t_table={"Day/Period":[] ,1:[] ,2:[] ,3:[] ,4:[] ,5:[] ,6:[] ,7:[]}
   t_table["Day/Period"]=ldays
   t_table[1]=t_t[0]
   t_table[2]=t_t[1]
   t_table[3]=t_t[2]
   t_table[4]=t_t[3]
   t_table[5]=t_t[4]
   t_table[6]=t_t[5]
   t_table[7]=t_t[6]
   print(tabulate(t_table,headers="keys",tablefmt="fancy_grid",stralign="center",numalign="center"))
   con='s'
   while string.upper(con)!='Y' and string.upper(con)!='N':
      con=raw_input("\n\nConfirm(Y/N): ")
   if string.upper(con)=='Y':
      for i in range(5):
         for j in range(7):
            f.write(dt[i][j])
            f2.write(dt[i][j])
            f.write(",")
            f2.write(",")
         f.write("\n")
         f2.write("\n")
      f.close()
      f2.close()
   else:
      os.system('cls')
      f.close()
      print() 
      print("1. All")
      for i in range(len(ldays)):
         print(i+2,". ",ldays[i])
      print("Enter your option of days where time table has to be changed: ")
      i=0
      number=[]
      while True:
         while True:
            n=input()
            if n in range(1,9):
               if n not in number:
                  number.append(n)
               break
            else:
               print("Invalid input")
         print()
         con='s'
         while string.upper(con)!='Y' and string.upper(con)!='N':
            con=raw_input("\n\nAnymore(Y/N): ")
         if string.upper(con)=='N':
            break
      time_table(u,code,ls,lc,number,dt)
          
   





#Program to execute logging in and scraping of data   
def login_scrape(soup,code):
   os.system('cls')
   l = [] 
   for i in soup.findAll('b'):
      l.append(i.text)
   i=0
   lsub = []
   while l:
      if l[i]=='Name':
         break
      else:
         i=i+1
   i=i+1        
   while l[i]!='Date/Hours':
      lsub.append(str(l[i]))
      i=i+1
   l2=[]
   for i in soup.findAll('td'):
      l2.append(i.text)    
   i=0
   while l2:
      if l2[i]=='Name':
         break
      else:
         i=i+1
   i=i+1
   l3=[]
   while l2[i]!=uid:
      l3.append(l2[i])
      i=i+1
   i=0
   l4=[]
   for i in range (0,len(l3)):
      st1=''
      st2=l3[i]
      j=len(lsub[i])
      for k in range(j,len(l3[i])):
         st1=st1+st2[k]
      l4.append(st1)
   lcode=[]
   for i in range (0,len(l4)):
      st1=''
      st2=l4[i]
      for j in range(0,len(l4[i])):
         if st2[j]=='[':
            break
         else:
            st1=st1+st2[j]
      lcode.append(str(st1))
   lt_clas=[]
   for i in range(0,len(l4)):
      st1=''
      st2=l4[i]
      fl=0
      for j in range(len(l4[i])):
         if st2[j]=="[":
            fl=1
         else:
            pass
         if fl==1:
            st1=st1+st2[j]
      t1=int(filter(str.isdigit, str(st1)))
      lt_clas.append(t1)
   l5=[]
   for i in soup.findAll('strong'):
      l5.append(i.text)
   la_clas=[]
   for i in range(0,len(l5)):
      t1=int(filter(str.isdigit, str(l5[i])))
      la_clas.append(t1)
   f=open(uid+".txt","r")
   i=0
   while True:
      l=f.readline()
      if not l:
         break
      else:
         i=i+1
   if i==0 or i==3:
      f.close()
      f=open(uid+".txt","a")
      f2=open(code+'.txt','a')
      f2.close()
      f2=open(code+'.txt','r')
      i=0
      l2=[]
      while True:
         l=f2.readline()
         if not l:
            break
         else:
            l2.append(l)
            i=i+1
      if i==0:  
         t=time_table(uid,code,lsub,lcode)
      else:
         for i in range(len(l2)):
            f.write(l2[i])
            f.write("\n")
   else:
      pass
   f.close()
   t=(uid,lsub,lcode,lt_clas,la_clas)
   return t




#To print Time Table
def print_t_table(t):
   os.system('cls')
   print("\n\nTime Table:")
   print("---------- \n")
   ldays=['Monday','Tuesday','Wednesday','Thursday','Friday']
   t_table={}
   t_table={"Day/Period":[] ,1:[] ,2:[] ,3:[] ,4:[] ,5:[] ,6:[] ,7:[]}
   t_table["Day/Period"]=ldays
   t_table[1]=t[0]
   t_table[2]=t[1]
   t_table[3]=t[2]
   t_table[4]=t[3]
   t_table[5]=t[4]
   t_table[6]=t[5]
   t_table[7]=t[6]
   print(tabulate(t_table,headers="keys",tablefmt="fancy_grid",stralign="center",numalign="center"))


#To scrape the days of absentt
def scrape_abs(soup):
   l=[]
   d={}
   for i in soup.findAll('td'):
      l.append(i.text)
   c=0
   for i in range((len(l)-1),-1,-1):
      if l[i]=='7':
         break
      else:
         c=c+1
   i=len(l)-c
   l2=[]
   while i!=len(l):
      l2.append(str(l[i]))
      i=i+1
   for i in range(8):
      l=[]
      for j in range(i,len(l2),8):
         l.append(l2[j])
      d[i]=l
   print
   print(tabulate(d,headers=["Day","1","2","3","4","5","6","7"],tablefmt="fancy_grid",numalign="center",stralign="center"))
   



#To print attendance log   
def print_a_log(t,soup):
   os.system('cls')
   print("\n\nAttendance Log:")
   print("--------------\n")
   d={0:[],1:[],2:[],3:[],4:[]}
   d[0]=t[0]
   d[1]=t[1]
   d[2]=t[2]
   d[3]=t[3]
   l=[]
   for i in range(len(t[1])):
      p=float(d[2][i]-d[3][i])/d[2][i]
      p=p*100
      per="%.2f" % p
      l.append(per)
   d[4]=l
   print(tabulate(d,headers=["Subject","Subject Code","Total Classes","Total Absent","Percent"],tablefmt="fancy_grid",numalign="left"))
   scrape_abs(soup)
   



#To prnt number of leaves available
def leave_avail(t):
   os.system('cls')
   dic={}
   ls=t[0]
   lc=t[1]
   ltc=t[2]
   lac=t[3]
   lsa=[]
   lca=[]
   lp=[]
   s=t[4]
   for i in range(len(ls)):
      totc=ltc[i]
      tota=lac[i]
      lsa.append('0')
      lca.append('0')
      p=float((totc-tota)*100)/totc
      lp.append("%.2f" % p)
      per=0.0
      tempc=totc
      tempa=tota
      while True:
         tempc=tempc+1
         tempa=tempa+1
         per=float((tempc-tempa)*100)/tempc
         if per>s:
            lsa[i]=tempa-tota
            lca[i]=tempa-tota
         elif per>75:
            lca[i]=tempa-tota
         else:
            break
   dic[0]=lc
   dic[1]=ltc
   dic[2]=lac
   dic[3]=lp
   dic[4]=lsa
   dic[5]=lca
   print("\n\nLeave Available:")
   print("---------------" )
   print("\n\n")
   for i in range(len(ls)):
      print(ls[i]," = ",lc[i])
   print("\n\n")
   print(tabulate(dic,headers=["Subject Code","Total Classes(Current)","Total Absent(Cur.)","Percent(Cur.)","Leave available(Safe)","Leave available(KTU)"],tablefmt="fancy_grid",numalign="left"))
   
            
      
#To Find the day
def find_day(d):
   d=datetime.strptime(d, "%d/%m/%Y")
   day_name=d.strftime("%A")
   return day_name

#To find the differnce b/w two days
def dif_day(d1,d2):
    d1=datetime.strptime(d1, "%d/%m/%Y")
    d2=datetime.strptime(d2, "%d/%m/%Y")
    return abs((d2 - d1).days)

#To find differnce b/w today and the first day of leave
def dif_2day(d):
   l=d.split('/')
   d=''
   for i in range(2,-1,-1):
      d=d+l[i]
      if i!=0:
         d=d+'/'
   d1=datetime.strptime(d, "%Y/%m/%d")
   d2=datetime.date(datetime.now())
   d=str(d2)
   d2=datetime.strptime(d, "%Y-%m-%d")
   c=0
   d=d2
   while str(d)!=str(d1):
      d=d+timedelta(1)
      c=c+1
   c=c
   return c


#To check if date entered in valid
def cor_date(d1):
   fl=0
   try:
      d1=datetime.strptime(d1, "%d/%m/%Y")
      d2=datetime.date(datetime.now())
      if str(d1)<str(d2):
         print("Enter upcoming days")
      else:
         fl=1
   except ValueError:
      print("Invalid Input.")
   return fl

   
#To plan leave
def leave_plan(t,dic):
   os.system('cls')
   ls=t[0]
   lc=t[1]
   lsub=t[0]
   lt=t[2]
   totp=0
   la=t[3]
   ls_p=[]
   os.system('cls')
   l_date=[]
   d_cper={"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[]}
   l_day=[]
   d_c={}
   c=0
   dic_det={}
   l=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
   d_cday={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0}
   print("\n\nEnter the dates:")
   print("---------------\n")  
   while True:
      d=''
      d=raw_input("Enter date(DD/MM/YYYY): ")
      if len(d)==10:
         con='s'
         if cor_date(d)==1:
            if d not in l_date:
               l_date.append(d)
               c=c+1
         while string.upper(con)!='Y' and string.upper(con)!='N':
            con=raw_input("\nAnymore(Y/N): ")
         if string.upper(con)=='N':
            break
      else:
         print("Invalid date Entry")
      print
   l_date.sort()
   for i in range(len(lc)):
      dic_det[i]=[lc[i],lt[i],la[i]]
   for i in range(len(lc)):
      per=float((dic_det[i][1]-dic_det[i][2])*100)/dic_det[i][1]
      dic_det[i].append("%.2f" % per)
   dif=dif_day(l_date[0],l_date[len(l_date)-1])
   dif=dif+1
   for i in range(c):
      l_day.append(find_day(l_date[i]))
   day=l_day[0]
   z=0
   for i in range(7):
      if day==l[i]:
         break
      else:
         z=z+1
   for i in range(dif):
      if z==5 or z==6:
         pass
      else:
         d_cday[l[z]]=d_cday[l[z]]+1
      z=z+1
      if z==7:
         z=0
      else:
         pass
   for i in range(len(lc)):
      for j in range(5):
         count=0
         for k in range(7):
            if dic[j][k]==lc[i]:
               count=count+1
         d_cper[l[j]].append(count) 
   for i in range(len(lc)):
      count=0
      for j in range(5):
         count=count+(d_cper[l[j]][i]*d_cday[l[j]])
      ct=count+lt[i]
      dic_det[i].append(ct)
   d_cday={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0}
   for i in range(c):
      count=0
      for j in range(5):
         if l_day[i]==l[j]:
            count=count+1
      d_cday[l_day[i]]=count
   for i in range(len(lc)):
      count=0
      for j in range(5):
         count=count+(d_cper[l[j]][i]*d_cday[l[j]])
      ct=count+la[i]
      dic_det[i].append(ct)
   z=0
   dif=dif_2day(l_date[0])
   d_cday={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0}
   d1=str(datetime.date(datetime.now()))
   d2=d1.split("-")
   d1=""
   for i in range(2,-1,-1):
      d1=d1+d2[i]
      if i!=0:
         d1=d1+'/'
   day=find_day(d1)
   for i in l:
      if i==day:
         z=z+1
         break
      else:
         z=z+1
   for i in range(dif):
      if z==5 or z==6:
         pass
      else:
         d_cday[l[z]]=d_cday[l[z]]+1
      z=z+1
      if z==7:
         z=0
      else:
         pass
   for i in range(len(lc)):
      count=0
      for j in range(5):
         count=count+(d_cper[l[j]][i]*d_cday[l[j]])
      ct=count+lt[i]
      dic_det[i][4]=ct
   for i in range(len(lc)):
      per=float((dic_det[i][4]-dic_det[i][5])*100)/dic_det[i][4]
      dic_det[i].append("%.2f" % per)
   l=[]
   d={}
   for i in range(7):
      l=[]
      for j in range(len(lc)):
         l.append(dic_det[j][i])
      d[i]=l
   print
   for i in range(len(lc)):
      print(lc[i]," = ",ls[i])
   print()
   print(tabulate(d,headers=["Subject Code","Total Classes(Cur.)","Total Absent(Cur.)","Percentage(Cur.)","Total Classes","Total Absent","Percentage"],tablefmt="fancy_grid",numalign="left"))
   print("\n** The log is calcuated from tommorrow")
   
   



#To print pick up log
def pick_up_log(tup):
   os.system('cls')
   print("\n\nPick up log:")
   print("-----------\n")
   lsub=tup[0]
   lcode=tup[1]
   lt_clas=tup[2]
   la_clas=tup[3]
   d={}
   for i in range(len(lsub)):
      l=[]
      count=0
      l=[lsub[i],lcode[i],lt_clas[i],la_clas[i]]
      per=(float(lt_clas[i]-la_clas[i])*100.0)/lt_clas[i]
      l.append("%.2f" % per)
      while per<=75:
         count=count+1
         per=(float((lt_clas[i]+count)-la_clas[i])*100.0)/(lt_clas[i]+count)
      l.append(count)
      d[i]=l
   d2={}
   for i in range(6):
      d2[i]=[]
      for j in range(len(lsub)):
         d2[i].append(d[j][i])
   print(tabulate(d2,headers=["Subject","Subject Code","Total Classes","Total Absent","Percent","Req. Classes"],tablefmt="fancy_grid",numalign="left"))
         


   
#To erase previous inputs
def new_sem(uid):
   f=open(uid+".txt","w")
   f.close()



   
#main program starts here
while True:
   tup=login_()
   uid=tup[0]
   pas=tup[1]
   code=tup[2]
   payload={'user':uid,'pass':pas}
   with requests.Session() as s:
      i_connect()
      p=s.post('https://www.rajagiritech.ac.in/stud/parent/varify.asp', data=payload)
      q=s.get('https://www.rajagiritech.ac.in/stud/KTU/Parent/Leave.asp')
      t=s.get('https://www.rajagiritech.ac.in/stud/KTU/Parent/Leave.asp?code='+code)
   soup=BeautifulSoup(t.text,"lxml")
   tup=login_scrape(soup,code)
   uid=tup[0]
   lsub=tup[1]
   lcode=tup[2]
   lt_clas=tup[3]
   la_clas=tup[4]
   dt={}#stores data according to day
   t_t={}#stores data according to period number
   l=[]
   j=0
   k=0
   f=open(uid+".txt","r")
   while True:
      l=f.readline()
      if not l:
         break
      else:
         if j>=3:
            lp=l.split(",")
            lt=[]
            for i in range(0,7):
               lt.append(lp[i])
            dt[k]=lt
            k=k+1
         elif j==2:
            saf=int(filter(str.isdigit, str(l)))
         else:
            pass
         j=j+1
   for i in range(7):
      l=[]
      for j in range(5):
         l.append(dt[j][i])
      t_t[i]=l
   f.close()
   l=[]
   #os.system('cls')
   fl=0
   while True:
      tup=(lsub,lcode,lt_clas,la_clas,saf)
      print("\n\n\n1. Time Table")                #print_t_table(uid)
      print("2. Attendance Log")                  #print _a_log(tup)
      print("3. Number of leaves Available")      #leave_avail(tup,dt)
      print("4. Leave Planner")                   #leave_plan(tup,t_t)
      print("5. Classes required to keep up")     #pick_up_log(tup)
      print("6. New Semester")                    #new_sem(uid)
      print("7. Exit")
      ch=input("\nEnter your option: ")
      if ch==1:
         print_t_table(t_t)
      elif ch==2:
         print_a_log(tup,soup)
      elif ch==3:
         leave_avail(tup)
      elif ch==4:
         leave_plan(tup,dt)
      elif ch==5:
         pick_up_log(tup)
      elif ch==6:
         new_sem(uid)
         break
      elif ch==7:
         fl=1
         break
      else:
         print("\n\n\nInvalid Entry.")
   if fl==1:
      break

#Program Over!!!!!!!!
