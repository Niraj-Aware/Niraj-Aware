import streamlit as st
import sqlite3
import random

conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT, name TEXT, phone TEXT, email TEXT, wallet REAL)')

def add_userdata(username,password,name,phone,email,wallet):
    c.execute('INSERT INTO userstable(username,password,name,phone,email,wallet) VALUES (?,?,?,?,?,?)',(username,password,name,phone,email,wallet))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def update_wallet(username,new_wallet):
    c.execute('UPDATE userstable SET wallet=? WHERE username=?',(new_wallet,username))
    conn.commit()

def main():
    st.title("Streamlit App with Login Page and User Database")

    menu = ["Home","Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            create_table()
            result = login_user(username,password)
            if result:
                current_user=result[0][0]
                current_wallet=result[0][5]
                st.success(f"Logged In as {current_user}")

                task = st.selectbox("Task",["Play Game","View Wallet"])
                if task == "Play Game":
                    st.subheader(f"Welcome to the game {current_user}!")
                    color=st.radio('Select Color',['Red','Green'])
                    bid=st.number_input(f'Enter Bid Amount (Wallet: {current_wallet})',min_value=0.0,max_value=current_wallet)
                    if bid>0:
                        red_bid=random.uniform(1,current_wallet)
                        green_bid=random.uniform(1,current_wallet)
                        winner_color='Red' if red_bid<green_bid else 'Green'
                        profit=bid*0.7
                        new_wallet=current_wallet+profit if color==winner_color else current_wallet-bid
                        update_wallet(current_user,new_wallet)
                        result=f"You won {profit}!" if color==winner_color else f"You lost {bid}."
                        result+=f"\n\nRed Bid: {red_bid}\nGreen Bid: {green_bid}\nWinner Color: {winner_color}"
                        st.write(result)

                elif task == "View Wallet":
                    result=f"Wallet: {current_wallet}"
                    st.write(result)

            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        new_name=st.text_input('Name')
        new_phone=st.text_input('Phone No.')
        new_email=st.text_input('Email')
        new_wallet=st.number_input('Money Wallet',min_value=0.0)

        if st.button("Signup"):
            create_table()
            add_userdata(new_user,new_password,new_name,new_phone,new_email,new_wallet)
            st.success(f"Welcome {new_user}! You have successfully created a new account.")
            #st.info(f"Go to Login Menu to login.")

if __name__ == '__main__':
  main()