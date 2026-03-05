# Google Trends - AI Agent Skill

Monitor and analyze Google Trends data for market research, content planning, and trend tracking.

## Capabilities

1. **Daily Trending Searches** - What's trending today in any country
2. **Keyword Interest Over Time** - Historical trend data for keywords
3. **Keyword Comparison** - Compare multiple keywords
4. **Related Topics & Queries** - Discover related searches
5. **Regional Interest** - See where keywords are most popular

## Installation

```bash
# Clone the skill
git clone https://github.com/prikotov/google-trends.git
cd google-trends

# Install Python dependencies
pip install -r requirements.txt
```

## Usage

### Get Trending Searches (Today)

```bash
# US Daily Trends (default)
bash trends-daily.sh US

# Russia
bash trends-daily.sh RU

# Germany
bash trends-daily.sh DE
```

### Check Keyword Interest Over Time

```bash
# Timeline analysis (default: 12 months)
python3 trends.py "opencode" -m timeline

# Specify period
python3 trends.py "bitcoin" -m timeline -t "today 3-m"

# Compare keywords
python3 trends.py "opencode" "cursor" "cline" -m timeline
```

### Related Queries

```bash
# Find related searches
python3 trends.py "artificial intelligence" -m queries
```

### Regional Interest

```bash
# Interest by country
python3 trends.py "python" -m regions

# Specific country
python3 trends.py "веб-разработка" -m regions -g RU
```

## Options

| Option | Short | Description | Values |
|--------|-------|-------------|--------|
| `--mode` | `-m` | Report type | `timeline`, `regions`, `related`, `queries` |
| `--geo` | `-g` | Geography | Country codes (US, RU, DE, etc.) |
| `--timeframe` | `-t` | Time period | `today 3-m`, `today 12-m`, `today 5-y` |

## Output

Reports are saved to `trends_reports/YYYY-MM-DD/`:
- `trends_YYYY-MM-DD_HH-MM-SS.csv` - CSV format
- `trends_YYYY-MM-DD_HH-MM-SS.md` - Markdown format

## Example Workflows

### Morning Market Research

```bash
# Get trending searches
bash trends-daily.sh US
bash trends-daily.sh RU

# Check if trends relate to your business
python3 trends.py "AI tools" -m timeline
```

### Content Planning

```bash
# Compare potential blog topics
python3 trends.py "react hooks" "vue composition api" "svelte" -m timeline

# Find related queries
python3 trends.py "react hooks" -m queries
```

## Country Codes

| Code | Country |
|------|---------|
| US | United States (default) |
| RU | Russia |
| DE | Germany |
| GB | United Kingdom |
| FR | France |
| JP | Japan |

## Requirements

- Python 3.7+
- pytrends library

## Limitations

- Google Trends doesn't provide official API
- Rate limiting may apply for heavy usage
- Data is relative (0-100 scale), not absolute numbers
- Historical data limited to ~5 years

## Author

**Dmitry Prikotov**  
[prikotov.pro](https://prikotov.pro/)

## License

MIT
