import reflex as rx
from Portafolio_Web.styles.styles import Size
from Portafolio_Web.components.link_icon import link_icon
from Portafolio_Web.styles.colors import TextColor
import Portafolio_Web.constants as constants
import datetime as dt

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/imgs/img_footer.png",
            alt="Imagen con las letras VD",
            width=Size.BIG.value,
            height=Size.BIG.value,      
        ),
         rx.link(
            f"©copyrigth {dt.datetime.now().year} By VikusDEV",
            href= constants.GITHUB_URL,
            is_external=True,
            font_size=Size.MEDIUM.value,
             #dar color al texto
            color=TextColor.FOOTER_COLOR.value,
        ),
        rx.text(
            "Building with Reflex and Python",
            font_size=Size.MEDIUM.value,
            maring_top=Size.ZERO.value,
           
        ),
        padding_top=Size.BIG.value,
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.ACCENT.value,
        spacing=Size.DEFAULT.value,
        padding_x=Size.BIG.value,
    )
        
        