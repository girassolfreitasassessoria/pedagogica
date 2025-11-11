#!/usr/bin/env python3
"""
fetch_instagram_posts.py
Simple helper to fetch the latest public post URLs from a public Instagram profile page
and save them to data/insta_posts.json.

Note: Instagram may block automated requests. Run this script locally. It uses requests + BeautifulSoup.
It only extracts links that match '/p/<id>/' from the profile page HTML.
"""
import requests, re, json, sys, time
from bs4 import BeautifulSoup

PROFILE = "https://www.instagram.com/inclusao.gf.oficial/"
OUT = "data/insta_posts.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_profile(url):
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text

def extract_post_urls(html):
    # Find occurrences of /p/<shortcode>/
    matches = re.findall(r'\/p\/[A-Za-z0-9_\-]+\/', html)
    # make unique while preserving order
    seen = set(); out = []
    for m in matches:
        full = "https://www.instagram.com" + m
        if full not in seen:
            seen.add(full); out.append(full)
    return out

def main():
    try:
        html = fetch_profile(PROFILE)
    except Exception as e:
        print("Erro ao buscar o perfil:", e); sys.exit(1)
    urls = extract_post_urls(html)
    # keep the first 12
    urls = urls[:12]
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(urls, f, indent=2, ensure_ascii=False)
    print(f"Salvas {len(urls)} URLs em {OUT}")

if __name__ == "__main__":
    main()
