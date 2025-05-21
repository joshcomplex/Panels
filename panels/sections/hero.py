#imports
import reflex as rx
from panels.components.video import video_container
from panels.sections.form import registration_form
def hero_primary_button():
    """Create a 'Get Started' button with hover effects."""
    return rx.el.a(
        "Get Started", #TODO: retrieve from backend table
        href="#",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "orange"},
        display="inline-block",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        color="#2563EB",
        transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )

def hero_secondary_button():
    """Create a 'Learn More' button with hover effects."""
    return rx.el.a(
        "Learn More", #TODO: retrieve from backend table
        href="#", #TODO: retrieve from backend table
        background_color="DBEAFE",
        border_width="2px",
        border_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={ 
            "background-color": "#ffffff",
            "color": "#2563EB",
        },
        display="inline-block",
        padding_left="2rem",
        padding_right="2rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="9999px",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
#        color="#ffffff",
        transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )

def hero_section():
    """Create the hero section with heading, description, and call-to-action buttons."""
    return rx.box(
        rx.heading(
            "Revolutionize Full Stack with Reflex", #TODO: retrieve from backend table
            font_weight="700",
            margin_bottom="1.5rem",
            font_size=rx.breakpoints(
                {"0px": "2.25rem", "768px": "3rem"}
            ),
            line_height=rx.breakpoints(
                {"0px": "2.5rem", "768px": "1"}
            ),
#            color="#ffffff",
            as_="h1",
        ),
        rx.text(
            "Harness the power of artificial intelligence to drive innovation, efficiency, and growth in your organization.", #TODO: retrieve from backend table
            margin="2rem",
            font_size=rx.breakpoints(
                {"0px": "1.125rem", "768px": "1.25rem"}
            ),
            line_height=rx.breakpoints(
                {"0px": "1.75rem", "768px": "1.75rem"}
            ),
#            color="#ffffff",
        ),
        rx.flex(
            hero_primary_button(),
            hero_secondary_button(),
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "640px": "row"}
            ),
            justify_content="center",
            gap=rx.breakpoints(
                {"0px": "1rem", "640px": "0"}
            ),
            column_gap=rx.breakpoints({"640px": "1rem"}),
        ),
        max_width="56rem",
        margin_left="auto",
        margin_right="auto",
        text_align="center",
    )

def hero(type=None, source=None):
    content = hero_section()
    if type == "image" and source:
        content = rx.flex(
            content,
            rx.box(
            rx.image(
                alt="Hero Section Image",
                src=source,
                border_radius="0.5rem",
                box_shadow="0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
            ),
            width=rx.breakpoints({"768px": "50%"}),
        ),
        id="hero",
        display="flex",
        flex_direction=rx.breakpoints(
            {"0px": "column", "768px": "row"}
        ),
        align_items="left",
        margin_bottom="3rem",
        text_align="left",
    )
    elif type == "video" and source:
        content = rx.flex(
            content,
            video_container(source),
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "768px": "row"}
            ),
            align_items="left",
            margin_bottom="3rem",
            text_align="left",
        )
    elif type == "form" and source:
        content = rx.flex(
            content,
            registration_form(source),  # Assuming source is a function call like registration(contest)
            display="flex",
            flex_direction=rx.breakpoints(
                {"0px": "column", "768px": "row"}
            ),
            align_items="left",
            margin="3rem",
            text_align="left",
        )

    return rx.box(
        content,
        class_name="hero",
        backdrop_blur="blur(12px)",
        background_color="#DBEAFE4d",
        margin="2rem",
        padding="3rem",
        border_radius="0.75rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    )
