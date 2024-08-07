import reflex as rx


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.hstack(
        rx.text("Lego Propiedades", height="40px"), position="sticky", bg="blue"
    )


app = rx.App()
app.add_page(index)
app._compile()
