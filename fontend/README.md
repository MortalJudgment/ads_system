# Frontend using Gradio

This project uses Gradio to create a web interface for the multi-agent system.

## Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── chat_interface.py
│   │   ├── login.py
│   │   └── interest_selection.py
│   ├── pages/
│   │   ├── home_page.py
│   │   ├── chat_page.py
│   │   └── user_preferences_page.py
│   ├── styles/
│   │   └── style.css
│   └── utils/
│       ├── api.py
│       └── helpers.py
├── public/
│   └── index.html
├── .gitignore
├── requirements.txt
└── README.md
```
##
Require 3.10 <= Python version <= 3.13 

## Setup

1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    pip install 'crewai[tools]'
    ```
2. Run the application:
    ```sh
    python run_fontend.py
    ```

## Features
1. Login with user details and interests.

2. Chat interface for interacting with the multi-agent system.

3. Update user preferences based on user queries.

## Status
On process
