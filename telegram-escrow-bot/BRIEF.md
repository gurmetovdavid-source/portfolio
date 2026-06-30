# Telegram Escrow Bot — Freelance Demo Project

Source Upwork job (approximate): "Development of Telegram Escrow Bot" (Apr 17 2026).
Client asks: a Telegram bot that acts as an escrow service for secure transactions between buyers and sellers.

## Implemented features
- Create a deal (`/newdeal`) with amount and description
- Buyer joins via inline button (`confirm`)
- Buyer releases funds when satisfied (`release`)
- Cancel deal before completion (`cancel`)
- Open dispute (`dispute`) — admin gets notified
- Persistent storage in JSON (`deals.json`)

## How to run
1. Copy `.env.example` to `.env`
2. Put your bot token and admin Telegram ID
3. Install deps: `pip install -r requirements.txt`
4. Run: `python bot.py`

## Tech stack
- Python 3.11+
- aiogram 3.x
- python-dotenv
