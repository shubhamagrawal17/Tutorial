import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return (
        """
        <html>
            <head>
                <title>Azure DevOps Demo</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        padding: 40px;
                        text-align: center;
                    }
                    h1 {
                        color: #2e86de;
                    }
                    p {
                        color: #555;
                    }
                    .highlight {
                        color: #e74c3c;
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <h1>🚀 Hello from
                <span class="highlight">Azure DevOps Pipeline!</span></h1>
                <p>This is a demo Flask app deployed via a CI/CD pipeline.</p>
            </body>
        </html>
        """
    )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # nosec
