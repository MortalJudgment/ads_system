# AdChat Frontend

This is the frontend part of the AdChat application, which is a multi-agent chat application with personalized ads. This project uses React for the frontend.


## Structure

```
frontend/
├── public/
│   ├── index.html           # Main HTML file
│   └── favicon.ico          # Favicon for the web app
├── src/
│   ├── components/
│   │   ├── Login/
│   │   │   ├── Login.js     # Login component logic
│   │   │   └── Login.css    # Styling for Login component
│   │   ├── ChatApp/
│   │   │   ├── ChatApp.js        # Main ChatApp component
│   │   │   ├── ChatApp.css       # Styling for ChatApp
│   │   │   ├── ChatWindow.js     # Component for displaying chat messages
│   │   │   └── MessageInput.js   # Component for user to input messages
│   │   ├── AdDisplay/
│   │   │   ├── AdDisplay.js  # Component to display ads
│   │   │   └── AdDisplay.css # Styling for AdDisplay
│   │   ├── InterestSelector/
│   │   │   ├── InterestSelector.js  # Component for user to select interests
│   │   │   └── InterestSelector.css # Styling for InterestSelector
│   │   └── MultiAgents/
│   │       ├── agents.py     # Definitions for crewai agents
│   │       ├── crew.py       # Crew AI management
│   │       ├── tasks.py      # Task definitions for agents
│   │       └── tool.py       # Utility functions for agents
│   ├── services/
│   │   ├── api.js           # Functions to interact with backend APIs
│   │   └── authService.js   # Functions to handle authentication
│   ├── contexts/
│   │   ├── UserContext.js   # Context to manage user state
│   │   └── ChatContext.js   # Context to manage chat state
│   ├── hooks/
│   │   └── useChat.js       # Custom hook to manage chat functionality
│   ├── utils/
│   │   └── validators.js    # Utility functions for input validation
│   ├── app/
│   │   ├── App.js           # Main application component
│   │   └── App.css          # Global styling for the application
│   ├── index.js             # Entry point for the React application
│   └── index.css            # Global CSS imports
├── .gitignore               # Git ignore file
├── package.json             # NPM package file
├── README.md                # Project documentation
└── requirements.txt         # Python requirements (including crewai)
```
##
Require 3.10 <= Python version <= 3.13 

## Getting Started

### Prerequisites

- Node.js (version 18 or later)
- npm (version 6 or later)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/adchat-frontend.git
    cd adchat-frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

### Running the Application

1. Start the development server:
    ```sh
    npm start
    ```

2. Open your browser and navigate to `http://localhost:3000`.

### Building for Production

1. Build the application:
    ```sh
    npm run build
    ```

2. The build output will be in the `build/` directory.

### Running with Docker

1. Build the Docker image:
    ```sh
    docker build -t adchat-frontend .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 3000:3000 adchat-frontend
    ```

3. Open your browser and navigate to `http://localhost:3000`.

## Project Structure

- `public/`: Public assets and the HTML template.
- `src/`: React application source code.
  - `components/`: React components.
  - `contexts/`: React context providers.
  - `hooks/`: Custom React hooks.
  - `services/`: API service functions.
  - `app/`: Main App component and CSS.
- `package.json`: Project configuration and dependencies.
- `Dockerfile`: Docker configuration for the frontend.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.