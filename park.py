#!/usr/bin/env python
import streamlit as st

def main():
    st.set_page_config(page_title="Parking Lot App", page_icon="🅿️", layout="wide")
    st.title("Parking Lot App")

    # create a list of 8 parking spots
    parking_spots = ["Available" for _ in range(8)]

    # display the parking lot cards
    cols = st.beta_columns(4)
    for i, col in enumerate(cols):
        if parking_spots[i] == "Available":
            button = col.button(f"Spot {i+1}\n{parking_spots[i]}")
            if button:
                parking_spots[i] = "Occupied"
                col.empty()
                col.info(f"Spot {i+1}\n{parking_spots[i]}")
        else:
            button = col.button(f"Spot {i+1}\n{parking_spots[i]}")
            if button:
                parking_spots[i] = "Available"
                col.empty()
                col.success(f"Spot {i+1}\n{parking_spots[i]}")

if __name__ == "__main__":
    main()
