import reflex as rx
from Portafolio_Web.styles.styles import Size

def image_skill(image: str, alt: str) -> rx.Component:
    return rx.image(
        src=image,
        alt=alt,
        width=Size.ULTRA_BIG.value,
        heigth=Size.ULTRA_BIG.value,
    )