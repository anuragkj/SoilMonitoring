import streamlit as st
import gspread
from PIL import Image
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import plotly.graph_objects as go
import datetime

# Set up the page layout
st.set_page_config(page_title="Soilitix", page_icon=":📈:")


st.title("Soilitix")

st.caption(
    "Optimize your crop and plant growth with Soilitix - the web application for tracking soil health metrics like temperature, moisture, and humidity."
)

with st.sidebar:
    img = Image.open("./Images/soilitix.png")
    st.image(img)
    st.subheader("About Soiltix")
    st.write(
        "Soilitix is a web application designed for monitoring soil health. It allows farmers and gardeners to track important soil metrics such as temperature, moisture, and humidity. The application provides an easy-to-use interface that enables users to visualize and analyze their soil data, helping them make informed decisions about their crops and plants."
    )

    st.write(
        "One of the key features of Soilitix is the ability to track soil data over time. Users can select a date range and view data for that specific period, allowing them to identify trends and patterns in their soil health. The application also provides a slider that allows users to adjust the number of data points displayed, giving them more control over their data analysis."
    )

    st.write(
        "Overall, Soilitix is a robust tool for anyone who wants to monitor their soil health and optimize their crop and plant growth. Its user-friendly interface, robust data analysis capabilities, and customizable alerts make it an essential tool for farmers, gardeners, and anyone else who cares about their soil health."
    )

# Authenticate with service account credentials
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("./google-creds.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet and select the worksheet
sheet = client.open("Soilitix_Data").sheet1

# Create the Streamlit interface
column_select = st.selectbox(
    "Sensed Data to be plotted:",
    ["Temperature", "Humidity", "Moisture"],
    key="column_select",
)

all_data = sheet.get_all_values()
dates = sorted(list(set([row[0] for row in all_data])))

# Get the initial data for the selected date
# Set default date to current date
default_date = datetime.date.today().strftime("%m/%d/%Y")
selected_date = st.selectbox("Select Date", dates, index=dates.index(default_date))
# selected_date = st.selectbox("Select Date", dates, index=len(dates) - 1)
selected_data = [row for row in all_data if row[0] == selected_date]
selected_row_count = st.slider(
    "Number of rows to display", min_value=1, max_value=len(selected_data), value=10
)

# # Create the initial Plotly figure object
# df = pd.DataFrame(
#     selected_data, columns=["Date", "Time", "Temperature", "Humidity", "Moisture"]
# )

selected_data = [row for row in all_data if row[0] == selected_date]

last_n_data = selected_data[-selected_row_count:]

df = pd.DataFrame(
    last_n_data, columns=["Date", "Time", "Temperature", "Humidity", "Moisture"]
)
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Time"], y=df[column_select]))

# Add layout settings
fig.update_layout(
    title=f"{column_select} vs Time for {selected_date}",
    xaxis_title="Time",
    yaxis_title=f"{column_select}",
)
# Show the graph
st.plotly_chart(fig, use_container_width=True)

# Define function to update the graph
def update_graph():
    # Get the data for the selected date and number of rows
    selected_data = [row for row in all_data if row[0] == selected_date]
    last_n_data = selected_data[-selected_row_count:]
    df = pd.DataFrame(
        last_n_data, columns=["Date", "Time", "Temperature", "Humidity", "Moisture"]
    )

    # Update the graph data
    fig.update_traces(x=df["Time"], y=df[column_select])


# Create a button to refresh the data
if st.button("Refresh Data"):
    update_graph()
