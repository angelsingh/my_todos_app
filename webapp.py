import streamlit as st
import func  # This will handle file reading/writing

# Load todos from the file at the start of the session
if 'todos' not in st.session_state:
    st.session_state['todos'] = func.get_todos()  # Initialize todos from file

def add_todo():
    """Add a new todo item and save to the file."""
    todo = st.session_state['new_todo']
    if todo.strip():  # Avoid empty todos
        st.session_state['todos'].append(todo + "\n")  # Append newline to match file format
        func.write_todos(st.session_state['todos'])  # Save to file
        st.session_state['new_todo'] = ""  # Clear the input field

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Display the list of todos
for index, todo in enumerate(st.session_state['todos']):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")  # Strip to remove extra spaces
    if checkbox:
        st.session_state['todos'].pop(index)  # Remove from session state
        func.write_todos(st.session_state['todos'])  # Save updated list to file
        st.rerun()  # Refresh the app state

# Input field for adding new todos
st.text_input(label="Add a new todo item:", placeholder="Type here...",
              on_change=add_todo, key='new_todo')