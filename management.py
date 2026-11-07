import json
import os

Data_File = "students.json"

def load_data():
    if not os.path.exists(Data_File):
        return{}
    try:
        with open(Data_File, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return{}

def save_file(data):
    with open(Data_File, "w") as file:
        json.dump(data,file,indent=4)

def create_data(data):
    print("\n Create New Data")
    stu_id = int(input("Enter Your ID :"))
    if stu_id in data:
        print(f"\n Already {stu_id} ID id exists, create new ID.")
        return
    
    name = input("Enter Your Name :").strip()
    age = input("Enter Your Age :").strip()
    email = input("Enter Your Email-ID :").strip()
    data[stu_id] = {
        "name" : name,
        "age" : age,
        "email" : email
    }
    save_file(data)
    print(f"Student {name} is added successfully.")

def read_file(data):
    print("\n View Student Data")
    stu_id = int(input("Enter Your ID :"))
    if stu_id in data:
        found = data[stu_id]
        print(f"Student ID : {found}")
        print(f"Student Name : {found["name"]}")
        print(f"Student Email-ID : {found["email"]}")
    else:
        print(f"Student ID {stu_id} is not found.")

def update_data(data):
    print("\n Update Student Data")
    stu_id = int(input("Enter Your ID :"))
    if stu_id in data:
        studentid = data[stu_id]
        Sname = input(f"Enter Update Name {studentid["name"]} :").strip()
        Sage = input(f"Enter Update Age {studentid["age"]} :").strip()
        Semail = input(f"Enter Update Email-ID {studentid["email"]} :").strip()
        if Sname:
            studentid["name"] = Sname
        if Sage:
            studentid["age"] = Sage
        if Semail:
            studentid["email"] = Semail
        data[stu_id] = studentid
        save_file(data)
        print(f"\n Student ID {stu_id} data is updated successfully.")
    else:
        print(f"Student ID {stu_id} is not found.")

def delete_data(data):
    print("\n Delete Student Data")
    stu_id = int(input("Enter Your ID :"))
    if stu_id in data:
        confirm = input(f"Are You Sure To Delete ID {stu_id} Data (Y/N) :").lower()
        if confirm == "y":
            del data[stu_id]
            save_file(data)
            print("Student data is deleted successfully.")
        else:
            print("Delete Process Will Cancelled.")
    else:
        print(f"This ID {stu_id} is not found.")

def main():
    student_data = load_data()

    while True:
        print("\n ------------------------------")
        print("\n Student Management System")
        print("1. Create New Student Data")
        print("2. View Student Data")
        print("3. Update Student Data")
        print("4. Delete Student Data")
        print("5. Exit")

        choice = int(input("Enter Your Choice (1-5) :"))
        if choice == 1:
            create_data(student_data)
        elif choice == 2:
            read_file(student_data)
        elif choice == 3:
            update_data(student_data)
        elif choice == 4:
            delete_data(student_data)
        elif choice == 5:
            print("Thank You For Use This System.")
            break
        else:
            print(f"Invalid Choice {choice}, Enter Between (1-5).")

if __name__ == "__main__":
    main()