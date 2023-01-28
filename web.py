import streamlit as st
import fuctions

todo_list = fuctions.read_file()


def add_todo():
    item = st.session_state["new_todo"] + "\n"
    item = item.title()
    todo_list.append(item)
    fuctions.write_file(todo_list)



st.title("Mstr's todo app")
st.subheader("Dont forget anything ever again!")

for index, i in enumerate(todo_list):
    i = i.title()
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        todo_list.pop(index)
        fuctions.write_file(todo_list)
        del st.session_state[i]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add a New Item to the  List...", on_change=add_todo, key='new_todo')
