from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def hello(name: str = 'Recruto', message: str = 'Давай дружить'):
    return f"""
    <html>
        <head>
            <title>Recruto test</title>
        </head>
        <body>
            <h1>Hello <i>{name}</i>! {message}!</h1>
        </body>
    </html>
    """
