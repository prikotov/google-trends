---
name: google-trends
description: Анализ поисковых трендов через Google Trends
---

## Когда использовать

- Анализ популярности поисковых запросов
- Сравнение трендов по запросам
- Динамика интереса во времени
- Географическое распределение запросов

## Запуск

```bash
python3 .opencode/skills/google-trends/trends.py [опции] <запросы...>
```

### Обязательный параметр

- `запросы` — один или несколько поисковых запросов для анализа

### Опции

| Опция | Сокращение | Описание | Значения | По умолчанию |
|-------|------------|----------|----------|--------------|
| `--geo` | `-g` | Код региона | RU, US, DE и т.д. | весь мир |
| `--timeframe` | `-t` | Период | `"today 3-m"`, `"today 12-m"`, `"today 5-y"` | `"today 12-m"` |
| `--mode` | `-m` | Режим отчёта | `timeline`, `regions`, `related`, `queries` | `timeline` |

### Режимы отчётов

| Параметр | Описание |
|----------|----------|
| `timeline` | Динамика во времени (по умолчанию) |
| `regions` | Географическое распределение |
| `related` | Связанные темы |
| `queries` | Связанные запросы |

### Примеры

```bash
# Динамика за год
python3 .opencode/skills/google-trends/trends.py "opencode"

# За последние 3 месяца
python3 .opencode/skills/google-trends/trends.py -t "today 3-m" "artificial intelligence"

# Для России
python3 .opencode/skills/google-trends/trends.py -g RU "веб-разработка"

# Сравнение двух запросов
python3 .opencode/skills/google-trends/trends.py "opencode" "cursor ai"

# География запросов
python3 .opencode/skills/google-trends/trends.py -m regions "python"

# Связанные запросы
python3 .opencode/skills/google-trends/trends.py -m queries "python"
```

## Результат

`trends_reports/YYYY-MM-DD/`:
- `trends_запрос_YYYY-MM-DD_HH-MM-SS.csv` / `.md` — данные Trends

### Поля в отчёте timeline

| Поле | Описание |
|------|----------|
| `date` | Дата |
| `<запрос>` | Относительная популярность (0-100) для каждого запроса |

### Поля в отчёте regions

| Поле | Описание |
|------|----------|
| `region` | Регион |
| `value` | Популярность в регионе |

### Поля в отчёте related

| Поле | Описание |
|------|----------|
| `topic` | Связанная тема |
| `type` | Тип темы |
| `value` | Относительная популярность |

### Поля в отчёте queries

| Поле | Описание |
|------|----------|
| `query` | Связанный запрос |
| `value` | Относительная популярность |

## Ограничения

- Данные за последние 5 лет
- Сравнение до 5 запросов одновременно
