# Import required libraries
from flask import Flask
import os

# Create the Flask application
app = Flask(__name__)


# Define the home page route
@app.route("/")
def home():

    # HTML content displayed on the web page
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My PaaS Application</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                text-align: center;
                padding-top: 100px;
                color: white;
            }

            .container {
                background: white;
                color: #333;
                width: 60%;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            }

            h1 {
                color: #667eea;
                font-size: 40px;
            }

            h2 {
                color: #555;
            }

            p {
                font-size: 18px;
            }

            .status {
                display: inline-block;
                background: #28a745;
                color: white;
                padding: 10px 20px;
                border-radius: 20px;
                margin-top: 15px;
            }

            footer {
                margin-top: 25px;
                font-size: 14px;
                color: #777;
            }
        </style>
    </head>

    <body>

        <!-- Main application container -->
        <div class="container">

            <!-- Application heading -->
            <h1>Hello from PaaS!</h1>

            <!-- Application description -->
            <h2>My First PaaS Web Application</h2>

            <p>
                Created using Python and Flask.
            </p>

            <!-- Application status -->
            <div class="status">
                Application Running Successfully
            </div>

            <!-- Footer -->
            <footer>
                Python + Flask + Cloud PaaS
            </footer>

        </div>

    </body>
    </html>
    """


# Run the application
if __name__ == "__main__":

    # Get the port number provided by the cloud platform.
    # If no port is provided, use port 5000 for local testing.
    port = int(os.environ.get("PORT", 5000))

    # Start the Flask server
    # 0.0.0.0 allows the application to accept external connections.
    app.run(host="0.0.0.0", port=port)
