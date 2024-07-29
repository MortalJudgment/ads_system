# import gradio as gr
# from ..utils.api import get_ads_for_user

# def ad_interface(user_id, visible:bool = True):
#     with gr.Group(visible = visible):
#         gr.Markdown("# Relevant Ads")
#         ads_output = gr.JSON(label="Ads")

#     def update_ads():
#         ads = get_ads_for_user(user_id)
#         return ads

#     ads_output.change(update_ads, outputs=ads_output)

#     return gr.Column([ads_output])

import gradio as gr

def ad_interface():
    return gr.Markdown("Ads will appear here")