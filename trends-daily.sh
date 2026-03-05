#!/bin/bash
# Get today's trending searches
# Usage: ./trends-daily.sh [country_code]
# Example: ./trends-daily.sh RU

GEO="${1:-US}"
curl -s "https://trends.google.com/trending/rss?geo=$GEO" | \
  grep -o '<title>[^<]*</title>' | \
  sed 's/<[^>]*>//g' | \
  tail -n +2 | \
  head -20
