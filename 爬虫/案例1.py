import requests
import time
from lxml import html

TMDB_BASE_URL = "https://www.themoviedb.org"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}


def get_movies_by_page(page_num):
    """抓取单页的电影链接"""
    url = f"{TMDB_BASE_URL}/movie/top-rated?page={page_num}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            print(f"第 {page_num} 页请求失败，状态码: {response.status_code}")
            return []

        document = html.fromstring(response.text)
        # 定位卡片中的电影详情链接
        hrefs = document.xpath('//div[contains(@class, "card")]//a[contains(@href, "/movie/")]/@href')

        # 去重并拼接完整 URL
        urls = list(set([TMDB_BASE_URL + href for href in hrefs if href.startswith('/movie/')]))
        return urls
    except Exception as e:
        print(f"抓取第 {page_num} 页时出错: {e}")
        return []


def main():
    all_movie_urls = []

    # 假设抓取前 10 页（可以根据需要调整最大页数）
    MAX_PAGE = 1

    for page in range(1, MAX_PAGE + 1):
        print(f"正在抓取第 {page} 页...")
        urls = get_movies_by_page(page)

        if not urls:
            print("未能获取到数据，可能已达到末尾或被拦截。")
            break

        all_movie_urls.extend(urls)

        # 极重要：设置延迟，避免频率过高被封禁 IP
        time.sleep(2)

    # 去除可能存在的重复链接
    all_movie_urls = list(set(all_movie_urls))

    print(f"\n共抓取到 {len(all_movie_urls)} 条电影链接：")
    for url in all_movie_urls:
        print(url)


if __name__ == '__main__':
    main()