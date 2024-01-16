import os

from dotenv import load_dotenv


load_dotenv()


TOKEN: str = str(os.getenv('TOKEN'))
VIDEO_SAVE_PATH: str = str(os.getenv('VIDEO_SAVE_PATH'))
