import reflex as rx
from Portafolio_Web.styles.styles import Size
from Portafolio_Web.styles.colors import Color, TextColor
import Portafolio_Web.constants as constants
from Portafolio_Web.components.button import button
import Portafolio_Web.styles.styles as styles


def projects() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.image(
                padding_y=Size.BIG.value,
                src="/imgs/delivery.png",
                alt="Imagen de un menu lateral a la izquierda y un mapa a la derecha con una ruta trazada",
                widht="11em",
                height="22em",
                margin_right=Size.BIG.value,  
            ),
            rx.vstack(
                rx.box(
                    rx.text("BooFast", font_size=Size.BIG.value, color=TextColor.ACCENT.value),
                    rx.text("Aplicacion para delivery", font_size=Size.MEDIUM.value, color=TextColor.ACCENT.value),
                    class_name="nes-balloon from-left is-dark"  
                ),
                rx.span(
                    "Aplicación para Delivery, la cual permite a los clientes realizar pedidos y a los repartidores realizar entregas",
                ),
                rx.span(
                    "Desarrollada con php, html, css, javascript, boostrap, jquery, ajax, mysql, entre otros",
                ),
                button(
                    "Ver proyecto",
                    f"{constants.DELIVERY_REPO_URL}"
                ),
                align_items="start",   
            ),
            direction=styles.FLEX_DIRECTION,
        ),
        rx.text(""),
        rx.flex(
            rx.image(
                padding_y=Size.BIG.value,
                src="/imgs/mecawash.png",
                alt="Imagen de un menu lateral a la izquierda y unos graficos a la derecha",
                widht="11em",
                height="22em",
                margin_right=Size.BIG.value,  
            ),
            rx.vstack(
                rx.box(
                    rx.text("MecaWash", font_size=Size.BIG.value, color=TextColor.ACCENT.value),
                    rx.text("Aplicacion para lavado,repacion y pintado de autos", font_size=Size.MEDIUM.value, color=TextColor.ACCENT.value),
                    class_name="nes-balloon from-left is-dark"  
                ),
                rx.span(
                    "Aplicacion para el lavada de autos, mecanica, entre otros, la cual permite llevar un control de los clientes, servicios realizados, entre otros",
                ),
                rx.span(
                    "Desarrollada en C#, ASP.NET, HTML, CSS, Javascript, Boostrap, SQL Server, entre otros",
                ),
                button(
                    "Ver proyecto",
                    f"{constants.MECAWASH_REPO_URL}"
                ),
                align_items="start",
            ),
            direction=styles.FLEX_DIRECTION,   
        ),
        padding_top=Size.VERY_BIG.value,
        #separar cada flex con un espacio
        spacing=Size.VERY_BIG.value,
        style=styles.max_width_style
    )