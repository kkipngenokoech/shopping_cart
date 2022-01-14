from IPython.display import clear_output
cart=[]#global list variable
def add_item(item):
    clear_output()
    cart.append(item)
    print("item {} has been appended".format(item))
#add_item("banana")-test code
def remove_item(item):
    clear_output()
    try:
        cart.remove(item)
        print("item {} has been removed ".format(item))
    except:
        print("sorry we could not remove the item ".format(item))
def show_cart():
    clear_output()
    if cart:
        print("here is your cart:")
        for item in cart:
            print("-{}".format(item))
    else:
        print("your cart is empty")
def clear_cart():
    clear_output()
    cart.clear()
    print("your cart is empty")
def main_function():
    done=False
    while not done:
        answer=input("quit/add/remove/show/clear:").lower()
        clear_output()
        if answer=="quit":
            print("thank you for using our program")
            show_cart()
            done=True
        elif answer=="add":
            item_to_add=input("which item would you like to add if none enter none").title()
            if item_to_add=="None":
                break
            else:
                add_item(item_to_add)
        elif answer=="remove":
            item_to_remove=input("what item would you like to remove ,if none enter none").title()
            if item_to_remove=="None":
                break
            else:
                remove_item(item_to_remove)
        elif answer=="show":
            show_cart()
        elif answer =="clear":
            affirmative=input("are you sure you want to clear your cart").lower()
            if affirmative=="yes":
                clear_cart()
            else:
                print("your cart hasn't been cleared")
        else:
            print("sorry that wasn't part of the options try again:")
            main_function()
main_function()