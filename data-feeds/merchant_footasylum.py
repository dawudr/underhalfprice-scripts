import csv
import sys
import time
import gzip
import io
import urllib.request
import os

class Uhp:
    # Utility functions
    def replace_category(self, input) :
        x = input.split(",")
        output = ""

        count_level = 0
        for y in x:
            # We only interested in 2 sub categories
            if count_level < 2:
                if output == "":
                    # First Category
                    # Check if categories key exists so we can replace from dictionary
                    if y in category_dict:
                        output += category_dict[y]
                    else:
                        # Break loop
                        return "Uncategorized"
                else:
                    # 2nd or more categories
                    if y in category_dict:
                        output += ", " + category_dict[y]
                    # else Should we add as a new category here?
                count_level += 1
        return (output)



category_dict = {'Womens': 'Ladies',
                 'Womens Footwear': 'Shoes and Bags',
                 'Womens Accessories': 'Accessories',
                 'Womens Clothing': 'Clothing',
                 'Kids': 'Children',
                 'Junior Clothing': 'Clothing',
                 'Kids Accessories': 'Everything Else',
                 'Kids Footwear': 'Everything Else',
                 'Nursery Clothing': 'Everything Else',
                 'Mens': 'Men',
                 'Mens Accessories': 'Accessories',
                 'Mens Clothing': 'Clothing',
                 'Mens Footwear': 'Shoes'
                 }

# This script reads or streams from URL a Gzipped CSV product feed file and filters out under half price items and places results into a new CSV
# To run:
# py merchant_footasylum.py datafeeds.csv.gz
# py merchant_footasylum.py https://productdata.awin.com/datafeed/download/apikey/9c18bf753049bed5557a1dde6d47142c/language/en/fid/2832/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,rrp_price/format/csv/delimiter/%2C/compression/gzip/


# Expected URL:
# https://productdata.awin.com/datafeed/download/apikey/9c18bf753049bed5557a1dde6d47142c/language/en/fid/2832/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,rrp_price/format/csv/delimiter/%2C/compression/gzip/
print('Opening source CSV: ' + sys.argv[1])
path = sys.argv[1]
data = [];
uhp = Uhp()

# Check if file or url
if os.path.isfile(path):
    response = path
else:
    response = urllib.request.urlopen(path)

with gzip.open(response) as csv_file:
    csv_reader = csv.reader(io.TextIOWrapper(csv_file, newline=""), delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # Actual columns from Awin file are:
            # aw_deep_link, product_name, aw_product_id, merchant_product_id, merchant_image_url, description, merchant_category, search_price, rrp_price

            # Woocommerce Columns for import
            cols = (f'External URL, Name, Images, Sale price, Regular price, Categories, Type')
            data.append(cols)
        else:
            if float(row[7]) <= float(row[8]) / 2:

                # Column mappings Awin -> UHP:
                # aw_deep_link, description, merchant_image_url, search_price, rrp_price, merchant_category, custom field is Type
                item = (f'"{row[0]}", "{row[5]}", "{row[4]}", "{row[7]}", {row[8]}, "{uhp.replace_category(row[6])}", \"external\"')
                data.append(item)
                print(f'UHP Item found line: {line_count+1} -> {item}')
        line_count += 1

    print(f'\nProcessed {int(line_count) -1} lines items. \r\n Under Half Price Items found: {len(data) -1}')

filetimestr = 'datafeed_uhp_' + time.strftime("%Y%m%d-%H%M%S") + '.csv'
with open( filetimestr, "w") as csv_file:
    for line in data:
        csv_file.write(line )
        csv_file.write('\n')

    print(f'Output written to file: ' + filetimestr)