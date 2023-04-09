#!/usr/bin/env python
import streamlit as st

# Define a list of available parking spots
available_spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

# Define a dictionary to store the parked cars
parked_cars = {}

def main():
    st.title("Smart Car Parking")

    # Display the current status of the parking spots
    st.write("Current Parking Status:")
    for spot in available_spots:
        if spot in parked_cars:
            st.write(f"{spot}: {parked_cars[spot]}")
        else:
            st.write(f"{spot}: Empty")

    # Ask the user to choose an action
    action = st.selectbox("Choose an action:", ["Park car", "Remove car", "Exit"], key="action")

    # Perform the chosen action
    if action == "Park car":
        park_car()
    elif action == "Remove car":
        remove_car()
    else:
        st.write("Thank you for using Smart Car Parking!")

def park_car():
    # Ask the user for the car details
    name = st.text_input("Enter your name:", key="name")
    car_number = st.text_input("Enter your car number:", key="car_number")
    spot = st.selectbox("Choose a parking spot:", [spot for spot in available_spots if spot not in parked_cars], key="parking_spot")

    # Park the car
    parked_cars[spot] = f"{name} ({car_number})"
    st.write(f"{spot} is now occupied by {name} ({car_number})")

def remove_car():
    # Ask the user for the parking spot to free up
    spot = st.selectbox("Choose a parking spot to free up:", [spot for spot in parked_cars], key="remove_spot")

    # Remove the parked car from the dictionary
    removed_car = parked_cars.pop(spot)
    st.write(f"{spot} is now empty. {removed_car} has left.")

if __name__ == "__main__":
    main()
