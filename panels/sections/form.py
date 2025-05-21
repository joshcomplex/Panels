"""
Prebuilt forms to add to pages.
"""
import reflex as rx
from panels.components.style import create_link

def create_submit_button(button_text, tag, color_scheme):
    """Create a styled submit button for the beta signup form."""
    return rx.button(
        button_text,
        tag=tag,
        color_scheme=color_scheme,

        type="submit",
        
        button = rx.button(on_click=ClickState.change_text)
    )
def create_form_label(label_text):
    """Create a styled label for form inputs."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.25rem",
        color="#374151",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_form_input(input_id, input_name, input_type):
    """Create a styled form input element with focus effects."""
    return rx.el.input(
        type=input_type,
        id=input_id,
        name=input_name,
        required=True,
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "border-color": "#3B82F6",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#3B82F6",
        },
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        width="100%",
    )

def create_form_field(
    label_text, input_id, input_name, input_type
):
    """Create a form field with a label and input element."""
    return rx.box(
        create_form_label(label_text=label_text),
        create_form_input(
            input_id=input_id,
            input_name=input_name,
            input_type=input_type,
        ),
    )

def beta_signup():
    """Create the beta signup form with input fields and submit button."""
    return rx.box(
        rx.form(
            create_form_field(
                label_text="Full Name",
                input_id="name",
                input_name="name",
                input_type="text",
            ),
            create_form_field(
                label_text="Email Address",
                input_id="email",
                input_name="email",
                input_type="email",
            ),
            create_submit_button("Get Early Access"),
            display="flex",
            flex_direction="column",
            gap="1.5rem",
        ),
        rx.text(
            "By joining, you agree to our ",
            create_link(
                hover_style={
                    "text-decoration": "underline"
                },
                text_color="#2563EB",
                link_url="#",
                link_text="Terms of Service",
            ),
            " and ",
            create_link(
                hover_style={
                    "text-decoration": "underline"
                },
                text_color="#2563EB",
                link_url="#",
                link_text="Privacy Policy",
            ),
            ".",
            margin_top="1.5rem",
            text_align="center",
            color="#4B5563",
        ),
        max_width="28rem",
        margin_left="auto",
        margin_right="auto",
    )

def registration_form(form):
    """Create a registration form with a action button."""
    return rx.box(form)
