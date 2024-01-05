import reflex as rx
from Portafolio_Web.components.subtitle import subtitle

def subtitle_skills() -> rx.Component:
    return rx.box(
        rx.center(
            subtitle("Habilidades"),
            padding_y="2.5em",
        ),
    )