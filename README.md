# Google Trends

> Анализ поисковых трендов через Google Trends

## Зачем это нужно

Этот skill извлекает данные о популярности поисковых запросов из Google Trends. Данные помогают:

- **Отслеживать тренды** — что ищут прямо сейчас в разных странах
- **Сравнивать популярность** — несколько запросов на одном графике
- **Находить связанные запросы** — расширять семантическое ядро
- **Анализировать географию** — где интерес к запросу выше

## Что вы получите

Отчёты в форматах CSV и Markdown:

| Тип | Содержание |
|-----|------------|
| `timeline` | Динамика интереса во времени |
| `regions` | Географическое распределение |
| `related` | Связанные темы |
| `queries` | Связанные поисковые запросы |

## Установка

Skill совместим с различными AI-агентами. Примеры ниже даны для OpenCode.

```bash
# Клонирование skill
git clone https://github.com/prikotov/google-trends.git .opencode/skills/google-trends

# Установка зависимостей Python
pip install -r .opencode/skills/google-trends/requirements.txt
```

## Использование

### Напрямую через Python

```bash
# Динамика за год (по умолчанию)
python3 .opencode/skills/google-trends/trends.py "opencode"

# За последние 3 месяца
python3 .opencode/skills/google-trends/trends.py -t "today 3-m" "artificial intelligence"

# Сравнение запросов
python3 .opencode/skills/google-trends/trends.py "opencode" "cursor ai" "cline"

# Для конкретной страны
python3 .opencode/skills/google-trends/trends.py -g RU "веб-разработка"
```

### Параметры

| Параметр | Сокращение | Описание | Пример |
|----------|------------|----------|--------|
| `--mode` | `-m` | Тип отчёта | `-m regions` |
| `--geo` | `-g` | Код страны | `-g RU` |
| `--timeframe` | `-t` | Период | `-t "today 3-m"` |

### Типы отчётов

| Значение | Описание |
|----------|----------|
| `timeline` | Динамика во времени (по умолчанию) |
| `regions` | Географическое распределение |
| `related` | Связанные темы |
| `queries` | Связанные запросы |

### Тренды дня

```bash
# США (по умолчанию)
bash .opencode/skills/google-trends/trends-daily.sh US

# Россия
bash .opencode/skills/google-trends/trends-daily.sh RU

# Германия
bash .opencode/skills/google-trends/trends-daily.sh DE
```

### Через агента

После установки skill агент автоматически узнаёт о нём. Примеры запросов:

```
Проверь тренды для запроса "artificial intelligence"
```

```
Сравни популярность "opencode" и "cursor ai"
```

```
Покажи связанные запросы для "python programming"
```

## Результаты

Отчёты сохраняются в папку с датой:

```
trends_reports/
└── 2026-03-05/
    ├── trends_opencode_2026-03-05_10-30-15.csv
    └── trends_opencode_2026-03-05_10-30-15.md
```

## Ограничения

- Данные за последние 5 лет
- Сравнение до 5 запросов одновременно
- Относительные значения (0-100), не абсолютные числа
