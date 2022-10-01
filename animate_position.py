from turtle import onclick
import flet
from flet import Container, ElevatedButton, Page, Stack, animation

def main(page: Page):
    c1 = Container(
        width=50,
        height=50,
        left=-100,
        bgcolor='red',
        animate_position=animation.Animation(duration=3000, curve='easeOut'),
    )
    
    c2 = Container(
        width=50,
        height=50,
        top=60,
        left=0,
        bgcolor='green',
        animate_position=True,
    )

    c3 = Container(
        width=50,
        height=50,
        top=120,
        left=0,
        bgcolor='blue',
        animate_position=animation.Animation(duration=1000, curve='bounceOut')
    )

    def animate_container(e):
        c1.top = 20
        c1.left = 0
        c2.top = 100
        c2.left = 40
        c3.top = 180
        c3.left = 100
        page.update()

    page.add(
        Stack(controls=[c1, c2, c3], height=250),
        ElevatedButton('Animage', on_click=animate_container)
    )

flet.app(target=main)