from time import sleep
import flet
from flet import Page, Text, Row, TextField, ElevatedButton, Checkbox, Column
from flet.ref import Ref

def main(page: Page):
    t = Text(value='Hello, world', color='green')
    page.controls.append(t)
    # page.update()

    # t2 = Text()
    # page.add(t2)

    # for i in range(10):
    #     t2.value = f'Step {i}'
    #     page.update()
    #     sleep(1)

    page.add(
        Row(controls=[
            Text('A'),
            Text('B'),
            Text('C'),
        ]),

        Row(controls=[
            TextField(label='Your Name'),
            ElevatedButton(text='Say my name!', color='red')
        ])
    )

    # for i in range(10):
    #     page.controls.append(Text(f'Line {i}'))
    #     if i > 4:
    #         page.controls.pop(0)

    def button_clicked(e):
        page.add(Text('Clicked!'))
    
    page.add(ElevatedButton(text='Click me', on_click=button_clicked))

    def add_clicked(e):
        page.add(Checkbox(label=new_task.value))

    new_task = TextField(hint_text='Whats needs to be done?', width=300)

    row = Row([new_task, ElevatedButton('Add', on_click=add_clicked)])
    page.add(row)

    def togle_row(e):
        row.disabled = True if row.disabled == False else False
        page.update()

    page.add(ElevatedButton('Disable', on_click=togle_row))

    first_name = Ref[TextField]()
    last_name = Ref[TextField]()
    greetings = Ref[Column]()

    def btn_click(e):
        greetings.current.controls.append(Text(f'Hello, {first_name.current.value} {last_name.current.value}!'))
        first_name.current.value = ''
        last_name.current.value = ''
        page.update()
        first_name.current.focus()

    page.add(
        TextField(ref=first_name, label='First name', autofocus=True),
        TextField(ref=last_name, label='Last name'),
        ElevatedButton(text='Say hello', on_click=btn_click),
        Column(ref=greetings),
    )


    t = Text(
        value='This is a Text control sample',
        size=30,
        color='white',
        bgcolor='pink',
        weight='bold',
        italic=True,
    )
    page.add(t)

flet.app(target=main, port=8000)