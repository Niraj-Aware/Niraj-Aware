import streamlit as st
import requests

def generate_quickchart_url(data):
    # Construct the API URL for quickchart.io
    url = "https://quickchart.io/chart?c=" + data
    return url

def main():
    st.title("Graph Generator using quickchart.io API")
    
    # Get user statements as input
    user_statements = st.text_area("Enter your statements here:")
    
    # Process user statements and create data for the graph
    # (Replace this with your data processing logic)
    data_for_graph = {
        "type": "bar",
        "data": {
            "labels": ["Label 1", "Label 2", "Label 3"],
            "datasets": [{
                "label": "Data",
                "data": [10, 20, 15]
            }]
        }
    }
    
    # Convert data to JSON string
    data_json = json.dumps(data_for_graph)

    # Generate the quickchart.io URL for the graph
    graph_url = generate_quickchart_url(data_json)

    # Display the graph
    st.image(graph_url, use_column_width=True)

if __name__ == "__main__":
    main()
