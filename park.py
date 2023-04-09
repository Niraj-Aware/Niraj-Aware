#!/usr/bin/env python
import streamlit as st
import time

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spots = capacity
        self.occupied_spots = {}

    def park_car(self, car_id):
        if self.available_spots == 0:
            st.write("Sorry, parking lot is full.")
        else:
            for spot, parked_car_id in self.occupied_spots.items():
                if parked_car_id == car_id:
                    st.write(f"Car {car_id} is already parked at spot {spot}.")
                    return
            # Car is not already parked, find available spot
            spot = self.get_available_spot()
            self.occupied_spots[spot] = car_id
            self.available_spots -= 1
            st.write(f"Car {car_id} parked at spot {spot}")
    
    def get_available_spot(self):
        for i in range(1, self.capacity+1):
            if i not in self.occupied_spots:
                return i
    
    def remove_car(self, car_id):
        for spot, parked_car_id in self.occupied_spots.items():
            if parked_car_id == car_id:
                del self.occupied_spots[spot]
                self.available_spots += 1
                st.write(f"Car {car_id} removed from spot {spot}")
                break
        else:
            st.write(f"Car {car_id} not found in parking lot")

def main():
    st.set_page_config(page_title="Smart Parking System", page_icon="🅿️", layout="wide")
    st.title("Smart Parking System")
    st.write("Welcome to the Smart Parking System! Please enter the capacity of the parking lot.")
    
    capacity = st.number_input("Enter parking lot capacity:", value=5, min_value=1)
    parking_lot = ParkingLot(capacity)
    
    st.write("\n### Parking lot status:")
    st.write(f"Available spots: {parking_lot.available_spots}/{parking_lot.capacity}")
    if parking_lot.occupied_spots:
        st.write("Occupied spots:")
        for spot, car_id in parking_lot.occupied_spots.items():
            st.write(f"Spot {spot}: Car {car_id}")
    else:
        st.write("No cars parked in the lot.")
    
    st.write("\n### Actions:")
    col1, col2, col3 = st.beta_columns(3)
    
    with col1:
        car_id = st.text_input("Enter car ID:")
        
    with col2:
        if st.button("Park car"):
            parking_lot.park_car(car_id)
    
    with col3:
        if st.button("Remove car"):
            parking_lot.remove_car(car_id)
    
    st.write("\n### Parking lot status:")
    st.write(f"Available spots: {parking_lot.available_spots}/{parking_lot.capacity}")
    if parking_lot.occupied_spots:
        st.write("Occupied spots:")
        for spot, car_id in parking_lot.occupied_spots.items():
            st.write(f"Spot {spot}: Car {car_id}")
    else:
        st.write("No cars parked in the lot.")
        
    time.sleep(1)

if __name__ == "__main__":
    main()
