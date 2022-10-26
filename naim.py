from dearpygui.dearpygui import *

def save_calback(sender, data):
    print('Click')

create_context()
create_viewport(title='Title', width=700, height=500)

with window(label='Window', width=600, height=400):
    add_text('Hello, world!')
    add_button(label='Save', callback=save_calback)
    add_input_text(label='string', default_value='Default text')
    add_slider_float(label='float', default_value=0.5, max_value=1)
    add_menu(label='Langage')
    add_table(label='Users', width=100, height=75)

setup_dearpygui()
show_viewport()
start_dearpygui()
