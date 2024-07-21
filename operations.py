import read 
import write
from datetime import datetime

def valid_item_id(): 
    '''This function prompts user to enter ID id an item and validates the input
    
    Returns: int(The valid item ID entered by user)
    '''
    while True:
        try:
            item_id=int(input("Please enter the ID of the item your choosing: "))
            if 0 < item_id and item_id <= len(read.item_dict):
                return item_id
            print("Invalid Item ID. Please try again.")
        except ValueError:  
            print("Non-numerical values are invalid! Please try again.")

def update_item_file(quantity, valid_id, is_return):
    '''This function updates the value of quantity of selected after a transaction
     for returning transactions the value of quantity is increased whereas for renting transaction quantity is decreased
    
    Parameters : 
        quantity(int): The valid quantity entered by user
        valid_id(int): The valid item ID entered by user
        is_return(boolean): To represent if transaction is rent or return
    '''
    if is_return==True:
        read.item_dict[valid_id][3] =int(read.item_dict[valid_id][3]) + (int(quantity))
    else:
        read.item_dict[valid_id][3] =int(read.item_dict[valid_id][3]) - (int(quantity))    
    
    file=open("item.txt","w")
    for values in read.item_dict.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+"\n")
    file.close()

def user_input():
    '''This function prompts user to input customer details validates the input
    
    Returns: 
    first_name(String): The valid first name of customer
    last_name(String): The valid last name of customer
    phone_num(String): The valid phone number of customer
    '''
    while(True):                   
        first_name=input("Please enter your first name: ").title().strip()
        if first_name.isalpha():
            break
        print("Please enter alphabetical values for first name and try again.")
    while(True):
        last_name=input("Please enter your last name: ").title().strip()
        if last_name.isalpha():
            break
        print("Please enter alphabetical values for last name and try again.")
    while(True):
        phone_num=input("Please enter your phone number: ")
        if len(phone_num)==10 and phone_num.isdigit():
            break
        print("Please enter a 10 digit numerical value for phone number and try again.")
    return first_name, last_name, phone_num

def rent():
    print("")
    print("Thank you for choosing to rent.")
    print("")
    is_return=False
    
    first_name, last_name, phone_num = user_input()
    print("Thank you for your input.")
    print("Given below is the list of equipment. Please choose to your liking.")
     
         
    rented_items=[]
    
    rent_more=True
    while rent_more==True:
        read.display()
        
        print("")
        valid_id,quantity =get_valid_id_quantity(is_return)
        update_item_file(quantity, valid_id, is_return) 
        
        item_name=read.item_dict[valid_id][0]
        selected_quantity=quantity
        display_price_of_item=read.item_dict[valid_id][2]
        brand_name=read.item_dict[valid_id][1]
        price_of_selected_item=read.item_dict[valid_id][2].replace("$",'')
        total_price=int(price_of_selected_item)*int(selected_quantity)
        
        rented_items.append([item_name,selected_quantity,display_price_of_item,total_price,brand_name])
        
        user_request=input("Dear user, do you want to borrow more items?\nIf yes, press 'Y' else press 'Enter': ").upper().strip()
        print("\n")
        
        if  user_request=='Y':
            rent_more=True
        else:
            print_invoice(rented_items,first_name,last_name,phone_num,is_return)
            break 
    
