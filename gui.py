import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
inputbox = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To_do App', layout=[[label], [inputbox, add_button]])

window.read()
window.close()
