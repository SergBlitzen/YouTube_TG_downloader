from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from pytube import YouTube

from config import VIDEO_SAVE_PATH

main_router = Router()


class VideoEdit(StatesGroup):
    setting_video_url = State()


@main_router.message(Command(commands=['start']))
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Use /download command")


@main_router.message(Command(commands=['download']))
async def download_video(message: Message, state: FSMContext):
    await message.answer("Enter video url")
    await state.set_state(VideoEdit.setting_video_url)


@main_router.message(VideoEdit.setting_video_url)
async def get_video_url(message: Message, state: FSMContext):
    await message.answer("Starting...")
    video_url = message.text
    video_obj: YouTube = YouTube(video_url)
    video_obj.streams.get_highest_resolution().download(output_path=VIDEO_SAVE_PATH)
    await state.clear()
    await message.answer("Download complete. Check your folder")
