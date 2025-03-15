import streamlit as st
import pandas as pd
import json
import os
import requests

# File to store book data
LIBRARY_FILE = "library.json"

# Function to load books from a file
def load_books():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save books to a file
def save_books(books):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Load books into session state
if "books" not in st.session_state:
    st.session_state.books = load_books()

def get_book_cover(title):
    """Fetch book cover from Open Library API."""
    try:
        response = requests.get(f"https://openlibrary.org/search.json?title={title}")
        data = response.json()
        if "docs" in data and len(data["docs"]) > 0:
            cover_id = data["docs"][0].get("cover_i", None)
            if cover_id:
                return f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
    except:
        pass
    return "https://via.placeholder.com/150"  # Default placeholder

# Sidebar navigation
st.sidebar.title("📚 Personal Library Manager")
option = st.sidebar.radio("Navigate", ["Add Book", "Remove Book", "Search Books", "Display All Books", "Statistics"])

# Add a book
if option == "Add Book":
    st.title("📖 Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, step=1)
        genre = st.text_input("Genre")
        read_status = st.checkbox("Have you read this book?")
        submit = st.form_submit_button("Add Book")
    
    if submit:
        new_book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
        st.session_state.books.append(new_book)
        save_books(st.session_state.books)
        st.success(f"'{title}' added successfully!")

# Remove a book
elif option == "Remove Book":
    st.title("🗑 Remove a Book")
    book_titles = [book["title"] for book in st.session_state.books]
    book_to_remove = st.selectbox("Select a book to remove", book_titles)
    if st.button("Remove Book"):
        st.session_state.books = [book for book in st.session_state.books if book["title"] != book_to_remove]
        save_books(st.session_state.books)
        st.success(f"'{book_to_remove}' removed successfully!")

# Search for a book
elif option == "Search Books":
    st.title("🔍 Search for a Book")
    search_query = st.text_input("Enter title or author")
    if st.button("Search"):
        results = [book for book in st.session_state.books if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found.")

# Display all books
elif option == "Display All Books":
    st.title("📚 Your Library")
    if st.session_state.books:
        df = pd.DataFrame(st.session_state.books)
        df["read"] = df["read"].apply(lambda x: "✅ Read" if x else "❌ Unread")
        st.table(df)
    else:
        st.warning("Your library is empty.")

# Display statistics
elif option == "Statistics":
    st.title("📊 Library Statistics")
    total_books = len(st.session_state.books)
    read_books = sum(1 for book in st.session_state.books if book["read"])
    unread_books = total_books - read_books
    read_percentage = (read_books / total_books * 100) if total_books > 0 else 0
    
    st.metric("Total Books", total_books)
    st.metric("Read Books", read_books)
    st.metric("Unread Books", unread_books)
    st.metric("Percentage Read", f"{read_percentage:.2f}%")
    
    st.bar_chart(pd.DataFrame({"Read": [read_books], "Unread": [unread_books]}, index=["Books"]))

st.sidebar.info("Built with ❤️ using Streamlit by HAMZA AFTAB!")

# Save books on session state change
def save_books(books):
    st.session_state.books = books

st.session_state.books = load_books()

# # Display book covers
# if st.session_state.books:
#     for book in st.session_state.books:
#         st.image(get_book_cover(book["title"]), width=150)
#         st.write("")
#         st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
#         st.write("")
#         st.markdown("---")
#         st.write("")
#         st.info(f"Cover image fetched from Open Library API.")
#     else:
#         st.warning("Your library is empty.")
#         st.info(f"Cover images fetched from Open Library API.")

# Save books on session state change
