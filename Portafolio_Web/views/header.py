import reflex as rx
from Portafolio_Web.styles.styles import Size
from Portafolio_Web.styles.colors import Color
import Portafolio_Web.constants as constants
from Portafolio_Web.components.button import button
import Portafolio_Web.styles.styles as styles

def header() -> rx.Component:
    return rx.vstack( 
        rx.flex(
            rx.image(
                src="/imgs/inicio.png",
                alt="Letra V de color blanco sin fondo",
                width="16em",
                height="30em",
                margin_right=Size.BIG.value,  
            ),
            rx.vstack(
                rx.box(
                    rx.text("Programador Full-Stack"),
                    rx.text("Apasionado por la tecnología"),
                    class_name="nes-balloon from-left is-dark"  
                ),
                rx.span(
                    "Hola soy Vikus y soy un programador Full-Stack, me gusta mucho la tecnología", 
                    rx.span(
                        " me destaco por ser autodidacta",
                        color=Color.SECONDARY.value,
                        font_size=Size.DEFAULT.value,  
                    ),
                    "!",
                ),
                rx.span(
                    "Experto en python, php, C#, .NET, html, css, javascript, Database, entre otros",
                ),
                rx.span(
                    "En mi encontraras un programador que se adapta a cualquier situación y que siempre busca la mejor solución",
                ),
                button(
                    "Contactame",
                    f"mailto:{constants.MY_EMAIL}"
                ),
                align_items="start",
            ),
            direction=styles.FLEX_DIRECTION,
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style
    )