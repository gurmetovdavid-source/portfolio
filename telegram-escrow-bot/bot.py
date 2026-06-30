import asyncio
import json
import os
from datetime import datetime
from uuid import uuid4

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

DATA_FILE = "deals.json"


def load_deals():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_deals(deals):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(deals, f, ensure_ascii=False, indent=2)


def get_deal_keyboard(deal_id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"confirm:{deal_id}"),
                InlineKeyboardButton(text="❌ Отменить", callback_data=f"cancel:{deal_id}"),
            ],
            [
                InlineKeyboardButton(text="💰 Освободить средства", callback_data=f"release:{deal_id}"),
                InlineKeyboardButton(text="⚠️ Спор", callback_data=f"dispute:{deal_id}"),
            ],
        ]
    )


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я <b>Escrow-бот</b> для безопасных сделок.\n\n"
        "Команды:\n"
        "/newdeal — создать новую сделку\n"
        "/deals — список активных сделок\n"
        "/help — помощь",
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "<b>Как работает escrow-бот:</b>\n\n"
        "1. Продавец создаёт сделку через /newdeal, указывая сумму и описание.\n"
        "2. Покупатель получает ссылку и подтверждает участие.\n"
        "3. После выполнения работы/передачи товара покупатель нажимает «Освободить средства».\n"
        "4. Если возник спор — любая сторона нажимает «Спор», администратор разбирается.\n\n"
        "<i>Демо-версия: оплата симулирована, для тестирования логики.</i>",
        parse_mode="HTML",
    )


@router.message(Command("newdeal"))
async def cmd_newdeal(message: Message):
    parts = message.text.split("\n", 2)
    if len(parts) < 3:
        await message.answer(
            "Используйте формат:\n\n"
            "/newdeal\n"
            "Сумма в USD\n"
            "Описание сделки\n\n"
            "Пример:\n"
            "/newdeal\n"
            "150\n"
            "Разработка лендинга для кофейни",
        )
        return

    try:
        amount = float(parts[1].strip())
    except ValueError:
        await message.answer("❌ Сумма должна быть числом.")
        return

    description = parts[2].strip()
    deal_id = str(uuid4())[:8]
    deals = load_deals()
    deals[deal_id] = {
        "id": deal_id,
        "seller_id": message.from_user.id,
        "seller_username": message.from_user.username or "",
        "buyer_id": None,
        "amount": amount,
        "description": description,
        "status": "pending",  # pending, active, released, cancelled, disputed
        "created_at": datetime.now().isoformat(),
    }
    save_deals(deals)

    await message.answer(
        f"✅ Сделка <b>#{deal_id}</b> создана!\n\n"
        f"💰 Сумма: <b>${amount}</b>\n"
        f"📝 Описание: {description}\n\n"
        "Отправьте покупателю эту ссылку или сообщение с ID сделки.",
        parse_mode="HTML",
    )
    await message.answer(
        f"📌 Сделка #{deal_id}\n"
        f"Покупатель, нажмите кнопку ниже, чтобы присоединиться.",
        reply_markup=get_deal_keyboard(deal_id),
    )


@router.message(Command("deals"))
async def cmd_deals(message: Message):
    deals = load_deals()
    user_id = message.from_user.id
    user_deals = [d for d in deals.values() if d["seller_id"] == user_id or d["buyer_id"] == user_id]

    if not user_deals:
        await message.answer("У вас пока нет сделок. Создайте через /newdeal")
        return

    text = "<b>Ваши сделки:</b>\n\n"
    for d in user_deals:
        role = "Продавец" if d["seller_id"] == user_id else "Покупатель"
        text += (
            f"#{d['id']} | ${d['amount']} | {d['status'].upper()}\n"
            f"Роль: {role} | {d['description'][:40]}...\n\n"
        )
    await message.answer(text, parse_mode="HTML")


