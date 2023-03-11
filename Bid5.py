import streamlit as st
import time
import random

# dictionary to store user information
USERS = {}


# function to authenticate user
def login(username, password):
    if username in USERS and USERS[username]['password'] == password:
        return True
    else:
        return False


# function to register new user
def register(username, phone, email, wallet, password):
    if username in USERS:
        return False
    else:
        USERS[username] = {'phone': phone, 'email': email, 'wallet': wallet, 'password': password}
        return True


# function to validate bid amount
def validate_bid(username, amount):
    wallet = USERS[username]['wallet']
    if amount <= wallet:
        USERS[username]['wallet'] -= amount
        return True
    else:
        return False


# function to play the game
def play_game(users, color, bids):
    # determine the winning bid
    min_bid = min(bids.values())
    winner = [user for user in bids.keys() if bids[user] == min_bid][0]

    # calculate the winner's profit
    amount = bids[winner]
    profit = int(amount * 0.7)
    USERS[winner]['wallet'] += profit

    # display the result
    st.write(f"Color: {color}")
    st.write("Bids:")
    for user, amount in bids.items():
        st.write(f"{user}: {amount}")
    st.write(f"Winner: {winner}")
    st.write(f"Profit: {profit}")
    st.write(f"{winner}'s new wallet balance: {USERS[winner]['wallet']}")


# main program
def main():
    st.set_page_config(page_title="Colour Bid Game", page_icon=":money_with_wings:")
    st.title("Colour Bid Game")

    # set up session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'increment' not in st.session_state:
        st.session_state['increment'] = 10
    if 'bids' not in st.session_state:
        st.session_state['bids'] = {'Red': 0, 'Green': 0, 'Blue': 0}

    # login or register
    if st.sidebar.button("Login"):
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if login(username, password):
            st.sidebar.success("Login successful!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.sidebar.error("Invalid username or password")
    elif st.sidebar.button("Register"):
        username = st.sidebar.text_input("Username")
        phone = st.sidebar.text_input("Phone number")
        email = st.sidebar.text_input("Email")
        wallet = st.sidebar.number_input("Wallet amount", min_value=0, step=1)
        password = st.sidebar.text_input("Password", type="password")
        if register(username, phone, email, wallet, password):
            st.sidebar.success("Registration successful!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.sidebar.error("Username already exists")

    # display color cards
    st.write("Click on a color card to place a bid")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Red"):
            if st.session_state['logged_in']:
            username = st.session_state['username']
            wallet = USERS[username]['wallet']
            bid_amount = st.number_input("Enter bid amount", min_value=st.session_state['increment'], max_value=wallet, step=st.session_state['increment'])
            if validate_bid(username, bid_amount):
                st.session_state['bids']['Red'] += bid_amount
            st.success("Bid placed successfully!")
            else:
            st.error("Insufficient funds")
            with col2:
                if
            st.button("Green"):
            if st.session_state['logged_in']:
                username = st.session_state['username']
            wallet = USERS[username]['wallet']
            bid_amount = st.number_input("Enter bid amount", min_value=st.session_state['increment'], max_value=wallet,
                                         step=st.session_state['increment'])
            if validate_bid(username, bid_amount):
                st.session_state['bids']['Green'] += bid_amount
            st.success("Bid placed successfully!")
            else:
            st.error("Insufficient funds")
            with col3:
                if
            st.button("Blue"):
            if st.session_state['logged_in']:
                username = st.session_state['username']
            wallet = USERS[username]['wallet']
            bid_amount = st.number_input("Enter bid amount", min_value=st.session_state['increment'], max_value=wallet,
                                         step=st.session_state['increment'])
            if validate_bid(username, bid_amount):
                st.session_state['bids']['Blue'] += bid_amount
            st.success("Bid placed successfully!")
            else:
            st.error("Insufficient funds")

            # display wallet balance
            if st.session_state['logged_in']:
                username = st.session_state['username']
            wallet = USERS[username]['wallet']
            st.write(f"Your wallet balance: {wallet}")

            # play the game
            if st.button("Play"):
                if
            st.session_state['logged_in']:
            play_game(USERS, "Random", st.session_state['bids'])
            st.session_state['bids'] = {'Red': 0, 'Green': 0, 'Blue': 0}
            else:
            st.warning("Please login or register to play the game")

            # reset the game
            if st.button("Reset"):
                st.session_state['bids'] = {'Red': 0, 'Green': 0, 'Blue': 0}
            st.success("Game reset successfully!")

            # logout
            if st.session_state['logged_in'] and st.sidebar.button("Logout"):
                st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.sidebar.success("Logout successful!")

if __name__ == "__main__":
    main()
