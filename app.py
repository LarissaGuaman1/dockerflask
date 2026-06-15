from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Flask</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #7c3aed, #38bdf8);
                color: white;
            }

            .card {
                background: rgba(255, 255, 255, 0.15);
                padding: 40px;
                border-radius: 25px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(10px);
            }

            h1 {
                font-size: 45px;
                margin-bottom: 15px;
            }

            p {
                font-size: 20px;
                margin-bottom: 25px;
            }

            .badge {
                display: inline-block;
                padding: 12px 20px;
                border-radius: 20px;
                background: white;
                color: #7c3aed;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Hola Mundo! 🚀</h1>
            <p>Servicio Flask ejecutándose correctamente con Docker.</p>
            <div class="badge">Flask + Docker</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)