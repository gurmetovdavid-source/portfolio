# Projects

A selection of projects I have built for clinics, healthcare teams, and service businesses. Most are production-ready and deployed.

---

## DentalCloud

A full SaaS platform for healthcare clinics.

- **What it does:** online scheduling, patient CRM, doctor dashboard, patient portal, internal chat, photo management, QR upload, email and push notifications.
- **Stack:** Next.js 14, React 18, TypeScript, PostgreSQL, Drizzle ORM, Docker, Nginx.
- **Highlights:** custom JWT auth, role-based access control, multi-clinic support, Docker deployment on VPS.
- **Status:** In production.
- **Repo:** [dentalcloud-saas](https://github.com/gurmetovdavid-source/dentalcloud-saas)
- **Live demo:** [dentalcloud-app.vercel.app](https://dentalcloud-app.vercel.app) — click "Try demo doctor" or "Try demo patient" to explore without registration.

---

## Clinic Analytics Dashboard

A modern analytics dashboard for healthcare clinics.

- **What it does:** visualizes appointments, revenue by service, doctor workload, and patient satisfaction.
- **Stack:** Next.js 14, TypeScript, Tailwind CSS, Recharts, Lucide React.
- **Highlights:** responsive KPI cards, interactive charts, dark-mode-ready color system.
- **Status:** Published.
- **Repo:** [clinic-analytics-dashboard](https://github.com/gurmetovdavid-source/clinic-analytics-dashboard)
- **Live demo:** [clinic-analytics-dashboard.vercel.app](https://clinic-analytics-dashboard.vercel.app)

---

## AI Clinic Receptionist

A Telegram bot that books appointments through natural language.

- **What it does:** patients describe what they need, the bot extracts name, service, and time with an LLM, then saves the request and notifies the clinic manager.
- **Stack:** Python, aiogram 3.x, SQLite, OpenRouter LLM API.
- **Highlights:** LLM-powered intent extraction, async handlers, manager notifications.
- **Status:** Published.
- **Repo:** [ai-clinic-receptionist](https://github.com/gurmetovdavid-source/ai-clinic-receptionist)

---

## Clinic Inventory Tracker

A lightweight inventory app for medical supplies.

- **What it does:** tracks stock levels, shows low-stock alerts, manages suppliers.
- **Stack:** Next.js 14, TypeScript, Tailwind CSS, localStorage.
- **Highlights:** client-side persistence, responsive table, demo data reset.
- **Status:** Published.
- **Repo:** [clinic-inventory-tracker](https://github.com/gurmetovdavid-source/clinic-inventory-tracker)
- **Live demo:** [clinic-inventory-tracker.vercel.app](https://clinic-inventory-tracker.vercel.app)

---

## TaskFlow Dashboard

A Kanban-style task and project management dashboard for teams.

- **What it does:** organize tasks into columns, track status, priority, and assignee, see team productivity stats.
- **Stack:** Next.js 14, TypeScript, Tailwind CSS, localStorage, Lucide React.
- **Highlights:** drag-and-drop board feel, responsive layout, demo data in browser storage.
- **Status:** Published.
- **Repo:** [taskflow-dashboard](https://github.com/gurmetovdavid-source/taskflow-dashboard)
- **Live demo:** [taskflow-dashboard.vercel.app](https://taskflow-dashboard.vercel.app)

---

## Expense Tracker SaaS

A simple expense tracker for individuals and small teams.

- **What it does:** add expenses by category, set monthly budgets, see spending analytics and trends.
- **Stack:** Next.js 14, TypeScript, Tailwind CSS, Recharts, localStorage, Lucide React.
- **Highlights:** budget progress, category and time charts, responsive UI.
- **Status:** Published.
- **Repo:** [expense-tracker-saas](https://github.com/gurmetovdavid-source/expense-tracker-saas)
- **Live demo:** [expense-tracker-saas.vercel.app](https://expense-tracker-saas.vercel.app)

---

## LeadTrack SaaS

A multi-partner lead tracking platform built from a real Upwork brief. It covers partner onboarding, offer management, lead attribution, conversion tracking, settlements, and a partner portal.

- **What it does:** manage partners and offers, track leads by source and status, record events, calculate commissions, generate settlement reports, and give partners a self-service portal.
- **Stack:** Next.js 14, TypeScript, Tailwind CSS, Recharts, Lucide React, localStorage.
- **Highlights:** admin + partner views, role-aware navigation, interactive charts, status-driven badges, widget demo for embedded lead forms.
- **Status:** Published.
- **Repo:** [leadtrack-saas](https://github.com/gurmetovdavid-source/leadtrack-saas)
- **Live demo:** [leadtrack-saas.vercel.app](https://leadtrack-saas.vercel.app)

---

## Voice AI Assistant

A voicebot that makes outbound phone calls, listens, speaks, and saves results to a CRM.

- **What it does:** dials candidates via SIP, handles speech-to-text and text-to-speech, runs an LLM for conversation, uploads call recordings to CRM deals.
- **Stack:** Python, FastAPI, Asterisk, SIP, ASR/TTS, LLM APIs, Bitrix24 webhook.
- **Highlights:** end-to-end call automation, real-time audio handling, CRM integration.
- **Status:** Working prototype.
- **Repo:** [mango-asterisk-voicebot](https://github.com/gurmetovdavid-source/mango-asterisk-voicebot)

---

## Shift Report Bot

A Telegram bot for managing shift schedules and collecting photo reports from assistants.

- **What it does:** tracks morning/evening shifts, sends reminders and deadlines, collects photo reports, pings managers if reports are missing.
- **Stack:** Python, aiogram, FSM, APScheduler, Docker.
- **Highlights:** scheduled reminders, role-based workflows, deployed and running 24/7.
- **Status:** In production.
- **Repo:** [tg-report-bot](https://github.com/gurmetovdavid-source/tg-report-bot)

---

## More bots

Other Telegram automation projects I have built for clinics and teams:

- **Recipe Bot** — generates filled medical prescription forms in PDF from patient data.
- **Patient Bot** — appointment booking and FAQ bot for patients.

These are kept private until cleaned and translated.

---

## Publication status

Some repos are being cleaned and translated before going public. See [PROJECTS_TO_PUBLISH.md](./PROJECTS_TO_PUBLISH.md) for the full publication plan.

[Back to README](./README.md)
