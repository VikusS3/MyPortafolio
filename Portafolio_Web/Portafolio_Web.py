import reflex as rx
import Portafolio_Web.styles.styles as styles
from Portafolio_Web.views.navbar import navbar
from Portafolio_Web.views.header import header
from Portafolio_Web.views.skills import skills
from Portafolio_Web.views.projects import projects
from Portafolio_Web.views.subtitle_project import subtitle_project
from Portafolio_Web.views.subtitle_skills import subtitle_skills
from Portafolio_Web.views.footer import footer


def index()-> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                subtitle_skills(),
                skills(),
                subtitle_project(),
                projects(),
                footer(),
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
    description= "VikusDEV es un programador freelance que se dedica al desarrollo web, diseño web, desarrollo de aplicaciones, desarrollo de software, entre otros.",
)
app.compile()