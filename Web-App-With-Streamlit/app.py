import streamlit as st
import pandas as pd
import os
from io import BytesIO
import datetime
import matplotlib.pyplot as plt

# Setting the app
st.set_page_config(page_title="Growth Minds Project Web App", page_icon="🧠", layout="wide")
st.title("🧠 Growth Minds Project Web App using Streamlit 🧠")

# Instructions
st.write("Transform files into CSV and Excel format with built-in data cleaning and visualization")

# File upload section
uploaded_files = st.file_uploader("Upload a file", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        file_size = file.getbuffer().nbytes / 1024  # Get file size in KB
        upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unknown file extension: {file_ext}")
            continue

        # Display file information
        st.subheader(f"File: {file.name}")
        st.write(f"**File Type:** {file_ext}")
        st.write(f"**File Size:** {file_size:.2f} KB")
        st.write(f"**Upload Time:** {upload_time}")
        st.write(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")
        
        # Show first 5 rows
        st.subheader("Preview:")
        st.dataframe(df.head())

        # Data Cleaning
        st.subheader("Data Cleaning:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(f"Remove Duplicates - {file.name}"):
                df = df.drop_duplicates()
                st.success("Duplicates removed successfully!")

        with col2:
            if st.button(f"Fill Missing Values - {file.name}"):
                numeric_cols = df.select_dtypes(include=['number']).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.success("Missing values filled successfully!")
                
        with col3:
            if st.button(f"Clean Column Names - {file.name}"):
                df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
                st.success("Column names cleaned successfully!")

        # Column Selection
        st.subheader("Column Selection:")
        selected_columns = st.multiselect(f"Select columns to keep - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns] if selected_columns else df
        
        # Data Summary
        if st.checkbox(f"Show Summary Stats - {file.name}"):
            st.subheader("Data Summary:")
            st.write(df.describe().T)

        # Visualizations
        st.subheader("Visualizations:")
        if st.checkbox(f"Show Bar Chart - {file.name}"):
            st.bar_chart(df.select_dtypes(include=['number']).iloc[:, :3])
        
        if st.checkbox(f"Show Pie Chart - {file.name}"):
            categorical_cols = df.select_dtypes(include=['object']).columns
            if not categorical_cols.empty:
                category_col = st.selectbox("Choose a categorical column:", categorical_cols)
                fig, ax = plt.subplots()
                df[category_col].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                st.pyplot(fig)
            else:
                st.warning("No categorical columns available for pie chart.")

        # File Conversion
        st.subheader("File Conversion:")
        conversion_type = st.radio(f"Convert {file.name} to:", ["Excel", "CSV"])
        new_file_name = st.text_input(f"Rename {file.name} before download:", file.name)

        if st.button(f"Convert & Download - {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                new_file_name = new_file_name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False)
                new_file_name = new_file_name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)
            st.download_button(label=f"Download {new_file_name}", data=buffer.getvalue(), file_name=new_file_name, mime=mime_type)

        # File Merging Feature (If multiple files uploaded)
        if len(uploaded_files) > 1:
            st.subheader("Merge Files")
            merge_col = st.text_input("Enter column name for merging (if applicable):")
            if merge_col and merge_col in df.columns:
                if 'merged_df' not in st.session_state:
                    st.session_state['merged_df'] = df
                else:
                    st.session_state['merged_df'] = pd.merge(st.session_state['merged_df'], df, on=merge_col, how='outer')
                st.success("Files merged successfully!")

if 'merged_df' in st.session_state:
    st.subheader("Merged Data Preview")
    st.dataframe(st.session_state['merged_df'].head())