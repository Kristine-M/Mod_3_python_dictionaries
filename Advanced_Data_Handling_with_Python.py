hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

# Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.

#task 1
def book_room(hotel_rooms, room_num, customer_name):
    hotel_rooms[room_num]["status"] = "booked"
    hotel_rooms[room_num]["customer"] = customer_name
    
book_room(hotel_rooms, "101", "Kris")
print(hotel_rooms)

def check_out_room(hotel_rooms, room_num):
    hotel_rooms[room_num]["status"] = "available"
    hotel_rooms[room_num]["customer"] = ""
    
check_out_room(hotel_rooms, "101")
print(hotel_rooms)

def display_status(hotel_rooms):
    
    for room_num in hotel_rooms:
        print("Room ", room_num, " status: ", hotel_rooms[room_num]["status"])
        
display_status(hotel_rooms)

#task 2


# Holds a dictionary of products where each product has attributes 
# like name, category, and price.
products = {
    "1": {"name": "Desk", "category": "Home", "price": 400},
    "2": {"name": "Headphones", "category": "Electronics", "price": 100}
}

# Implement a search function that allows searching for products by 
# name, returning a list of matching products (case-insensitive search).
# Handle cases where no matches are found.

def search(products, prod_name):
    
    for item_num in products:
        if prod_name.lower() == products[item_num]["name"].lower():
            return products[item_num]
        
    print("No matches found")
                
                
found = search(products, "pjs")
print(found)

# Handle cases where no matches are found.