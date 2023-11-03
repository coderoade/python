names=[]
phone_numbers = []
total = 2


for i in range(total):
    name = input("Name: ")
    phone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")

for i in range(total):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\nEnter search term: ")

print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

else:
    print("Name Not Found")



addition_contact = input("Enter the contact you want to  add\n")
addition_number=input("enter the number you want to enter\n")
addition = names.append(addition_contact)
addition1=phone_numbers.append(addition_number)

print(names)
print(phone_numbers)
    


deletion_element = input("enter the contact you want to delete")
deletion_number=input("Enter the number you want to  delete")

if deletion_element  in names:

    deletion = names.remove(deletion_element)
    

    if deletion_number in phone_numbers:
         deletion1 = phone_numbers.remove(deletion_number)


else: print("none")
        



print("The contacts are", names) 
print("The phone numbers are ", phone_numbers)
         

    






        