from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


class WebhookData(BaseModel):
    function: str
    data: Dict


def create(data):
    return {"message": "Create action"}


def update(data):
    return {"message": "Update action"}


def delete(data):
    return {"message": "Delete action"}


function_map = {
    'create': create,
    'update': update,
    'delete': delete,
}


@app.get("/")
async def read_root():
    return {"message": "Welcome to the webhook API"}


@app.post("/Datalore")
async def handle_webhook(webhook_data: WebhookData):
    function_name = webhook_data.function
    if function_name in function_map:
        response = function_map[function_name](webhook_data.data)
    else:
        response = {"error": "Unknown function"}

    return response
