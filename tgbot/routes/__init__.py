from aiogram import Dispatcher, Router
from tgbot.middlewares.database import DatabaseMiddleware

from tgbot.routes.admin.admin_menu import admin_menu_router
from tgbot.routes.user.welcome import user_welcome_router
from tgbot.middlewares.role import AdminCheckerMiddleware



def register_all_routers(dp: Dispatcher, config, connection) -> None:
    """Register routers into main router."""
    master_router = Router()
    # Setup MiddleWares.
    master_router.message.outer_middleware(AdminCheckerMiddleware(config.tg_bot.admin_id))
    master_router.callback_query.outer_middleware(AdminCheckerMiddleware(config.tg_bot.admin_id))
    master_router.message.middleware(DatabaseMiddleware(connection))
    master_router.callback_query.middleware(DatabaseMiddleware(connection))
    
    # Add local routers.
    master_router.include_router(admin_menu_router)
    master_router.include_router(user_welcome_router)
    
    # Include into Dispather.
    dp.include_router(master_router)


