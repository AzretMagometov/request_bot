import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import create_settings
from handlers.user_handlers import router as user_router

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    settings = create_settings()

    bot = Bot(token=settings.token)
    dp = Dispatcher()

    dp["admins"] = settings.admins
    dp.include_router(user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
