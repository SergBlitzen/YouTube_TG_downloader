from aiogram import types
from aiogram import Router
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pytube import YouTube

from config import VIDEO_SAVE_PATH

main_router = Router()


class VideoEdit(StatesGroup):
    setting_video_url = State()
    setting_audio_url = State()


@main_router.message(Command(commands=['start']))
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Use /download command")


@main_router.message(Command(commands=['download']))
async def download_video(message: types.Message, state: FSMContext):
    await message.answer("Enter video url")
    await state.set_state(VideoEdit.setting_video_url)


@main_router.message(VideoEdit.setting_video_url)
async def get_video_url(message: types.Message, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="Download mp4 video",
            callback_data='video'
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text="Download mp3 audio",
            callback_data='audio'
        )
    )
    await state.set_data({'URL': message.text})
    await message.answer(
        text='Select download option',
        reply_markup=builder.as_markup()
    )


@main_router.callback_query(F.data == 'audio')
@main_router.callback_query(F.data == 'video')
async def download_video(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Starting...")
    video_url = await state.get_data()
    video_obj: YouTube = YouTube(video_url['URL'])
    actions = {
        'video': video_obj.streams.get_highest_resolution(),
        'audio': video_obj.streams.get_audio_only()
    }
    actions[call.data].download(output_path=VIDEO_SAVE_PATH)
    await call.message.answer("Download complete. Check your folder")

