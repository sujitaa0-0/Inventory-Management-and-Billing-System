def renter_bill(rented_items,first_name,last_name,phone_num,grand_total,today_date_and_time,is_return):
    
    if(is_return):
        message="Return"
    else:
        message="Rent"
    with open(message+"_"+last_name+"_"+str(phone_num)+".txt","w") as file:
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\t\t\tSUJITA'S RENTAL SHOP\n")
        file.write("\n")
        file.write("\t\t\t\t\t\t\t\tAddress : Kamalpokhari | Contact : 9847346647\n")
        file.write("\t\t\t\t\t\t\t\t"+"="*29)
        file.write("\n\n\n")
        file.write("Name: "+first_name+" "+last_name+"\n")
        file.write("Contact Number: "+str(phone_num)+"\n")
        file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
        file.write("="*83)
        file.write("\n")
        if(is_return):
            file.write("Return Details\n")
            file.write("-"*178)
            file.write("\n")
            file.write("Name\t\t\t\t\t\t\t|\t\tBrand\t\t|\t\tQuantity\t\t|\t\tRate\t\t|\t\tFine\t\t|\t\tTotal\t\t\t|\n")
            file.write("-"*178)
            file.write("\n")
            for i in rented_items:
                file.write(str(i[0]).ljust(60)+str(i[5]).ljust(40)+str(i[1]).ljust(35)+str(i[2]).ljust(35)+"$"+str((i[4])).ljust(35)+"$"+str((i[3]))+"\n")
            file.write("-"*178)
            file.write("\n")
            file.write("Grand Total: $"+str(grand_total)+"\n")
            file.write("-"*50)
            file.write("\n")
            file.write("Thank you for buying.\n")
            file.write("Please do shop with us again.\n")
            file.write("\n")
        else:
            file.write("Purchase Details \n")
            file.write("-"*154)
            file.write("\n")
            file.write("Name\t\t\t\t\t\t\t|\t\tBrand\t\t|\t\tQuantity\t\t|\t\tRate\t\t|\t\tTotal\t\t\t|\n")
            file.write("-"*154)
            file.write("\n")
            for i in rented_items:
                file.write(str(i[0]).ljust(60)+str(i[4]).ljust(40)+str(i[1]).ljust(35)+str(i[2]).ljust(35)+"$"+str(i[3])+"\n")
            file.write("-"*154)
            file.write("\n")
            file.write("Grand Total: $"+str(grand_total)+"\n")
            file.write("-"*50)
            file.write("\n")
            file.write("Rent Ownership is 5 days.\n")
            file.write("Note: Fine will be added to the grand total incase of delay.\n")
            file.write("\n")
        
