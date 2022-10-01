from turtle import width
import flet
from flet import Container, ElevatedButton, Page, animation

def main(page: Page):
    c = Container(
        width=150,
        height=150,
        bgcolor='red',
        animate=animation.Animation(duration=1000, curve='bounceOut'),
    )

    def animate_container(e):
        c.width = 100 if c.width == 150 else 150
        c.height = 50 if c.height == 150 else 150
        c.bgcolor = 'blue' if c.bgcolor == 'red' else 'red'
        c.update()

    page.add(c, ElevatedButton('Animate container', on_click=animate_container))

flet.app(target=main)
        
