import streamlit as st
import sqlite3
from datetime import datetime,timedelta

conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT, name TEXT, phone TEXT, email TEXT, wallet REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS gamestable(username TEXT,color TEXT,bid REAL,time TIMESTAMP)')

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
    c.execute('UPDATE userstable SET wallet=? WHERE username=?',(new_wallet,current_user))
    conn.commit()

def add_game_data(username,color,bid,time):
    c.execute('INSERT INTO gamestable(username,color,bid,time) VALUES (?,?,?,?)',(username,color,bid,time))
    conn.commit()

def get_game_data(time):
  time=(datetime.now()-timedelta(minutes=15)).strftime('%Y-%m-%d %H:%M:%S')
  query=f'SELECT * FROM gamestable WHERE time>="{time}"'
  print(query)
  c.execute(query)
  data=c.fetchall()
  return data

st.set_page_config(page_title='Streamlit App',page_icon=':slot_machine:',layout='wide')

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
                  col1,col2=st.columns(2)
                  with col1:
                      red_button=st.button('',key='red')
                      if red_button:
                          color='Red'
                          bid=st.number_input(f'Enter Bid Amount (Wallet: {current_wallet})',min_value=0.0,max_value=current_wallet,key='red_bid')
                          if bid>0:
                              add_game_data(current_user,color,bid,str(datetime.now()))
                              game_data=get_game_data(datetime.now())
                              red_bid=sum([x[2] for x in game_data if x[1]=='Red'])
                              green_bid=sum([x[2] for x in game_data if x[1]=='Green'])
                              winner_color='Red' if red_bid<green_bid else 'Green'
                              profit=bid*0.7
                              new_wallet=current_wal
if __name__ == '__main__':
 main()
