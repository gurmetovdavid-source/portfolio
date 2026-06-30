# Telegram Escrow Bot Demo

Telegram-бот для безопасных сделок между покупателем и продавцом — демо-проект для портфолио фрилансера.

## Что реализовано

- Создание сделки через `/newdeal`
- Покупатель подтверждает участие через inline-кнопку
- Покупатель освобождает средства через `release`
- Отмена сделки до завершения через `cancel`
- Открытие спора через `dispute` — уведомление администратору
- Персистентное хранилище сделок в `deals.json`

## Стек

- Python 3.11+
- aiogram 3.x
- python-dotenv

## Как запустить

```bash
cd telegram-escrow-bot
cp .env.example .env
# Отредактируй .env: укажи BOT_TOKEN и ADMIN_ID
pip install -r requirements.txt
python bot.py
```

## Важно

Это демо-версия логики escrow. Реальная оплата и хранение средств не реализованы.
