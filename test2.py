from amazon.paapi import AmazonAPI

KEY    = "AKIAI7K5KRMGQS3KMWPQ"
SECRET = "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"
TAG    = "haruyasu0f-22"
COUNTRY = "JP"
keyword = "任天堂Switch"


amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)
print(amazon)
# products = amazon.search_items(keywords=keyword)
item = amazon.get_items('B01N5IB20Q')[0]
print(item)
# asin     = products["data"][0].asin
# price    = products["data"][0].offers.listings[0].price.amount
# url      = products["data"][0].detail_page_url
# title    = products["data"][0].item_info.title.display_value

# print(asin, price, url, title)