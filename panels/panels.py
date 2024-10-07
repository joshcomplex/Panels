"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from panels.sections.hero import hero
from panels.sections.form import registration_form, beta_signup
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.section(
        rx.color_mode.button(position="top-right"),
        hero(type="video", source="https://www.youtube.com/embed/dQw4w9WgXcQ"),
        hero(type="image", source="https://placehold.co/600x400"),
        hero(type="form", source=registration_form(beta_signup())),
#        features(),
#        showcase(),
#        chat(),
#        pricing(),
#        faq(),
#        cta(),
    )

app = rx.App()
app.add_page(index)
