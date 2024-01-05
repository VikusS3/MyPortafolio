import reflex as rx
from Portafolio_Web.styles.styles import Size
from Portafolio_Web.styles.colors import TextColor

def subtitle(text: str) -> rx.Component:
    return rx.hstack(
        rx.text(text),
        padding_y=5,
        font_size=Size.BIG.value, 
        color=TextColor.PRIMARY.value,
        align_items="center",
    )