# import gradio as gr
# from ..utils.api import send_message_to_agents

# def chat_interface(user_id, visible:bool = True):
#     with gr.Group(visible=visible):
#         gr.Markdown("# Chat with AI Agents")
#         chatbot = gr.Chatbot()
#         msg = gr.Textbox()
#         clear = gr.Button("Clear")

#     def user(user_message, history):
#         return "", history + [[user_message, None]]

#     def bot(history):
#         user_message = history[-1][0]
#         bot_message = send_message_to_agents(user_id, user_message)
#         history[-1][1] = bot_message
#         return history

#     msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
#         bot, chatbot, chatbot
#     )
#     clear.click(lambda: None, None, chatbot, queue=False)

#     return gr.Column([chatbot, msg, clear])

import gradio as gr

def chat_interface():
    return gr.Chatbot(label="Multi-Agent Chat")