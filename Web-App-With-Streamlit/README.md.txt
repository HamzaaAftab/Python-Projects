# Growth Minds Project Web App

🧠 **Growth Minds Project Web App using Streamlit** 🧠

## 📌 Overview
This Streamlit-based web application allows users to upload CSV and Excel files, perform data cleaning operations, visualize data, and convert files between CSV and Excel formats. The application provides an intuitive interface for handling datasets efficiently.

## 🚀 Features
- **File Upload:** Supports CSV and Excel file uploads.
- **Data Preview:** Displays the first five rows of the uploaded file.
- **Data Cleaning:**
  - Remove duplicate rows.
  - Fill missing values in numeric columns with the column mean.
- **Column Selection:** Choose specific columns to retain in the dataset.
- **Data Visualization:** Generate bar charts for numeric columns.
- **File Conversion:** Convert between CSV and Excel formats.
- **File Renaming:** Allows renaming before downloading.
- **Multiple File Handling:** Supports multiple files processing at once.
- **File Merging (Upcoming Feature):** Ability to merge multiple files into one dataset.

## 🔧 Installation
Ensure you have Python installed, then install the required dependencies:
```sh
pip install streamlit pandas openpyxl
```

## ▶️ How to Run the App
```sh
streamlit run app.py
```

## 📂 Usage
1. Upload one or more CSV/XLSX files.
2. View and clean data using the available options.
3. Visualize the dataset using bar charts.
4. Convert files to the desired format.
5. Download the processed file with a custom filename.

## 🎯 Future Enhancements
- Support for more data cleaning operations.
- Advanced data visualization options.
- Feature to merge multiple datasets.

## 💡 Contributing
Feel free to fork the repository, make improvements, and submit pull requests! 🚀

## 📜 License
This project is licensed under the MIT License.

