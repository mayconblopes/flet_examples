import flet
from flet import Container, ElevatedButton, Page, animation, transform


def main(page: Page):
    c = Container(
        width=1000,
        height=100,
        bgcolor='blue',
        border_radius=10,
        offset=transform.Offset(-2, 0),
        animate_offset=animation.Animation(1000),
    )

    def animate(e):
        offset = 0 if c.offset == transform.Offset(-2, 0) else -2
        c.offset = transform.Offset(offset, 0)
        c.update()
    
    page.vertical_alignment = 'center'
    page.add(
        c,
        ElevatedButton('Menu', on_click=animate)
    )

flet.app(target=main)
