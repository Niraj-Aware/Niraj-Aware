#!/usr/bin/env python
import streamlit as st

def main():
    st.set_page_config(page_title="Parking Lot App", page_icon="🅿️", layout="wide")
    st.title("Parking Lot App")

    # create a list of 8 parking spots
    parking_spots = ["Available" for _ in range(8)]

    # display the parking lot cards
    cols = st.beta_columns(4)
    selected_spots = []
    for i, col in enumerate(cols):
        if parking_spots[i] == "Available":
            spot_selected = col.checkbox(f"Spot {i+1}\n{parking_spots[i]}")
            if spot_selected:
                selected_spots.append(i)
                col.info(f"Spot {i+1}\n{parking_spots[i]}")
            else:
                col.empty()
        else:
            spot_selected = col.checkbox(f"Spot {i+1}\n{parking_spots[i]}")
            if spot_selected:
                selected_spots.append(i)
                col.success(f"Spot {i+1}\n{parking_spots[i]}")
            else:
                col.empty()

    if selected_spots:
        if st.button("Update Selected Spots"):
            for spot_index in selected_spots:
                if parking_spots[spot_index] == "Available":
                    parking_spots[spot_index] = "Occupied"
                else:
                    parking_spots[spot_index] = "Available"
            selected_spots = []
    
    st.write(parking_spots)

if __name__ == "__main__":
    main()
