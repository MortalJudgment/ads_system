import sys
import os

# Add the src directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import gradio as gr
from fontend.src.components.login import login_interface
from fontend.src.components.chat_interface import chat_interface

def main():
    with gr.Blocks() as app:
        user_id = gr.State(None)

        login_component = login_interface()
        chat_component = chat_interface(user_id)

        # Initially, only show login
        chat_component.visible = False

        def on_login(result):
            if "successful" in result:
                user_id.value = 1  # In a real app, you'd get this from the login response
                login_component.visible = False
                chat_component.visible = True
            return result

        login_component.submit(on_login, inputs=login_component, outputs=login_component)

    app.launch()

if __name__ == "__main__":
    main()

