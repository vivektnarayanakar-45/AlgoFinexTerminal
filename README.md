# AlgoFinex Terminal (AFT)

Bloomberg‑style financial terminal with real‑time market data, advanced charting, options chain (Black‑Scholes), portfolio analytics (VaR, Sharpe), news sentiment (FinBERT), screener (30+ filters), algo strategy monitor, and a Bloomberg‑style command bar.

## Features
- Live market dashboard (WebSocket push)
- Interactive charting with `lightweight-charts`
- Options chain with theoretical pricing (Black‑Scholes)
- Portfolio analytics: VaR, Sharpe ratio, daily returns
- News + sentiment analysis using FinBERT
- Screener with 30+ fundamental/technical filters
- Algorithmic strategy monitoring
- Command palette (Ctrl+K) for quick navigation and actions
- Docker Compose deployment
- CI/CD with GitHub Actions

## Tech Stack
**Backend:** FastAPI, PostgreSQL + TimescaleDB, Redis (cache + pub/sub), WebSockets, FinBERT (Hugging Face), Black‑Scholes  
**Frontend:** React, TypeScript, Tailwind CSS, lightweight‑charts, react‑grid‑layout, Vite

## Quick Start

### 1. Clone & Environment
```bash
git clone <repo>
cd algo_finex_terminal
cp .env.example .env
# Edit .env if needed (defaults work for local)
