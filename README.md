PDT-Clinical-Assistant-Bot/
├── bot.py
├── .env.example
├── requirements.txt
├── README.md
└── docs/   # если будет документация
PDT Clinical Assistant Bot

PDT Clinical Assistant Bot is an English-language Telegram bot designed to provide educational and clinical information on Photodynamic Therapy (PDT). It offers structured guidance on PDT, photosensitizers, treatment steps, and clinical applications.

Features

Overview of PDT

Information on photosensitizers

Advantages of the PDT method

Step-by-step treatment guidance

Applications in oncology, dermatology, urology, etc.

Access to brochures and clinical resources

Contact information for expert consultation

Installation
git clone https://github.com/rolloerro/PDT-Clinical-Assistant-Bot.git
cd PDT-Clinical-Assistant-Bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Create a .env file based on .env.example and set your Telegram bot token:

TOKEN=your_telegram_bot_token_here

Usage
python bot.py


The bot will start and run continuously.

Contributing

Contributions, bug reports, and feature requests are welcome. Please submit pull requests or open issues on GitHub.

License

MIT License
