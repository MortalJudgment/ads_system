# import gradio as gr
# from ..utils.api import login_user
# import re

# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return re.match(pattern, email) is not None

# def login(name, age, email, interests):
#     if not name or not age or not email:
#         return False, "Please fill in all fields"
    
#     if len(interests) < 2:
#         return False, "Please select at least 2 interests."

#     if not validate_email(email):
#         return False, "Please enter a valid email address."
    
#     try:
#         age = int(age)
#         if age < 5 or age > 120:
#             return False, "Please enter a valid age between 5 and 120."
#     except ValueError:
#         return False, "Please enter a valid age."
    
#     # if login_user(email, password): 
#     #     return True, "Login successful"
#     # else:
#     #     return False, "Please log in  first"
#     return True, "Login successful"

# def login_interface(visible : bool = True):
#     with gr.Group(visible=visible):
#         gr.Markdown("# Login")
#         name_input = gr.Textbox(label="Name")
#         age_input = gr.Number(label="Age")
#         email_input = gr.Textbox(label="Email")
#         interests = gr.CheckboxGroup(
#             ["Sports", "Travel", "Technology", "Food", "Music", "Movies", "Art", "Science", "Fashion", "Books"],
#             label="Interests (select at least 2)"
#         )
#         login_button = gr.Button("Login")
#         success_indicator = gr.Textbox("Login Success")

#     def login(name, age, email, interests):
#         # Your login logic here
#         # For demonstration, let's assume login is successful if all fields are filled
#         if name and age and email and len(interests) >= 2:
#             return True
#         return False

#     login_button.click(
#         login,
#         inputs=[name_input, age_input, email_input, interests],
#         outputs=success_indicator
#     )

#     return gr.Group([name_input, age_input, email_input, interests, login_button, success_indicator])


import gradio as gr

def login_interface():
    with gr.Group() as login_group:
        name_input = gr.Textbox(label="Name")
        age_input = gr.Number(label="Age")
        email_input = gr.Textbox(label="Email")
        interests = gr.CheckboxGroup(
            ["Sports", "Travel", "Technology", "Food", "Music", "Movies", "Art", "Science", "Fashion", "Books"],
            label="Interests (select at least 2)"
        )
        login_button = gr.Button("Login")
    return [name_input, age_input, email_input, interests, login_button]