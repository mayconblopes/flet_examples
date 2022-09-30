from turtle import color, width
import flet
from flet import ElevatedButton, Page, AppBar, Text, Column, colors, FilledButton, icons, IconButton, OutlinedButton

def main(page: Page):
    page.title = 'Botões no Flet' 
    page.vertical_alignment='center'
    page.horizontal_alignment='center'
    page.appbar = AppBar(
        bgcolor='#034582',
        color='#ffffff',
        center_title=True,
        title=Text(value='Tipos de Botões no Flet')
    )

    page.add(
        Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                ElevatedButton(text='ElevatedButton', bgcolor=colors.AMBER, color=colors.BLACK, height=35, width=150),
                FilledButton(text='FilledButton', icon=icons.APPS),
                IconButton(icon=icons.SMART_BUTTON, icon_color=colors.INDIGO),
                OutlinedButton(text='Outline Button')
            ]
        )
    )

flet.app(target=main, port=8000)