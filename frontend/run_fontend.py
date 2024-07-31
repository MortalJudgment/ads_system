# run_frontend.py

import gradio as gr
from src.components.login_interface import login_interface
from src.components.chat_interface import chat_interface
from src.components.ad_interface import ad_interface
from src.components.advance_setting import advanced_settings
from src.utils.api import authenticate_user, get_ads
from src.utils.helpers import validate_email, validate_age

def main():
    def login(name, age, email, interests):
        if not name or not age or not email:
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), "Please fill in all fields."
        
        if not validate_email(email):
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), "Invalid email format."
        
        if not validate_age(age):
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), "Age must be a positive integer."
        
        if len(interests) < 2:
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), "Please select at least 2 interests."
        
        if authenticate_user(name, age, email, interests):
            return gr.update(visible=False), gr.update(visible=True), gr.update(visible=True), gr.update(visible=True), ""
        else:
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), "Login failed. Please try again."

    def update_ads(chat_history):
        new_ads = get_ads(chat_history)
        return gr.update(value=new_ads)

    with gr.Blocks() as app:
        with gr.Row():
            with gr.Column(scale=1):
                advanced_settings_box = advanced_settings()
                advanced_settings_box.visible = False
            
            with gr.Column(scale=2):
                login_container = gr.Column(visible=True)
                with login_container:
                    login_components = login_interface()
                
                chat_box = chat_interface()
                chat_box.visible = False
            
            with gr.Column(scale=1):
                ad_box = ad_interface()
                ad_box.visible = False

        login_button = login_components[-1]  # Assuming the login button is the last element
        login_message = gr.Markdown()

        login_button.click(
            login,
            inputs=[*login_components[:-1]],  # All inputs except the button
            outputs=[login_container, chat_box, ad_box, advanced_settings_box, login_message]
        )

        # Update ads when chat history changes
        chat_box.change(
            update_ads,
            inputs=[chat_box],
            outputs=[ad_box]
        )
    
    app.launch()

if __name__ == "__main__":
    main()