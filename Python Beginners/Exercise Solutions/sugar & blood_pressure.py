def No_of_Entries():
    print("Enter your details:")
    name = input("Name: ")
    id = int(input("ID: "))
    age = int(input("Age: "))

    print("Select one of the following services:")
    print("1. blood_pressure")
    print("2. sugar_level")
    print("3. Both")

    option = input("Enter the number of your choice: ")

    if option == "1":
        print("Blood Pressure Check")

        systolic = int(input("Enter your systolic pressure: "))
        diastolic = int(input("Enter your diastolic pressure: "))

        if systolic < 90 or diastolic < 60:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your blood pressure is low.")
        elif systolic < 120 and diastolic < 80:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your blood pressure is normal.")
        elif systolic < 130 and diastolic < 80:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your blood pressure is elevated.")
        elif systolic < 140 and diastolic < 90:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your blood pressure is stage 1 hypertension.")
        else:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your blood pressure is stage 2 hypertension. Consult a doctor.")
    elif option == "2":
        print("Sugar Level Check")

        sugar_level = int(input("Enter your sugar level: "))

        if sugar_level < 80:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your sugar level is low.")
        elif sugar_level > 100:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your sugar level is high.Consult a doctor.")
        else:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your sugar level is normal")

    elif option == "3":
        print("You selected Both!")
        print("Sugar Level Check")
        sugar_level = int(input("Enter your sugar level: "))

        if sugar_level < 80:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your sugar level is low.")
        elif sugar_level > 100:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your sugar level is high.Consult a doctor.")
        else:
            print(f"Name: {name}, ID: {id}, Age: {age}")
            print("Your sugar level is normal")
            print("---------------------")
            
        print("Blood Pressure Check")
        systolic = int(input("Enter your systolic pressure: "))
        diastolic = int(input("Enter your diastolic pressure: "))

        if systolic < 90 or diastolic < 60:
            print("Your blood pressure is low.")
        elif systolic < 120 and diastolic < 80:
            print("Your blood pressure is normal.")
        elif systolic < 130 and diastolic < 80:
            print("Your blood pressure is elevated.")
        elif systolic < 140 and diastolic < 90:
            print("Your blood pressure is stage 1 hypertension.")
        else:
            print("Your blood pressure is stage 2 hypertension. Consult a doctor.")
    else:
        print("Invalid option. Please select a valid number.")
def output(n):
    try:
        for i in range(n):
            No_of_Entries()
    except Exception as e:
        print(f"An error occurred: {e}")
    return
tell = int(input('How Many Patients: '))
output(tell)
