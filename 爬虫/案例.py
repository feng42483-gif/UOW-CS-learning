import requests
import os
import csv
from lxml import html

# 常量
MOVIE_LIST_FILE ="csv_data/movie_list.csv"
TMDB_BASE_URL ="https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}

# 保存电影数据
def save_all_movies(all_movies):
    os.makedirs(os.path.dirname(MOVIE_LIST_FILE), exist_ok=True)
    with open(MOVIE_LIST_FILE, mode='w', newline='', encoding='utf-8-sig') as csvfile:
         writer = csv.DictWriter(csvfile,fieldnames=["电影名","电影年份","电影数据","电影标签","电影时长","电影评分","电影语言","电影导演","电影作者","电影口号","电影描述"])
         writer.writeheader()
         writer.writerows(all_movies)
# 获取电影数据
def get_movie_info(movie_info_url):
#     发送请求，获取数据
    movie_response = requests.get(movie_info_url, headers=HEADERS, timeout=60)
    print(f"发送请求{movie_info_url}，获取电影详情数据")
# 2.解析数据，获取电影详情
    movie_document = html.fromstring(movie_response.text)
    movie_names = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    movie_years =movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")
    movie_data =movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")
    movie_tags = movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")
    movie_cost_time =movie_document.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")
    movie_scores =movie_document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    movie_language = movie_document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    movie_director = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    movie_authors = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')
    movie_slogans = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')
    movie_descriptions = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')
# 3.返回电影详情
    movie_info ={
        "电影名":movie_names[0].strip() if movie_names else '',
        "电影年份":movie_years[0].strip() if movie_years else '',
        "电影数据":movie_data[0].strip() if movie_data else '',
        "电影标签":",".join(movie_tags) if movie_tags else '',
        "电影时长":movie_cost_time[0].strip() if movie_cost_time else '',
        "电影评分":movie_scores[0].strip() if movie_scores else '',
        "电影语言":movie_language[0].strip() if movie_language else '',
        "电影导演":",".join(movie_director) if movie_director else '',
        "电影作者":",".join(movie_authors) if movie_authors else '',
        "电影口号":movie_slogans[0].strip() if movie_slogans else '',
        "电影描述":movie_descriptions[0].strip() if movie_descriptions else '',

    }
    return movie_info

# 主函数，核心逻辑

def main():

    # 设置要爬取的页数
    page_count = 3

    # 保存所有电影
    all_movies = []

    # 遍历每一页
    for page in range(1, page_count + 1):

        # 拼接当前页面的URL
        page_url = TMDB_TOP_URL + f"?page={page}"

        print(f"\n========== 正在获取第 {page} 页 ==========")

        # 1.发送请求
        response = requests.get(
            page_url,
            headers=HEADERS,
            timeout=60
        )

        print(f"发送请求：{page_url}")

        # 2.解析数据
        document = html.fromstring(response.text)

        movie_list = document.xpath(
            '/html/body/div[2]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div'
        )

        print(f"第 {page} 页找到 {len(movie_list)} 部电影")

        # 3.遍历电影列表
        for movie in movie_list:

            movie_urls = movie.xpath('.//div/div/a/@href')

            if movie_urls:

                movie_info_url = TMDB_BASE_URL + movie_urls[0]

                movie_info = get_movie_info(movie_info_url)

                all_movies.append(movie_info)

    # 4.保存所有电影
    print("\n保存电影数据到CSV文件")

    save_all_movies(all_movies)

    print(f"一共获取 {len(all_movies)} 部电影")

if __name__== '__main__':
    main()