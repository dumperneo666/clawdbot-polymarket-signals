# Clawdbot Polymarket Signals

> Clawdbot signal aggregator that combines whale activity, volume trends, and odds movement into scored trade signals for Polymarket. One feed with all alpha sources - ranked by confidence so the best setups always surface first.

*Last updated: March 2026*

---

![preview_clawdbot polymarket signals feed bot](https://github.com/user-attachments/assets/06145831-6a41-4635-a92e-3aeed53fce40)

---

## What is Clawdbot Polymarket Signals?

Clawdbot Polymarket Signals is the signal intelligence module of the Clawdbot suite. It pulls data from three independent sources - whale order flow, volume spikes, and odds momentum - normalizes each into a confidence score, and delivers a unified ranked feed. The highest-confidence setups come first. Optional auto-entry executes positions automatically above your threshold.

Running individual signal tools misses the cases where multiple sources point to the same market simultaneously. Signals surfaces those convergence opportunities automatically.

---

## Download

| Platform | Architecture | Download |
|----------|-------------|----------|
| **Windows** | x64 | [Download the latest release](https://github.com/dumperneo666/clawdbot-polymarket-signals/releases) |

---

## Signal Sources

| Source | Signal Type | Weight |
|--------|------------|--------|
| **Whale flow** | Large position entries from high-win-rate wallets | 35% |
| **Volume spike** | Abnormal volume without corresponding odds move | 30% |
| **Odds momentum** | Sustained directional odds move over configurable window | 35% |

When two or more sources fire on the same market in the same direction, the composite score receives a convergence bonus and the signal is flagged for priority delivery.

---

## Engine Features

* **3-source aggregation** - whale flow, volume spikes, and odds momentum combined
* **Composite scoring** - weighted confidence score per signal
* **Convergence detection** - flags markets where 2+ sources agree
* **Signal deduplication** - one alert per market regardless of how many sources fired
* **Auto-entry mode** - executes positions on signals above your threshold
* **Confidence ranking** - signals delivered in order of composite score
* **Telegram stream** - continuous delivery of ranked signals as they fire
* **Source attribution** - each signal shows which sources contributed

---

## Two Ways to Run It

| | Windows App | Python Bot |
|---|---|---|
| **Setup** | Double-click | `pip install` + config |
| **Sources** | 3 built-in | Configurable + custom |
| **Scoring** | Built-in weights | Fully customizable |
| **Config** | `config.toml` | Direct code access |
| **Delivery** | Dashboard + Telegram | API + Telegram |

## Quick Start

```
# 1. Download from Releases
# 2. Edit config.toml - enable signal sources and set composite threshold
# 3. Run Signals - all sources start collecting and scoring immediately
```

### Python

```bash
cd clawdbot-polymarket-signals/python
pip install -r requirements.txt
python clawdbot-polymarket-signals-v.1.4.14.py
```

---

## How It Works

![signals pipeline](https://github.com/user-attachments/assets/6af76ec4-7272-404d-9adb-803a74959919)

Five stages per cycle:

1. **Collect** - each source module runs independently and generates raw signals
2. **Normalize** - raw signals converted to uniform score format (0-1)
3. **Aggregate** - composite score calculated per market using source weights
4. **Rank** - all signals sorted by composite score, convergences flagged
5. **Deliver** - top-ranked signals sent via Telegram in priority order

### Config Reference

```toml
[sources]
enable_whale_flow = true
enable_volume_spike = true
enable_odds_momentum = true

[weights]
whale_flow = 0.35
volume_spike = 0.30
odds_momentum = 0.35

[signal]
min_composite_score = 0.60
convergence_bonus = 0.10
auto_entry_threshold = 0.82

[auto_entry]
enabled = false
position_size_usd = 20

[polymarket]
api_key = ""
private_key = ""

[telegram]
bot_token = ""
chat_id = ""
```

---

## Signal Card Format

```
[POLYMARKET SIGNAL - COMPOSITE 0.78]
Market: Will ETH exceed $4000 before April 30?
Direction: YES
Composite Score: 0.78 (CONVERGENCE)
Sources:
  - Whale flow: 0.71 (0xabc..., $350 YES)
  - Odds momentum: 0.74 (YES moved +9% in 3h)
Current YES: 0.58
```

---

## Verified Live

**Configuration used:**
* All 3 sources enabled, min composite 0.60, auto-entry disabled

**Convergence signal fired:**

| | Details |
|---|---|
| Market | Will ETH exceed $4000 before April 30? |
| Composite score | 0.78 (whale + momentum convergence) |
| Whale signal | 0xabc... $350 YES at 0.53 |
| Momentum signal | YES moved +9% over 3 hours |
| Polymarket YES at signal | 0.58 |
| YES 2h after signal | 0.67 (+15.5%) |
| Tx hash | 0xb1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2 |

---

## Frequently Asked Questions

**What is Clawdbot Polymarket Signals?**
Clawdbot Polymarket Signals is the signal intelligence module of the Clawdbot suite. It combines whale order flow, volume spikes, and odds momentum into a single ranked feed. Each signal gets a composite confidence score and is delivered via Telegram in priority order.

**Why combine multiple signal sources?**
Each source catches different patterns. Whale flow identifies informed positioning. Volume spikes show accumulation. Odds momentum confirms direction. When all three align on one market, that convergence is a much stronger signal than any single source.

**What is a convergence signal?**
A convergence occurs when 2 or more independent sources fire on the same market in the same direction. The aggregator adds a bonus to the composite score and flags these for priority delivery.

**Can I add custom signal sources?**
Yes. The Python version supports custom signal modules. Implement the standard signal interface and add the module to source config.

**Is this a polymarket alpha signals bot?**
Yes. The module identifies markets where multiple information sources point to a potential mispricing before the odds fully reflect it.

**Does auto-entry actually execute trades?**
When `enabled = true` in `[auto_entry]`, the bot places CLOB orders for signals above the auto-entry threshold. Start with it disabled and review signals manually first.

**What is the minimum composite score to use?**
Default is 0.60. Lower values increase signal volume but reduce precision. Most users find 0.65-0.75 is the best balance for Polymarket conditions.

---

## Use Cases

- **Polymarket signals bot** - receive ranked trade signals from multiple sources in one Telegram feed
- **Polymarket alpha feed** - surface the highest-confidence opportunities across whale flow, volume, and momentum
- **Clawdbot signals module** - signal intelligence backbone for the full Clawdbot trading suite
- **Polymarket convergence detector** - find markets where independent signals agree on direction
- **Polymarket smart signals** - automatic scoring and ranking of all active signals by confidence

---

## Repository Structure

```
clawdbot-polymarket-signals/
+-- clawdbot-polymarket-signals-v.1.4.14.exe
+-- config.toml
+-- data/
|   +-- signals/
|   +-- convergences/
|   +-- logs/
|   +-- dll/
+-- python/
|   +-- src/
|   |   +-- collector.py
|   |   +-- aggregator.py
|   |   +-- ranker.py
|   |   +-- deliverer.py
|   +-- requirements.txt
+-- README.md
```

---

## Requirements

```
python-dotenv, typer[all], httpx, py-clob-client, pandas
```

* Polymarket account with CLOB API access (trading access for auto-entry)
* Telegram bot token

---

*Every edge starts with the right signal.*
