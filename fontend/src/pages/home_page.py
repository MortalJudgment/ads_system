import gradio as gr
from components.login import login_interface
from fontend.src.components.ad_interface import interest_selection

def home_page():
    with gr.Blocks() as home:
        gr.Markdown("# Welcome to Multi-Agent Chat App", elem_id="center-title")
        
        login_block = login_interface()
        interests = interest_selection()
        interests.visible = False
        
        def on_login(user_data):
            if user_data:
                return gr.update(visible=False), gr.update(visible=True), user_data
            return gr.update(visible=True), gr.update(visible=False), None

        login_components = [component for component in login_block.children if isinstance(component, gr.components.Component)]
        output_component = next((component for component in login_components if isinstance(component, gr.JSON)), None)

        if output_component:
            output_component.change(on_login, inputs=[output_component], outputs=[login_block, interests, interests])
        else:
            print("Warning: Could not find JSON output component in login interface")

    return home

# To launch the interface, you can call:
# iface = home_page()
# iface.launch()
