import reflex as rx
import Portafolio_Web.styles.styles as styles
from Portafolio_Web.views.navbar import navbar


def index()-> rx.Component:
    return rx.box(
        navbar(),
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