import reflex as rx
import Portafolio_Web.styles.styles as styles
from Portafolio_Web.views.navbar import navbar
from Portafolio_Web.views.header import header


def index()-> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                widht="100%",
                spacing=styles.Size.BIG.value,
            ),    
        ),
    )
    

    
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="VikusDEV - Programador Full Stack",
    description= "VikusDEV es un programador freelance que se dedica al desarrollo web, diseño web, desarrollo de aplicaciones, desarrollo de software, desarrollo de apl"
)
app.compile()