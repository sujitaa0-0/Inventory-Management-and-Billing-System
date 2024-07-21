item_dict={}
def equipments():
    file=open("item.txt","r")
    item_id=1
    for line in file:
        line=line.replace("\n","")
        item_dict[item_id]=line.split(",")
        item_id=item_id+1
    file.close()


def display():
    print("-" * 120)
    print("S.N |\t\t Name\t\t\t|\t   Brand\t\t|\tPrice\t|\tQuantity")
    print("-" * 120)
    for key, values in item_dict.items():
        print(key,"    "+str(values[0]).ljust(45)+str(values[1]).ljust(30)+str(values[2]).ljust(20)+str(values[3]))
        print("-" * 120)


equipments()
