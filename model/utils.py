import re

token1 = '@@ПЕРВЫЙ@@'
token2 = '@@ВТОРОЙ@@'


def decode_context(message_history) -> list[str]:
    if type(message_history) == list:
        message_history = ' '.join([message for message in message_history])

    regex = re.escape(token1) + r'|' + re.escape(token2)
    messages = re.split(regex, message_history)
    messages = [message.strip() for message in messages if message]

    return messages


def encode_context(message_history: list[str], last=True) -> str:
    message_history = [message for message in message_history if message is not None]

    res = ''.join([f'{token1}{message_history[i]}' if i % 2 == 0 else f'{token2}{message_history[i]}' for i in
                   range(len(message_history))])

    if last:
        res += token1 if len(message_history) % 2 == 0 else token2

    return res

