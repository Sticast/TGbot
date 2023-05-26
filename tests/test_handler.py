import pytest

from unittest.mock import AsyncMock

from handlers.users.echo import bot_echo
from handlers.users.help import bot_help


@pytest.mark.asyncio
async def test_echo_handler():
    text_mock = "repeat me"
    message_mock = AsyncMock(text=text_mock)
    await bot_echo(message=message_mock)
    message_mock.answer.assert_called_with(text_mock)


@pytest.mark.asyncio
async def test_help_handler():
    text_mock = "Список команд: \n/start - Начать диалог\n/help - Получить справку"
    message_mock = AsyncMock(text=text_mock)
    await bot_help(message=message_mock)
    message_mock.answer.assert_called_with(text_mock)
