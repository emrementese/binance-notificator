from src.notificators.telegram import TelegramBot
from src.logger import logger

def main():
    logger.info(f"Starting Notification Services...")
    services = []
    services.append(TelegramBot(chat_id=1097914704))
    
    


if __name__ == "__main__":
    main()