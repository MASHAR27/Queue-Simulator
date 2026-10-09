from collections import deque

my_queue = deque() # My initial empty queue of customers
print("Your a waiter who accordingly manages a queue")

while True:
    print("Choose 1 for adding a customers name to the queue ")
    print("Choose 2 for serving the next customer")
    print("Choose 3 for viewing the next customer to be served")
    print("Choose 4 for viewing the whole queue of customers")
    print("Choose 5 for Exiting")
    
    option = input("Please enter choice:  ").strip()
    
    if option == '1':
        name_cust = input("Please enter the customers name:  ").strip()
        if name_cust:
            my_queue.append(name_cust)
        else:
            print("The name can't be empty!")
    elif option == '2':
        if my_queue:
            print("Customer being served now!")
            cust_removed = my_queue.popleft()
            print(f"{cust_removed} has been served!!")
        else:
            print("No customer to serve in queue as the queue is empty!")
    elif option == '3':
        if my_queue:
            print(f"The next customer to be served in the queue is {my_queue[0]}")
        else:
            print("No next customer as the queue is empty!")    
    elif option == '4':
        print(f"The queue has total customers waiting : {len(my_queue)}  ") 
        print(f"The queue has these customers currently waiting: {my_queue}  ")      
    elif option == '5':
        break
    else:
        print("Please enter a valid option")      
                             
    
    