#imports
import reflex as rx

def create_get_started_button():
    """Create a 'Get Started' button with hover effects."""
    return rx.el.a(
        "Get Started",
        href="#",
        background_color="#ffffff",
        transition_duration="300ms",
        font_weight="600",
        _hover={"background-color": "#DBEAFE"},
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

def create_learn_more_button():
    """Create a 'Learn More' button with hover effects."""
    return rx.el.a(
        "Learn More",
        href="#",
        background_color="transparent",
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
        color="#ffffff",
        transition_property="color, background-color, border-color, text-decoration-color, fill, stroke",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
    )


def create_hero_section():
    """Create the hero section with heading, description, and call-to-action buttons."""
    return rx.box(
        rx.heading(
            "Revolutionize Your Business with AI",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size=rx.breakpoints(
                {"0px": "2.25rem", "768px": "3rem"}
            ),
            line_height=rx.breakpoints(
                {"0px": "2.5rem", "768px": "1"}
            ),
            color="#ffffff",
            as_="h1",
        ),
        rx.text(
            "Harness the power of artificial intelligence to drive innovation, efficiency, and growth in your organization.",
            margin_bottom="2rem",
            font_size=rx.breakpoints(
                {"0px": "1.125rem", "768px": "1.25rem"}
            ),
            line_height=rx.breakpoints(
                {"0px": "1.75rem", "768px": "1.75rem"}
            ),
            color="#ffffff",
        ),
        rx.flex(
            create_get_started_button(),
            create_learn_more_button(),
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
