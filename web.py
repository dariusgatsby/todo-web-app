import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    # Clear the input box after hitting enter
    st.session_state["new_todo"] = ""


st.title("My Todo app")
st.subheader("Built in Python!")
st.write("First app... Complete!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

text_input = st.text_input(label="", placeholder="Add a todo..",
                           key="new_todo", on_change=add_todo)


