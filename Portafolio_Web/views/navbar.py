import reflex as rx
from Portafolio_Web.styles.styles import Size
from Portafolio_Web.components.link_icon import link_icon
from Portafolio_Web.styles.colors import Color, TextColor
import Portafolio_Web.constants as constants

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="logo.png",
                alt="Imagen con las letras VD",
                width=Size.BIG.value,
                height=Size.BIG.value,      
            ),
            rx.text("VikusDEV"),
            rx.spacer(),
            
            rx.tablet_and_desktop(
                link_icon(
                    "linkedin",
                    constants.LINKEDIN_URL,  
                ),  
            ),
            link_icon(
                "github",
                 constants.GITHUB_URL,
            ),
            link_icon(
                "twitter",
                constants.TWITTER_X_URL,
            ),
            width="100%",           
        ),
        position="sticky",
        bg=Color.BACKGROUND.value,
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index=999,
        top=0,
        width="100%",
          
    )
    