def return_equipment():
    print("\n")
    print("Thank you for returning")
    is_return=True
    
    first_name, last_name, phone_num = user_input()
    
    print("Given below is the list of equipment. Please choose to your liking.")
    
    rented_items=[]
    
    return_more=True
    while return_more==True:
        read.display()
        print("")
        valid_id,quantity=get_valid_id_quantity(is_return)
        update_item_file(quantity, valid_id, is_return)        
        
        while True:
            try:
                days=int(input("Enter the number of days the item was rented: "))
                break
            except ValueError:
                print("Non-numerical values are invalid! Please try again.")
        
        if(days>5):
            fine_amt = 3*(days-5)
        else:
            fine_amt = 0
        
        item_name=read.item_dict[valid_id][0]
        selected_quantity=quantity
        brand_name=read.item_dict[valid_id][1]
        display_price_of_item=read.item_dict[valid_id][2]
        price_of_selected_item=read.item_dict[valid_id][2].replace("$",'')
        total_price=int(price_of_selected_item)*int(selected_quantity)+fine_amt
        
        rented_items.append([item_name,selected_quantity,display_price_of_item,total_price,fine_amt,brand_name])
        
        user_request=input("Dear user, do you want to return more items?\nIf yes, press 'Y' else press 'Enter': ").upper().strip()
        print("\n")
        if user_request=='Y':
            return_more=True
            
        else:
            print_invoice(rented_items,first_name,last_name,phone_num,is_return)
            return
    
        
 
def get_valid_id_quantity(is_return):
    valid_id = valid_item_id()
    while True:
        try:
            quantity=int(input("Please enter the quantity you want: "))  
            get_quantity_of_selected_item=read.item_dict[valid_id][3]
            if is_return:
                if  quantity>=1 :
                    return valid_id,quantity
                if_change=input("Dear user, you cannot return 0 equipment. Do you want to choose another item to return?\n If yes, press 'C' else press 'Enter':").upper().strip()
                if if_change=="C":
                    valid_id=valid_item_id()
            else:
                if 0 < quantity <= int(get_quantity_of_selected_item):
                    return valid_id,quantity
                if_change=input("Dear user, Item no."+str(valid_id)+" only has "+str(get_quantity_of_selected_item)+" equipment left.\nPlease enter a suitable quantity and try again or press 'C' to change item else press 'Enter':").upper().strip()
                if if_change=='C':
                    valid_id=valid_item_id()
        except ValueError:  
            print("Non-numerical values are invalid! Please try again.")
        

def print_invoice(rented_items,first_name,last_name,phone_num,is_return):
    total=0
    for i in rented_items:
        total+=int(i[3])
    grand_total=total
    today_date_and_time=datetime.now()
    print("\n")
    print("\t\t\t\t\tSUJITA'S RENTAL SHOP")
    print("\n")
    print("\t\t\t\tAddress : Kalanki  | Contact : 9847346647")
    print("")
    print("Name: "+first_name+" "+last_name)
    print("Contact Number: "+str(phone_num))
    print("")
    if(is_return):
        print("Date and time of return: "+str(today_date_and_time))
        print("="*130)
        print("Return Details")
        print("-"*130)
        print("Name\t\t\t\t|\tBrand\t\t|  Quantity  |   Rate     |   Fine    |   Total   |")
        print("-"*130)
            
        for i in rented_items:
            print((i[0]).ljust(40)+(i[5]).ljust(23)+str((i[1])).ljust(10)+str(i[2]).ljust(14)+"$"+str((i[4])).ljust(11)+"$"+str((i[3])))
        print("-"*130)
        print("Grand Total: $"+str(grand_total).ljust(2))
        print("-"*50)
        print("Thank you for buying")
        print("Please shop with us again!")
        write.renter_bill(rented_items,first_name,last_name,phone_num,grand_total,today_date_and_time,is_return)
    else:
        print("Date and time of purchase: "+str(today_date_and_time))
        print("="*100)
        print("Purchase Details")
        print("-"*100)
        print("Name\t\t\t\t|\tBrand\t\t|  Quantity  |    Rate    |    Total   |")
        print("-"*100)
            
        for i in rented_items:
            print((i[0]).ljust(40)+(i[4]).ljust(23)+str(i[1]).ljust(10)+str(i[2]).ljust(14)+"$"+str(i[3]))
        print("-"*100)
        print("Grand Total: $"+str(grand_total))
        print("-"*50)
        print("Rent Ownership is 5 days.")
        print("Note: Fine will be added to the grand total incase of delay.")
        write.renter_bill(rented_items,first_name,last_name,phone_num,grand_total,today_date_and_time,is_return)

    
