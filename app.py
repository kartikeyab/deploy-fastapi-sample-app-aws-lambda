from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get('/hcheck')
def hcheck():
    return {'status': 'Healthy'}


handler = Mangum(app)