import time
users = {}
auctions = {}
bids = {}
user_id_counter = 1
auction_id_counter = 1
bid_id_counter = 1
def register_user():
    global user_id_counter
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {'id': user_id_counter, 'password': password}
    user_id_counter += 1
    print(f"User {username} registered successfully!")
def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = users.get(username)
    if user and user['password'] == password:
        print(f"Welcome back, {username}!")
        return user
    else:
        print("Invalid username or password.")
        return None
def create_auction(user_id):
    global auction_id_counter
    title = input("Enter auction title: ")
    description = input("Enter auction description: ")
    start_price = float(input("Enter starting price: "))
    auctions[auction_id_counter] = {'id': auction_id_counter, 'title': title, 'description': description, 'start_price': start_price, 'user_id': user_id, 'highest_bid': start_price}
    auction_id_counter += 1
    print("Auction created successfully!")
def place_bid(user_id):
    auction_id = int(input("Enter auction ID to bid on: "))
    bid_amount = float(input("Enter your bid amount: "))
    auction = auctions.get(auction_id)
    if auction and bid_amount > auction['highest_bid']:
        global bid_id_counter
        bids[bid_id_counter] = {'id': bid_id_counter, 'auction_id': auction_id, 'user_id': user_id, 'amount': bid_amount}
        auction['highest_bid'] = bid_amount
        bid_id_counter += 1
        print("Bid placed successfully!")
    else:
        print("Invalid auction ID or bid amount must be higher than current highest bid.")
def view_auctions():
    for auction in auctions.values():
        print(f"Auction ID: {auction['id']}")
        print(f"Title: {auction['title']}")
        print(f"Description: {auction['description']}")
        print(f"Starting Price: {auction['start_price']}")
        print(f"Current Highest Bid: {auction['highest_bid']}")
        print()
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. View Auctions")
        print("4. Create Auction")
        print("5. Place Bid")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
            if user:
                while True:
                    print("1. Create Auction")
                    print("2. Place Bid")
                    print("3. Logout")
                    action = input("Enter your choice: ")
                    if action == '1':
                        create_auction(user['id'])
                    elif action == '2':
                        place_bid(user['id'])
                    elif action == '3':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            view_auctions()
        elif choice == '6':
            print("Exiting...")
            print("Logged out successfully")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()
