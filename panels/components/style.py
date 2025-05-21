import reflex as rx

def create_link(
    hover_style, text_color, link_url, link_text
):
    """Create a styled link element with hover effects."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover=hover_style,
        color=text_color,
    )
