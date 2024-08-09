import reflex as rx
from link_bio.components.link_button import link_button


def links() -> rx.Component:
    return rx.hstack(
        link_button("Instagram", "https://www.instagram.com/alexandra.lego.realestate/"),
        link_button("Linkedin", "https://www.linkedin.com/in/yevgeniya-alexandra-legostayeva-6068b925a"),
        link_button("Youtube","https://www.youtube.com/@alexandralegostayeva8147")
    )