import gradio as gr
from src.components.chat_interface import chat_interface
from src.utils.api import update_preferences, search_ads
from database.db_query import get_user_by_email, update_user_preferences, get_ads_by_preferences
from database.db_connection import create_user_db_connection

def chat_page(user_data):
    with gr.Blocks() as chat:
        if user_data.value:
            user = get_user_by_email(user_data.value.email)
            if user:
                gr.Markdown(f"# Chat with Multi-Agents - Welcome, {user[0]['name']}!")
                # Create a database connection for the user
                user_credentials = {
                    'dbname': user[0]['dbname'],
                    'user': user[0]['db_user'],
                    'password': user[0]['db_password']
                }
                db_connection = create_user_db_connection(user_credentials)
            else:
                gr.Markdown(f"# Chat with Multi-Agents - Welcome!")
        else:
            gr.Markdown(f"# Chat with Multi-Agents - Welcome!")

        with gr.Row(scale=3):
            chat_interface_instance = chat_interface(user_data.value.user_id)
        with gr.Row(scale=1):
            gr.Markdown("### Relevant Ads")
            ads_output = gr.JSON(label="Ads")

        def update_ads(message):
            if user_data.value:
                update_preferences(user_data.value.email, message, db_connection)
                ads = search_ads(user_data.value.email, db_connection)
                return ads
            return {}

        if chat_interface_instance and hasattr(chat_interface_instance, 'inputs') and chat_interface_instance.inputs:
            chat_interface_instance.inputs[0].submit(update_ads, inputs=[chat_interface_instance.inputs[0]], outputs=[ads_output])
        else:
            print("Warning: Could not find input component in chat interface")

    return chat