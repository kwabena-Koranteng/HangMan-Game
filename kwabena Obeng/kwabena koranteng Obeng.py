import os
def main():
    os.path.exists("file.txt")
    if os.path.exists("fil.txt")==True:
         filename = open("file.txt","a")
        
    else:
        print("File does not exist ")
   
    class Attendee:
        def __init__(self,name,company,state,email):
            self.name=name
            self.company=company
            self.state=state
            self.email=email
            
        def getname(self):
            return self.name
        
        def getcompany(self):
            return self.company
        
        def getemail(self):
            return self.email
        
        def getstate(self):
            return self.state
        
        def attendee_save(self):
            file=open("file.txt","a")
            attendeeinfo= self.getname() + '  ' + self.getcompany() + '   ' + self.getemail() + '  ' + self.getstate()
            print(attendeeinfo,file=file)
            file.close()
        
    print("\n Menu")
    print("(1) Add an attendee")
    print("(2) Display information on an attendee")
    print("(3) Delete an attendee")
    print("(4)List all attendees")
    print("(5) List all attendees from a state")
    f=open("file.txt","r")
    lista=[]
    for i in f:
        a=i.split()
        print(a)
        lista.append(Attendee(a[0],a[1],a[2],a[3]))
    
    
    choice=eval(input("\n Select 1-5: "))
    if choice==1:
        name=input("\n Enter the name of the attendee: ")
        company=input("\n Enter the name of the company: ")
        state=input("\n Enter the name of the state: ")
        email=input("\n Enter your email: ")
        attendee = Attendee(name,company,state,email)
        attendee.attendee_save()
        lista.append(attendee)
    elif choice==2:
        filename=open("file.txt","r")
        whichattendee = input("Which attendee? <Enter name of attendee>" )
        l=filename.readlines()
        found=False
        for i in l:
            a=i.split()
            if a[0]==whichattendee:
                print(a[0] + ' ' + a[2])
                found=True
        if not found:
            print("Name was not found")
                
            
    elif choice==3:
        whichattendee=input("Which attendee?<Enter the name you want to delete: >")
        found=False
        for i in lista:
            if i.name==whichattendee:
                lista.remove(i)
                break
                found=True
                
        filename=open("file.txt","w")
        for i in lista:
            print(i.name,i.company,i.email,i.state,file=filename)
        filename.close()
    elif choice ==4:
        filename=open("file.txt","r")
        l=filename.readlines()
        for i in l:
            a=i.split()
            lista.append(a)
            print(a[0],a[-1])       
            
    elif choice==5:
        filename=open("file.txt","r")
        whichattendee = input("Which state? <Enter state>" )
        l=filename.readlines()
        found=False
        for i in l:
            a=i.split()
            if a[3]==whichattendee:
                print(a[0])
                found=True
                #break

        if not found:
            print("Name was not found")
        
            
    
main()