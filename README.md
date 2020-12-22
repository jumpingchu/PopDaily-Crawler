# PopDaily-Crawler
【Python】爬取 PopDaily 近期文章資訊


## 版本紀錄
### ver 1.0
* `PopDailyPages.py` 收集近期 PGC 文章連結並分類
    * 目前分類 japan, travel, food, life, press, other
* `popdaily_crawler.ipynb` 由連結去取得文章資訊
    * 文章日期、分類、網址、標題、內文、標籤
    * 產出各分類的 `pandas.DataFrame`
    * 寫進同一個 Excel 檔案的不同 sheet
    * ”標籤“依據出現頻率找出前 20 名
