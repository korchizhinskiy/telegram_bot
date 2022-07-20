from aiogram import Dispatcher, Router

from tgbot.routes.admin.welcome import admin_welcome_router
from tgbot.middlewares.role import AdminCheckerMiddleware



def register_all_routers(dp: Dispatcher, config) -> None:
    """Register routers into main router."""
    master_router = Router()
    master_router.message.outer_middleware(AdminCheckerMiddleware(config.tg_bot.admin_id))
    dp.include_router(master_router)

    master_router.include_router(admin_welcome_router)

