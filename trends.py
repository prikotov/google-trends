#!/usr/bin/env python3
"""
Google Trends CLI - анализ динамики поисковых запросов
"""

import argparse
import sys
import json
from datetime import datetime
from pytrends.request import TrendReq

def get_interest_over_time(keywords, geo='', timeframe='today 12-m'):
    """Получить динамику интереса во времени"""
    pytrends = TrendReq(hl='ru', tz=180)
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')
    
    data = pytrends.interest_over_time()
    
    if data.empty:
        return []
    
    result = []
    for date, row in data.iterrows():
        item = {'date': date.strftime('%Y-%m-%d')}
        for kw in keywords:
            item[kw] = int(row[kw])
        result.append(item)
    
    return result

def get_related_topics(keyword, geo=''):
    """Получить связанные темы"""
    pytrends = TrendReq(hl='ru', tz=180)
    pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo=geo, gprop='')
    
    topics = pytrends.related_topics()
    
    result = []
    if keyword in topics and topics[keyword]['rising'] is not None:
        for _, row in topics[keyword]['rising'].head(10).iterrows():
            result.append({
                'topic': row['topic_title'],
                'type': row['topic_type'],
                'value': row['value']
            })
    
    return result

def get_related_queries(keyword, geo=''):
    """Получить связанные запросы"""
    pytrends = TrendReq(hl='ru', tz=180)
    pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo=geo, gprop='')
    
    queries = pytrends.related_queries()
    
    result = []
    if keyword in queries and queries[keyword]['rising'] is not None:
        for _, row in queries[keyword]['rising'].head(20).iterrows():
            result.append({
                'query': row['query'],
                'value': row['value']
            })
    
    return result

def get_interest_by_region(keyword, geo=''):
    """Получить интерес по регионам"""
    pytrends = TrendReq(hl='ru', tz=180)
    pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo=geo, gprop='')
    
    regions = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
    
    result = []
    for region, row in regions.head(20).iterrows():
        if row[keyword] > 0:
            result.append({
                'region': region,
                'value': int(row[keyword])
            })
    
    return sorted(result, key=lambda x: x['value'], reverse=True)

def save_csv(data, filename, fieldnames):
    """Сохранить данные в CSV"""
    import csv
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(data)

def save_markdown(data, filename, title, keyword):
    """Сохранить данные в Markdown"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"Запрос: {keyword}\n\n")
        
        if not data:
            f.write("_Нет данных_\n")
            return
        
        headers = list(data[0].keys())
        f.write('| ' + ' | '.join(headers) + ' |\n')
        f.write('| ' + ' | '.join(['---'] * len(headers)) + ' |\n')
        
        for row in data:
            values = [str(row.get(h, '')) for h in headers]
            f.write('| ' + ' | '.join(values) + ' |\n')

def create_report_dir():
    """Создать папку для отчётов"""
    import os
    report_dir = os.path.join(os.getcwd(), 'trends_reports')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    date_dir = os.path.join(report_dir, datetime.now().strftime('%Y-%m-%d'))
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)
    
    return date_dir

def main():
    parser = argparse.ArgumentParser(description='Google Trends CLI')
    parser.add_argument('keywords', nargs='+', help='Ключевые слова для анализа')
    parser.add_argument('-g', '--geo', default='', help='География (US, RU, DE и т.д.)')
    parser.add_argument('-t', '--timeframe', default='today 12-m', 
                       help='Период: "today 3-m", "today 12-m", "today 5-y"')
    parser.add_argument('-m', '--mode', default='timeline', 
                       choices=['timeline', 'regions', 'related', 'queries'],
                       help='Режим: timeline (динамика), regions (по регионам), related (связанные темы), queries (связанные запросы)')
    
    args = parser.parse_args()
    
    print(f"\n  Запрос: {', '.join(args.keywords)}")
    print(f"  Режим: {args.mode}")
    if args.geo:
        print(f"  Регион: {args.geo}")
    print()
    
    try:
        if args.mode == 'timeline':
            data = get_interest_over_time(args.keywords, args.geo, args.timeframe)
            fieldnames = ['date'] + args.keywords
            title = "Динамика интереса"
        elif args.mode == 'regions':
            data = get_interest_by_region(args.keywords[0], args.geo)
            fieldnames = ['region', 'value']
            title = "Интерес по регионам"
        elif args.mode == 'related':
            data = get_related_topics(args.keywords[0], args.geo)
            fieldnames = ['topic', 'type', 'value']
            title = "Связанные темы"
        elif args.mode == 'queries':
            data = get_related_queries(args.keywords[0], args.geo)
            fieldnames = ['query', 'value']
            title = "Связанные запросы"
        
        if not data:
            print("  Нет данных для отображения")
            return
        
        report_dir = create_report_dir()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        keyword_safe = args.keywords[0].replace(' ', '_')
        
        csv_file = os.path.join(report_dir, f'trends_{keyword_safe}_{timestamp}.csv')
        md_file = os.path.join(report_dir, f'trends_{keyword_safe}_{timestamp}.md')
        
        save_csv(data, csv_file, fieldnames)
        save_markdown(data, md_file, title, ', '.join(args.keywords))
        
        print(f"  Папка отчёта: trends_reports/{datetime.now().strftime('%Y-%m-%d')}")
        print(f"  Создано файлов:")
        print(f"    - trends_{keyword_safe}_{timestamp}.csv")
        print(f"    - trends_{keyword_safe}_{timestamp}.md")
        print(f"\n  Найдено записей: {len(data)}")
        
        # Показать последние 5 записей для timeline
        if args.mode == 'timeline' and data:
            print("\n  Последние значения:")
            for row in data[-5:]:
                values = [f"{kw}: {row[kw]}" for kw in args.keywords]
                print(f"    {row['date']}: {', '.join(values)}")
        
    except Exception as e:
        print(f"\n  Ошибка: {e}")
        sys.exit(1)

if __name__ == '__main__':
    import os
    main()
