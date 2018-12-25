import csv

class Uhp:

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
                 'Mens': 'Mens',
                 'Mens Accessories': 'Accessories',
                 'Mens Clothing': 'Clothing',
                 'Mens Footwear': 'Shoes'
                 }
uhp = Uhp()

data = [];
with open('datafeed_525247.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # print(f'Processing item line: {line_count+1} - name: {row[1]} rrp price: {row[21]} sale price: {row[7]}')
        if line_count == 0:
            # Actual columns from Awin file are:
            # aw_deep_link, product_name, aw_product_id, merchant_product_id, merchant_image_url, description, merchant_category, search_price, merchant_name, merchant_id, category_name, category_id, aw_image_url, currency, store_price, delivery_cost, merchant_deep_link, language, last_updated, display_price, data_feed_id, rrp_price, saving, product_price_old
            # cols = (f'{row[0]}, {row[1]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[8]}, {row[9]}, {row[7]}, {row[21]}, uhp_category')

            # Woocommerce Columns for import
            # External URL, Name, ID, Images, Description, x, x, x, Sale price, Regular price, Categories
            # cols = (f'External URL, Name, SKU, Images, Description, {row[6]}, {row[8]}, {row[9]}, Sale price, Regular price, Categories, Type')
            # cols = (f'Name, SKU, Images, Short Description, {row[6]}, {row[8]}, {row[9]}, Sale price, Regular price, Categories, External URL, Type')
            cols = (f'External URL, Name, Images, Sale price, Regular price, Categories, Type')
            # print(f'Column names are {(cols)}')
            data.append(cols)
        else:
            if float(row[7]) <= float(row[21]) / 2:
                # print(f'HALF PRICE..... {row[0]}, {row[1]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[8]}, {row[9]}, {row[7]}, {row[21]}')
                # aw_deep_link, product_name, merchant_product_id, merchant_image_url, description, merchant_category, merchant_name, merchant_id, search_price, rrp_price
                # item = (f'"{row[0]}", "{row[1]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[8]}", "{row[9]}", {row[7]}, {row[21]}') + ", \"" + uhp.replace_category(row[6]) + "\"" + ", \"external\""
                # item = (f'"{row[5]}", "{row[3]}", "{row[4]}", "{row[1]}", "{row[6]}", "{row[8]}", "{row[9]}", {row[7]}, {row[21]}, "{uhp.replace_category(row[6])}", "{row[0]}", \"simple\"')

                # Column mappings Awin -> UHP:
                # aw_deep_link, description, merchant_image_url, search_price, rrp_price, merchant_category, custom field is Type
                item = (f'"{row[0]}", "{row[5]}", "{row[4]}", "{row[7]}", {row[21]}, "{uhp.replace_category(row[6])}", \"simple\"')
                data.append(item)
                print(f'UHP Item found line: {line_count+1} -> {item}')
        line_count += 1

    print(f'\nProcessed {int(line_count) -1} lines items. \r\n Under Half Price Items found: {len(data) -1}')

with open( 'datafeed_uhp_output.csv', "w") as csv_file:
    # writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE, escapechar=' ')
    for line in data:
        # print(line)
        csv_file.write(line )
        csv_file.write('\n')
    # writer.writerows([data])

    print(f'Output written to file: datafeed_uhp_output.csv')