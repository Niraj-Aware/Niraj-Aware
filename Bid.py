import streamlit as st
import sqlite3

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

                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics")

                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(user_result,columns=["Username","Password","Name","Phone","Email","Wallet"])
                    st.dataframe(clean_db)
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