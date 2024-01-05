import reflex as rx
from Portafolio_Web.components.subtitle import subtitle

def subtitle_project() -> rx.Component:
    return rx.box(
        rx.center(
            subtitle("Proyectos"),
            padding_top="1.5em",
        ),
    )