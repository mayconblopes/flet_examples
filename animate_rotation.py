import flet
from flet import Container, ElevatedButton, Page, alignment, animation, transform
from math import pi


def main(page: Page):
    c = Container(
        width=100,
        height=70,
        bgcolor='blue',
        border_radius=5,
        rotate=transform.Rotate(0, alignment=alignment.center),
        animate_rotation=animation.Animation(duration=300, curve='bounceOut'),
    )

    def animate(e):
        # 2pi == 360°; 1pi == 180°; pi/2 == 90°
        c.rotate.angle += pi / 2
        page.update()

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 30
    page.add(
        c,
        ElevatedButton('Animate!', on_click=animate),
    )

flet.app(target=main)