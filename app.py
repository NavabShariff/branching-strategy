from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    environment = os.getenv("ENV_NAME", "dev")
    sprint_version = "sprint-1"  # Add the sprint version here
    return f"""
    <html>
        <head>
            <style>
                body {{
                    background-color: #f0f0f0;  /* Light grey background */
                    text-align: center;          /* Center text */
                    font-family: Arial, sans-serif; /* Font style */
                }}
                h1 {{
                    color: green;                /* Text color */
                    font-size: 48px;            /* Increased font size */
                }}
                h2 {{
                    color: blue;                 /* Color for the sprint version */
                    font-size: 36px;            /* Font size for the sprint version */
                }}
            </style>
        </head>
        <body>
            <h1>This is {environment} environment</h1>
            <h2>{sprint_version}</h2>  <!-- Display the sprint version -->
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # Bind to all interfaces