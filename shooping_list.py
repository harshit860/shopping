shopping_list = []


def add_to_list(item):

    shopping_list.append(item)
    print(" list has {} items.:".format(len(shopping_list)))


def show_list():
    print("Heres your list")
    for item in shopping_list:
        print(item)


def show_help():
     print("Whats should we pick up at the store")
     print(""""
     ======================>Shopping List<===========================
     YOU CAN START TO ENTER THE ITEMS IN THE LIST 
     
     OTHER OPTIONS AVAILABLE 
     Enter 'DONE' to stop adding items
     Enter 'HELP' for this help again
     Enter 'SHOW' to show the list
     """)

show_help()

while True:
    new_item = input(">")

    if new_item == 'DONE':
       print("Thank you for using Shooping list")
       break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)
