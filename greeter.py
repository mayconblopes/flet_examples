import flet
from flet import ElevatedButton, Text, TextField, Page

def main(page: Page):
    def btn_click(e):
        
        # validate txt_name.value to avoid empty field
        if not txt_name.value:
            txt_name.error_text = 'Please enter your name'
            page.update()

        else:
            name = txt_name.value
            page.clean()
            page.add(Text(f'Hello, {name}!'))
    
    txt_name = TextField(label='Your name')


    page.add(txt_name, ElevatedButton('Say hello!', on_click=btn_click))

flet.app(target=main)