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
    st.title("Smart Car Parking Simulation")
    capacity = st.number_input("Enter parking lot capacity:", value=5, min_value=1)
    parking_lot = ParkingLot(capacity)
    car_id = None
    action = None
    
    while True:
        st.write("\n### Parking lot status:")
        st.write(f"Available spots: {parking_lot.available_spots}/{parking_lot.capacity}")
        if parking_lot.occupied_spots:
            st.write("Occupied spots:")
            for spot, car_id in parking_lot.occupied_spots.items():
                st.write(f"Spot {spot}: Car {car_id}")
        else:
            st.write("No cars parked in the lot.")
        
        if not car_id:
            car_id = st.text_input("Enter car ID:")
        
        if not action:
            st.write("\n### Actions:")
            if parking_lot.available_spots > 0:
                if st.button("Park car"):
                    if car_id in parking_lot.occupied_spots.values():
                        st.write(f"Car {car_id} is already parked in the lot.")
                    else:
                        parking_lot.park_car(car_id)
            if parking_lot.occupied_spots:
                if st.button("Remove car"):
                    if car_id in parking_lot.occupied_spots.values():
                        parking_lot.remove_car(car_id)
                    else:
                        st.write(f"Car {car_id} is not parked in the lot.")
            if st.button("Exit"):
                st.write("Exiting...")
                break
        
        time.sleep(1)
            
if __name__ == "__main__":
    main()
