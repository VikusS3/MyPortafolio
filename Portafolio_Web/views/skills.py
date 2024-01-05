import reflex as rx
from Portafolio_Web.components.image_skill import image_skill
from Portafolio_Web.styles.styles import Size

def skills() -> rx.Component:
    return rx.box(
        rx.grid(
            image_skill(
                "/imgs/python.png",
                "Python",
            ),
            image_skill(
                "/imgs/js.png",
                "JavaScript",
            ),
            image_skill(
                "/imgs/html.png",
                "HTML",
            ),
            image_skill(
                "/imgs/css.png",
                "CSS",
            ),
            image_skill(
                "/imgs/git.png",
                "Git",
            ),
            image_skill(
                "/imgs/sql.png",
                "SQL",
            ),
            image_skill(
                "/imgs/mongodb.png",
                "MongoDB",
            ),
            image_skill(
                "/imgs/aws.png",
                "AWS",
            ),
            image_skill(
                "/imgs/boostrap.png",
                "boostrap",
            ),
            image_skill(
                "/imgs/shisharp.png",
                "C#",
            ),
             image_skill(
                "/imgs/php.png",
                "PHP",
            ),
            image_skill(
                "/imgs/mysql.png",
                "MySQL",
            ),
            template_columns="repeat(4, 1fr)",
            gap=9,
        ),
    )
    
