import gradio as gr
from utils.api import get_user_preferences

def user_preferences_page(user_data):
    with gr.Blocks() as preferences:
        gr.Markdown("# User Preferences")
        
        preferences_output = gr.JSON(label="Your current preferences")
        refresh_button = gr.Button("Refresh Preferences")

        def get_preferences():
            return get_user_preferences(user_data['email'])

        refresh_button.click(get_preferences, outputs=[preferences_output])

    return preferences