@router.callback_query(F.data.startswith("confirm:"))
async def confirm_deal(callback: CallbackQuery):
    deal_id = callback.data.split(":", 1)[1]
    deals = load_deals()
    deal = deals.get(deal_id)

    if not deal:
        await callback.answer("Сделка не найдена.", show_alert=True)
        return

    if deal["status"] != "pending":
        await callback.answer("Сделка уже активна или завершена.", show_alert=True)
        return

    if callback.from_user.id == deal["seller_id"]:
        await callback.answer("Продавец не может быть покупателем.", show_alert=True)
        return

    deal["buyer_id"] = callback.from_user.id
    deal["buyer_username"] = callback.from_user.username or ""
    deal["status"] = "active"
    save_deals(deals)

    await callback.message.edit_text(
        f"✅ Сделка <b>#{deal_id}</b> активирована!\n\n"
        f"💰 Сумма: ${deal['amount']}\n"
        f"📝 {deal['description']}\n"
        f"👤 Продавец: @{deal.get('seller_username', 'unknown')}\n"
        f"👤 Покупатель: @{deal.get('buyer_username', 'unknown')}\n\n"
        "Покупатель: после получения товара/услуги нажмите «Освободить средства».",
        parse_mode="HTML",
        reply_markup=get_deal_keyboard(deal_id),
    )
    await callback.answer("Вы присоединились к сделке.")


@router.callback_query(F.data.startswith("release:"))
async def release_deal(callback: CallbackQuery):
    deal_id = callback.data.split(":", 1)[1]
    deals = load_deals()
    deal = deals.get(deal_id)

    if not deal or deal["status"] != "active":
        await callback.answer("Сделка не активна.", show_alert=True)
        return

    if callback.from_user.id != deal["buyer_id"]:
        await callback.answer("Только покупатель может освободить средства.", show_alert=True)
        return

    deal["status"] = "released"
    save_deals(deals)

    await callback.message.edit_text(
        f"🎉 Сделка <b>#{deal_id}</b> завершена!\n\n"
        f"Средства в размере ${deal['amount']} освобождены продавцу.\n"
        f"Спасибо за использование escrow-бота.",
        parse_mode="HTML",
    )
    await bot.send_message(
        deal["seller_id"],
        f"💰 По сделке #{deal_id} покупатель освободил ${deal['amount']}.",
    )
    await callback.answer("Средства освобождены.")


@router.callback_query(F.data.startswith("cancel:"))
async def cancel_deal(callback: CallbackQuery):
    deal_id = callback.data.split(":", 1)[1]
    deals = load_deals()
    deal = deals.get(deal_id)

    if not deal:
        await callback.answer("Сделка не найдена.", show_alert=True)
        return

    if callback.from_user.id not in (deal["seller_id"], deal.get("buyer_id")):
        await callback.answer("Нет доступа.", show_alert=True)
        return

    if deal["status"] in ("released", "disputed"):
        await callback.answer("Сделку нельзя отменить.", show_alert=True)
        return

    deal["status"] = "cancelled"
    save_deals(deals)

    await callback.message.edit_text(
        f"❌ Сделка <b>#{deal_id}</b> отменена.",
        parse_mode="HTML",
    )
    await callback.answer("Сделка отменена.")


@router.callback_query(F.data.startswith("dispute:"))
async def dispute_deal(callback: CallbackQuery):
    deal_id = callback.data.split(":", 1)[1]
    deals = load_deals()
    deal = deals.get(deal_id)

    if not deal or deal["status"] != "active":
        await callback.answer("Сделка не активна.", show_alert=True)
        return

    deal["status"] = "disputed"
    save_deals(deals)

    await callback.message.edit_text(
        f"⚠️ Сделка <b>#{deal_id}</b> переведена в статус спора.\n\n"
        "Администратор свяжется с обеими сторонами для разрешения ситуации.",
        parse_mode="HTML",
    )
    if ADMIN_ID:
        await bot.send_message(
            ADMIN_ID,
            f"⚠️ Спор по сделке #{deal_id}\nСумма: ${deal['amount']}\nОписание: {deal['description']}",
        )
    await callback.answer("Спор открыт.")


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
