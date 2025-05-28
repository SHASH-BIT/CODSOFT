#Dynamic programming in python
#TASK 1
#SIMPLE CALCULATOR
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
          
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Enter the operation(1/2/3/4):")

    if choice == '1':
       result = num1 + num2
       operation = "+"
    elif choice == '2':
         result = num1 - num2
         operation = "-"
    elif choice == '3':
         result = num1 * num2
         operation = "*"
    elif choice == '4':
      if num2!= 0:
         result = num1 / num2
         operation = "/"
      else:
         print("Error: Dividion by zero not allowed.")
         return
    else:
         print("Invalid input")
         return

    print(f"{num1}{operation}{num2} = {result}")
calculator()

OUTPUT(Simple Calculator)
Select operation:
1. ADD
2. SUBTRACT
3. MULTIPLY
4. DIVIDE
Enter first number:  50
Enter second number:  60
Enter the operation(1/2/3/4): 3
50.0*60.0 = 3000.0



#TASK 2
#PASSWORD GENERATOR
import random 
import string
def generate_password(length):
    if length < 4:
        print("Password Length should ber at least 4 characters.")
        return None

    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    password=[
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars=lower+ upper + digits + symbols
    password +=random.choices(all_chars,k=length-4)
    random.shuffle(password)
    return ''.join(password)

def display_password(password):
    if password :
        print(f"Generated Password :{password}")
try:
    user_input= int(input("Enter the desired password length: "))
    pwd= generate_password(user_input)
    display_password(pwd)
except ValueError:
    print("Please enter a valid number.")
	
	
OUTPUT(PassWord Manager)
Enter the desired password length: 4
Generated Password :3B\l


#TASK 3
#CONTACT BOOK MANAGER
import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def refresh_listbox():
    contact_listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        contact_listbox.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and phone:
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        refresh_listbox()
        clear_fields()
        messagebox.showinfo("Success", f"Contact '{name}' added.")
    else:
        messagebox.showwarning("Input Error", "Name and phone number are required.")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def on_select(event):
    if contact_listbox.curselection():
        index = contact_listbox.curselection()[0]
        selected = contacts[index]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        name_entry.insert(0, selected["name"])
        phone_entry.insert(0, selected["phone"])
        email_entry.insert(0, selected["email"])
        address_entry.insert(0, selected["address"])

def update_contact():
    if contact_listbox.curselection():
        index = contact_listbox.curselection()[0]
        contacts[index] = {
            "name": name_entry.get().strip(),
            "phone": phone_entry.get().strip(),
            "email": email_entry.get().strip(),
            "address": address_entry.get().strip()
        }
        refresh_listbox()
        messagebox.showinfo("Updated", "Contact updated successfully.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

def delete_contact():
    if contact_listbox.curselection():
        index = contact_listbox.curselection()[0]
        confirm = messagebox.askyesno("Confirm", f"Delete '{contacts[index]['name']}'?")
        if confirm:
            del contacts[index]
            refresh_listbox()
            clear_fields()
            messagebox.showinfo("Deleted", "Contact deleted.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone:")
    if keyword:
        results = [f"{i+1}. {c['name']} - {c['phone']}" for i, c in enumerate(contacts)
                   if keyword.lower() in c['name'].lower() or keyword in c['phone']]
        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Not Found", "No matching contacts found.")

# GUI setup
root = tk.Tk()
root.title("Contact Manager")

# Labels and Entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Address:").grid(row=3, column=0, sticky="w")

name_entry = tk.Entry(root, width=30)
phone_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)
address_entry = tk.Entry(root, width=30)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
address_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, pady=5)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=5, column=0, pady=5)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=1, pady=5)
tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=6, column=0, columnspan=2, pady=5)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, width=50)
contact_listbox.grid(row=0, column=2, rowspan=7, padx=10, pady=5)
contact_listbox.bind('<<ListboxSelect>>', on_select)

root.mainloop()
# This code creates a simple contact manager application using Tkinter.

OUTPUT(Contact Book)
===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 1
Enter name: Shashwata Datta
Enter phone number: 1234567890
Enter email: Sdatta@gmail.com
Enter address: 123 Main St
Contact 'Shashwata Datta' added.

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 1
Enter name: Sharmistha Datta
Enter phone number: 9876543210
Enter email: Shdatta@gmail.com
Enter address: 456 Elm St
Contact 'Sharmistha Datta' added.

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 2

Contact List:
1. Shashwata Datta - 1234567890
2. Sharmistha Datta - 9876543210

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 3
Enter name or phone to search: Sharmistha Datta

Found Contact:
Name: Sharmistha Datta
Phone: 9876543210
Email: Shdatta@gmail.com
Address: 456 Elm St

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 4

Contact List:
1. Shashwata Datta - 1234567890
2. Sharmistha Datta - 9876543210

Enter the contact number to update: 2
Updating contact: Sharmistha Datta
New name (Bob): Partha Datta
New phone (9876543210): 
New email (Shdatta@gmail.com): Pdatta@gmail.com
New address (456 Elm St): 
Contact updated successfully.

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 2

Contact List:
1. Shashwata Datta - 1234567890
2. Partha Datta - 9876543210

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 5

Contact List:
1. Shashwata Datta - 1234567890
2. Partha Datta - 9876543210

Enter the contact number to delete: 1
Contact 'Shashwata Datta' deleted.

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 2

Contact List:
1. Partha Datta - 9876543210

===== Contact Manager =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Choose an option (1-6): 6
Exiting Contact Manager. Goodbye!


