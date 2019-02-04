# underhalfprice-scripts
Under Half Price Data feed automation and Ingestion

This script reads or streams from URL a Gzipped CSV product feed file and filters out under half price items and places results into a new CSV

This script take a CSV file from AWIN using -> Links & Tools / Create-a-Feed option.

With the following fields in exact order:
```
aw_deep_link,aw_product_id,merchant_product_id,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,rrp_price
```

### To created a download link:
https://productdata.awin.com/datafeed/download/apikey/xxxxxxx- add api key here - xxxxxxxx/language/en/fid/2832/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,rrp_price/format/csv/delimiter/%2C/compression/gzip/

## To run from command
```
py merchant_footasylum.py <source csv file>
```

```
py merchant_footasylum.py datafeeds.csv.gz
py merchant_footasylum.py https://productdata.awin.com/datafeed/download/apikey/xxxxxxx- add api key here - xxxxxxxx/language/en/fid/2832/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,rrp_price/format/csv/delimiter/%2C/compression/gzip/
```

File is parsed and output is created with under half price items into datafeed_uhp_<todays date and time>.csv

Source and Destination file location are updated by changing the filename in the following lines:


