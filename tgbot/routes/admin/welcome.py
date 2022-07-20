from aiogram import Router
from aiogram.types import Message

from tgbot.filters.role import Role_Filter
from tgbot.models.role import UserRole


admin_welcome_router = Router()

# Can use other variants:
# @admin_welcome_router.message(Role_Filter(user_role=[UserRole.ADMIN]), commands=["check"])
# @admin_welcome_router.message(Role_Filter(user_role=[UserRole.ADMIN, UserRole.USER]), commands=["check"])
@admin_welcome_router.message(Role_Filter(user_role=UserRole.ADMIN), commands=["admin"])
async def admin_welcome(message: Message) -> None:
    await message.reply("Привет, Администратор! Вы успешно прошли авторизацию.")
