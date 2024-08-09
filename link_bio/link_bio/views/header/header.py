import reflex as rx


def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(fallback="LP", size="8"),
        rx.vstack(
            rx.text("@alexandra.lego.realstate"),
            rx.text("""Hola, soy Alexandra y soy una apasionada asesora
            inmobilaria. Licenciada en Administracion de empresas y 
            proximamente martillera, con amplia experiencia internacional,
            hablo fluidamente 5 idiomas . Mi mayor motivacion es ayudarte 
            con mis conocimientos a lo largo de todo el proceso de compra,
            venta, alquiler o inversion en una propiedad. Mi objetivo es
            que tengas una excelente experiencia, que disfrutes el camino
            y encontremos la propiedad de tus sueños.""")
            )
    )