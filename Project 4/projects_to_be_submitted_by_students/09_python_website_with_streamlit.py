import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

# File Upload Button
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Pandas Reading the File that we uploaded

    st.subheader("Data Preview")
    st.write(df.head())  # It Displays the Data from the Uploaded file

    st.subheader("Data Statistics")
    st.write(df.describe())  # It Displays the Data Statistics from the Uploaded file such as mean, median, and standard deviation

    st.subheader("Filter Data")
    columns = df.columns.tolist()  # Converts to list
    selected_column = st.selectbox("Select a column to filter", columns)
    unique_values = df[selected_column].unique()  # Grabs all the unique values
    selected_value = st.selectbox("Select a value to filter", unique_values)
    filtered_df = df[df[selected_column] == selected_value]

    st.write(filtered_df)

    st.subheader("Data Visualization")
    selected_visualization = st.selectbox("Select a visualization", ["Scatter Plot", "Histogram", "Box Plot"])

    if selected_visualization == "Scatter Plot":
        x_axis = st.selectbox("Select X-axis", columns)
        y_axis = st.selectbox("Select Y-axis", columns)

        fig, ax = plt.subplots()
        ax.scatter(filtered_df[x_axis], filtered_df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title("Scatter Plot")
        st.pyplot(fig)

    elif selected_visualization == "Histogram":
        selected_column = st.selectbox("Select column to visualize", columns)

        fig, ax = plt.subplots()
        ax.hist(filtered_df[selected_column], bins=20, edgecolor="black")
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        ax.set_title("Histogram")
        st.pyplot(fig)

    elif selected_visualization == "Box Plot":
        selected_column = st.selectbox("Select column for Box Plot", columns)

        fig, ax = plt.subplots()
        ax.boxplot(filtered_df[selected_column].dropna(), vert=True)
        ax.set_title("Box Plot")
        ax.set_ylabel(selected_column)
        st.pyplot(fig)
