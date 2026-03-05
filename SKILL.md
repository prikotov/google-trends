---
name: google-trends
description: Search trend analysis via Google Trends
---

## When to use

- Analyze search query popularity
- Compare trends across queries
- Track interest dynamics over time
- Geographic distribution of queries

## Usage

### Search Query Analysis

```bash
python3 .opencode/skills/google-trends/trends.py [options] <queries...>
```

### Daily Trends

```bash
bash .opencode/skills/google-trends/trends-daily.sh [country_code]
```

Country code: `RU`, `US`, `DE`, `GB`, etc. Default: `US`.

## trends.py Parameters

### Required Argument

- `queries` — one or more search queries to analyze

### Options

| Option | Short | Description | Values | Default |
|--------|-------|-------------|--------|---------|
| `--geo` | `-g` | Region code | RU, US, DE, etc. | worldwide |
| `--timeframe` | `-t` | Time period | `"today 3-m"`, `"today 12-m"`, `"today 5-y"` | `"today 12-m"` |
| `--mode` | `-m` | Report mode | `timeline`, `regions`, `related`, `queries` | `timeline` |

### Report Modes

| Parameter | Description |
|-----------|-------------|
| `timeline` | Interest over time (default) |
| `regions` | Geographic distribution |
| `related` | Related topics |
| `queries` | Related queries |

### trends.py Examples

```bash
# Year-long timeline
python3 .opencode/skills/google-trends/trends.py "opencode"

# Last 3 months
python3 .opencode/skills/google-trends/trends.py -t "today 3-m" "artificial intelligence"

# For Russia
python3 .opencode/skills/google-trends/trends.py -g RU "web development"

# Compare two queries
python3 .opencode/skills/google-trends/trends.py "opencode" "cursor ai"

# Query geography
python3 .opencode/skills/google-trends/trends.py -m regions "python"

# Related queries
python3 .opencode/skills/google-trends/trends.py -m queries "python"
```

### trends-daily.sh Examples

```bash
# US trends (default)
bash .opencode/skills/google-trends/trends-daily.sh

# Russia trends
bash .opencode/skills/google-trends/trends-daily.sh RU

# Germany trends
bash .opencode/skills/google-trends/trends-daily.sh DE
```

## Output

`google_google_trends_reports/YYYY-MM-DD/`:
- `google_trends_query_YYYY-MM-DD_HH-MM-SS.csv` / `.md` — Trends data

### Timeline Report Fields

| Field | Description |
|-------|-------------|
| `date` | Date |
| `<query>` | Relative popularity (0-100) for each query |

### Regions Report Fields

| Field | Description |
|-------|-------------|
| `region` | Region |
| `value` | Popularity in region |

### Related Report Fields

| Field | Description |
|-------|-------------|
| `topic` | Related topic |
| `type` | Topic type |
| `value` | Relative popularity |

### Queries Report Fields

| Field | Description |
|-------|-------------|
| `query` | Related query |
| `value` | Relative popularity |

## Limitations

- Data available for last 5 years
- Compare up to 5 queries simultaneously
