# Google Trends

> Search trend analysis via Google Trends

## Why use this

This skill extracts search query popularity data from Google Trends. The data helps:

- **Track trends** — what people are searching for right now in different countries
- **Compare popularity** — multiple queries on one chart
- **Find related queries** — expand your semantic core
- **Analyze geography** — where interest in a query is higher

## What you get

Reports in CSV and Markdown formats:

| Type | Content |
|------|----------|
| `timeline` | Interest dynamics over time |
| `regions` | Geographic distribution |
| `related` | Related topics |
| `queries` | Related search queries |

## Installation

Skill is compatible with various AI agents. Examples below are for OpenCode.

```bash
# Clone skill
git clone https://github.com/prikotov/google-trends.git .opencode/skills/google-trends

# Install Python dependencies
pip install -r .opencode/skills/google-trends/requirements.txt
```

## Usage

### Direct via Python

```bash
# Year-long timeline (default)
python3 .opencode/skills/google-trends/trends.py "opencode"

# Last 3 months
python3 .opencode/skills/google-trends/trends.py -t "today 3-m" "artificial intelligence"

# Compare queries
python3 .opencode/skills/google-trends/trends.py "opencode" "cursor ai" "cline"

# For specific country
python3 .opencode/skills/google-trends/trends.py -g RU "web development"
```

### Parameters

| Parameter | Short | Description | Example |
|-----------|-------|-------------|---------|
| `--mode` | `-m` | Report type | `-m regions` |
| `--geo` | `-g` | Country code | `-g RU` |
| `--timeframe` | `-t` | Time period | `-t "today 3-m"` |

### Report types

| Value | Description |
|-------|-------------|
| `timeline` | Interest over time (default) |
| `regions` | Geographic distribution |
| `related` | Related topics |
| `queries` | Related queries |

### Daily Trends

```bash
# US (default)
bash .opencode/skills/google-trends/trends-daily.sh US

# Russia
bash .opencode/skills/google-trends/trends-daily.sh RU

# Germany
bash .opencode/skills/google-trends/trends-daily.sh DE
```

### Via agent

After installation, the agent automatically recognizes the skill. Example requests:

```
Check trends for "artificial intelligence"
```

```
Compare popularity of "opencode" and "cursor ai"
```

```
Show related queries for "python programming"
```

## Results

Reports are saved to a dated folder:

```
google_google_trends_reports/
└── 2026-03-05/
    ├── google_trends_opencode_2026-03-05_10-30-15.csv
    └── google_trends_opencode_2026-03-05_10-30-15.md
```

## Limitations

- Data for last 5 years
- Compare up to 5 queries simultaneously
- Relative values (0-100), not absolute numbers
