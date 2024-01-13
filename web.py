import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]
    todo = todo + "\n"
    functions.add_todo(todo)

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This App should help increase productivity")

# Impliment Delete Checked Item
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # print(f"Checkbox: {checkbox}, todo: {todo}")
    if checkbox:
        functions.delete_todo(index)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="New", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

st.session_state