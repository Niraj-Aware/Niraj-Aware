#!/usr/bin/env python
import streamlit as st

def main():
    st.set_page_config(page_title="Parking Lot App", page_icon="🅿️", layout="wide")
    st.title("Parking Lot App")

    # create a list of 8 parking spots
    parking_spots = ["Available" for _ in range(8)]

    # display the parking lot cards
    cols1, cols2 = st.beta_columns(2)
    selected_spots = []
    show_more = False
    for i, col in enumerate(cols1):
        if i >= 4 and not show_more:
            break
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
        # display the status of the parking spot
        col.write(f"Status: {parking_spots[i]}")

    for i, col in enumerate(cols2):
        if i < 4 and not show_more:
            continue
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
        # display the status of the parking spot
        col.write(f"Status: {parking_spots[i]}")

    if st.button("Show More" if not show_more else "Show Less"):
        show_more = not show_more
    
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
