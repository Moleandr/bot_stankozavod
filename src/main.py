from aiogram import Bot, Dispatcher
from app import config
from app.router import router


def main():
    bots = [Bot(token) for token in [config.token]]
    dp = Dispatcher()
    dp.include_router(router)
    dp.run_polling(*bots, polling_timeout=1)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        raise
