#Suppose that you’re in the habit of making a list of items you need from the grocery store.
#In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

def main():
     shopping_list()
   

def shopping_list():
    cart = {
    }
   
    while True:
      try:
        item = input().upper()

        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1   
      except EOFError:  
          break

    print_list(sorted(cart.items()))
    
def print_list(sorted_cart):
    
    for item, count in sorted_cart:
     print(f"{count} {item}")

main()

