from fastapi import FastAPI
from api.middleware.response_middleware import response_standardize_middleware

app = FastAPI()
app.mount('http')(response_standardize_middleware)
