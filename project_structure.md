```
    ads_system/
    ├── backend/
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── main.py
    │   │   ├── models.py
    │   │   ├── schemas.py
    │   │   ├── crud.py
    │   │   ├── database.py
    │   │   └── auth/
    │   │       ├── __init__.py
    │   │       └── authentication.py
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   └── test_app.py
    │   ├── README.md
    │   ├── requirements.txt
    │   └── Dockerfile
    ├── data/
    │   └── data_ads/
    │       ├── data_ads.json
    │       └── upload_ads_data.py
    ├── database/
    │   ├── __init__.py
    │   ├── db_connection.py
    │   └── db_queries.py
    ├── frontend/
    │   ├── src/
    │   │   ├── components/
    │   │   │   ├── __init__.py
    │   │   │   ├── chat_interface.py
    │   │   │   ├── login_interface.py
    │   │   │   ├── advance_setting.py
    │   │   │   └── ad_interface.py
    │   │   ├── pages/
    │   │   │   ├── __init__.py
    │   │   │   ├── home_page.py
    │   │   │   ├── chat_page.py
    │   │   │   └── ad_page.py
    │   │   ├── utils/
    │   │   │   ├── __init__.py
    │   │   │   ├── api.py
    │   │   │   └── helpers.py
    │   │   ├── public/
    │   │   │   └── index.html
    │   │   ├── styles/
    │   │   │   └── style.css
    │   │   └── multi_agents
    │   │   │   ├── __init__.py
    │   │   │   ├── agents.py
    │   │   │   ├── crew.py
    │   │   │   ├── tools.py
    │   │   └── └── tasks.py
    │   ├── .gitignore
    │   ├── requirements.txt
    │   ├── run_fontend.py
    │   └── README.md
    ├── app.py
    ├── .env
    ├── .gitignore
    ├── docker-compose.yml
    └── README.md
```