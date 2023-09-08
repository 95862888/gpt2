import requests
from aiogram import Router, types
from aiogram import F

import config
import json

router = Router()


contexts = {}


@router.message(F.text)
async def message_handler(message: types.Message):
    chat_id = message.chat.id

    if chat_id not in contexts:
        contexts[chat_id] = [message.text]
    else:
        contexts[chat_id].append(message.text)
        contexts[chat_id] = contexts[chat_id][:3]

    model_response = requests.post(
        config.MODEL_API,
        json={
            'context': json.dumps(contexts[chat_id])
        }
    ).json()

    response = model_response

    print(type(response))

    contexts[chat_id].append(response)
    contexts[chat_id] = contexts[chat_id][:3]

    await message.answer(response)
