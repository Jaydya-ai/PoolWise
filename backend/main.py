from fastapi import FastAPI

app = FastAPI(title='PoolWise Backend')

@app.get('/')
def root():
    return {'message': 'PoolWise backend running successfully'}

