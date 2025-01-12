import streamlit as st
import functions as fy

st.title("My TodoApp")
st.subheader("This is my TodoApp")
st.write("This app is here to increase your productivity")


def add_todo():
    todo_i = st.session_state['new_todo'] + "\n"
    todos_list.append(todo_i)
    fy.write_todos(todos_list)


todos_list = fy.get_todos()

#Displaying checkbox stuff

for index, todo in enumerate(todos_list):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos_list.pop(index)
        fy.write_todos(todos_list)
        del st.session_state[todo]
        st.rerun()


#User Input

st.text_input(label="", placeholder="Enter your Todo..", on_change=add_todo, key='new_todo')
