import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Lego Propiedades",
            height="40px"
            ),
        position="sticky",
        bg="skyblue",
        padding_x="16px",
        padding_y="8px",
        z_index="999"
    )
