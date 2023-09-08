import requests
from aiogram import Router, types
from aiogram import F

import config
import json

router = Router()


contexts = {int, list[str]}


@router.message(F.text)
async def message_handler(message: types.Message):
    model_response = requests.post(
        config.MODEL_API,
        json={
            "message": message.text
        }
    ).json()

    answer = model_response

    await message.answer(answer)
