# underhalfprice-scripts
Under Half Price Data feed automation and Ingestion

This script take a CSV file from AWIN using -> Links & Tools / Create-a-Feed option.


With the following fields in exact order:
```
aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,merchant_id,category_name,category_id,aw_image_url,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,display_price,data_feed_id,rrp_price,saving,product_price_old
```

To created a download link:
https://productdata.awin.com/datafeed/download/apikey/xxxxxxx- add api key here - xxxxxxxx/language/en/fid/2832/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,merchant_id,category_name,category_id,aw_image_url,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,display_price,data_feed_id,rrp_price,saving,product_price_old/format/csv/delimiter/%2C/compression/gzip/


## To run from command
```
py merchant_footasylum.py <source csv file>
```

File is parsed and output is created with under half price items into datafeed_uhp_<todays date and time>.csv

Source and Destination file location are updated by changing the filename in the following lines:


