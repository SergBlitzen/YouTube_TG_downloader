# YouTube downloader TG bot

A simple bot that requires only one command (and one message with link actually)
to download a video in highest resolution

## Preparing to launch

Install and activate virtual environment in root folder

Install dependencies:
```bash
pip install -r requirements.txt
```

Create `.env` file in root directory with environmental variables 

You need a TG bot token from BotFather to launch this code locally. You also need to provide
save path for downloaded videos.
Environmental variables are:
- `TOKEN=your_token_here`
- `VIDEO_SAVE_PATH=C:\\Users\\{user}\\Downloads`

## Launching application

Launch `main.py` from root project directory

```bash
python main.py
```

## Stack

- Python 3.11
- Aiogram 3.3.0
