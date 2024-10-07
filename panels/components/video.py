import reflex as rx

def create_youtube_iframe(source):
    """Creates an iframe element for embedding a YouTube video with specific styling and attributes."""
    return rx.el.iframe(
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
        allowfullscreen=True,
        frameborder="0",
        src=source,
        position="absolute",
        height="100%",
        left="0",
        border_radius="0.5rem",
        top="0",
        width="100%",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    )


def create_continue_button():
    """Creates a styled 'Continue to Site' button with hover effects and custom properties."""
    return rx.el.button(
        "Continue to Site",
        id="continue-button",
        class_name="transform",
        background_color="#2563EB",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        font_weight="700",
        _hover={
            "background-color": "#1D4ED8",
            "transform": "scale(1.05)",
        },
        margin_top="1.5rem",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        width="100%",
    )

def create_video_container(source):
    """Creates a container for the YouTube video and continue button with backdrop blur effect."""
    return rx.box(
        rx.box(
            create_youtube_iframe(source),
            padding_bottom="56.25%",
            position="relative",
        ),
        create_continue_button(),
        class_name="backdrop-filter glow",
        backdrop_blur="blur(4px)",
        background_color="#ffffff1a",
        max_width="56rem",
        padding="2rem",
        position="relative",
        border_radius="0.5rem",
        width="100%",
    )

def video_container(source):
    """Creates a container for the YouTube video and continue button with backdrop blur effect."""
    return rx.box(
        rx.box(
            create_youtube_iframe(source),
            padding_bottom="56.25%",
            position="relative",
        ),
        class_name="backdrop-filter glow",
        backdrop_blur="blur(4px)",
        background_color="#ffffff1a",
        max_width="56rem",
        padding="2rem",
        position="relative",
        border_radius="0.5rem",
        width="100%",
    )


def create_close_button():
    """Creates a close button with an 'X' icon and hover effects."""
    return rx.el.button(
        rx.icon(
            alt="Close",
            tag="x",
            height="2rem",
            width="2rem",
        ),
        position="absolute",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _hover={"color": "#D1D5DB"},
        right="1rem",
        color="#ffffff",
        top="1rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )


def create_main_content():
    """Creates the main content area with video container, close button, and diamond animation script."""
    return rx.box(
        rx.box(
            id="diamonds-container",
            position="absolute",
            top="0",
            right="0",
            bottom="0",
            left="0",
            pointer_events="none",
        ),
        create_video_container(),
        create_close_button(),
        rx.script(
            """
    const diamondsContainer = document.getElementById('diamonds-container');
    const continueButton = document.getElementById('continue-button');

    function createDiamond() {
        const diamond = document.createElement('div');
        diamond.classList.add('diamond');
        diamond.style.left = `${Math.random() * 100}vw`;
        diamond.style.animationDuration = `${Math.random() * 2 + 2}s`;
        diamondsContainer.appendChild(diamond);
        setTimeout(() => diamond.remove(), 3000);
    }

    function createDiamonds() {
        for (let i = 0; i < 30; i++) {
            setTimeout(createDiamond, Math.random() * 1500);
        }
    }

    continueButton.addEventListener('click', createDiamonds);
"""
        ),
        class_name="animated-bg",
        display="flex",
        height="100vh",
        align_items="center",
        justify_content="center",
        overflow="hidden",
    )


def create_animated_background_page():
    """Creates the main page with an animated background, YouTube video, and interactive elements."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .animated-bg {
            background: linear-gradient(45deg, #ff6b6b, #feca57, #ff9ff3);
            background-size: 400% 400%;
            animation: gradientAnimation 15s ease infinite;
        }
        .glow {
            box-shadow: 0 0 15px 5px rgba(255, 165, 0, 0.7);
        }
        @keyframes fall {
            0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
        }
        .diamond {
            position: absolute;
            width: 20px;
            height: 20px;
            background-color: rgba(255, 255, 255, 0.8);
            transform: rotate(45deg);
            animation: fall 3s linear infinite;
        }
    """
        ),
        create_main_content(),
    )