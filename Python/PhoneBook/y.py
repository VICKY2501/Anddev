import datetime

class data:
    def __init__(self, contact, name, address, note):
        self.contact = contact
        self.name = name
        self.address = address
        self.note = note
        
    def getDetails(self):
        return f"{timeStamp()}\nName: {self.name}\nContact: {self.contact}\nAddress: {self.address}\nNote: {self.note}\n\n"
    

def timeStamp():
    dd = datetime.datetime.today().day
    mm = datetime.datetime.today().month
    yy = datetime.datetime.today().year
    
    t = datetime.datetime.now().strftime("[%H:%M:%S]")
    return f"{t}  {dd:02d}.{mm:02d}.{yy:02d}"

def lineNumber():
    lines = sum(1 for i in open('Dairy.txt'))
    return lines

def searchByName(name):
    lineNo = 0
    with open("Dairy.txt") as f:
        for l, d in enumerate(f, 1):
            if name.lower() in d.lower():
                lineNo += l
    
    print("DATA FETCHED: \n")
    with open("Dairy.txt") as f:
        for search, data in enumerate(f, 1):
            for i in range(-2, 4):
                if search == lineNo + i:
                    print(f"{data}")
                    
                    
def searchByContact(contact):
    lineNo = 0
    with open("Dairy.txt") as f:
        for l, d in enumerate(f, 1):
            if contact in d:
                lineNo += l
    
    print("DATA FETCHED: \n")
    with open("Dairy.txt") as f:
        for search, data in enumerate(f, 1):
            for i in range(-3, 2):
                if search == lineNo + i:
                    print(f"{data}")
                    
                    
def searchByRecordNo(recordNo):
    find = f"Record No.: {recordNo}"
    lineNo = 0
    with open("Dairy.txt") as f:
        for l, d in enumerate(f, 1):
            if find in d:
                lineNo += l
    
    print("DATA FETCHED: \n")
    with open("Dairy.txt") as f:
        for search, data in enumerate(f, 1):
            for i in range(0, 6):
                if search == lineNo + i:
                    print(f"{data}")
            

# driver code
print("PhoneBook Diary\n".upper())

while True:
    option = int(input("1. Add\n2. Open\n3. Exit\nSelect any option: "))

    if option == 1:
        no_of_records = int(input("Enter the number of records to be added = "))
        for i in range(0, no_of_records):
            if no_of_records > 1:
                print(f"Enter details of Record {i+1}\n")
            
            contact = input("Enter the Contact number = ")
            while len(contact) != 10:
                print("ERROR: PLEASE ENTER A VALID NUMBER")
                contact = input("Enter the Contact number = ")
                
            name = input("Enter Name = ")
            address = input("Enter address = ")
            note = input("Enter note if any = ")
            record = data(contact, name, address, note)
            
            with open("Dairy.txt",'a') as f:
                f.write(f"Record No.: {int(lineNumber()/6 + 1)}\n")
                f.write(record.getDetails())
                print("Data Successfully added\n".upper())
                
    if option == 2:
        choice = int(input("\n1. Show All records\n2. Search\n3. Exit\nSelect any option: "))
        if choice == 1:
            print("\nAvailable Records: \n")
            with open("Dairy.txt", 'r') as f:
                f.seek(0)
                print(f.read())
        elif choice == 2:
            searchby = int(input("\nSearch by:\n1. Name\n2. Contact\n3. Record Number\nSelect any option: "))
            if searchby == 1:
                name = input("\nEnter Name of the record you want to search = ")
                searchByName(name)
            elif searchby == 2:
                contact = input("\nEnter Contact of the record you want to search = ")
                # checks if contact is valid
                while len(contact) != 10:
                    print("ERROR: PLEASE ENTER A VALID NUMBER")
                    contact = input("Enter Contact of the record you want to search = ")
                
                searchByContact(contact)
            elif searchby == 3:
                recordNo = int(input("\nEnter the record No. = "))
                searchByRecordNo(recordNo)

            else: print("Choose a valid option\n")
        elif choice == 3:
            print("Exiting...")
            exit()
                
    if option == 3:
        print("Exited".upper())
        exit()

    