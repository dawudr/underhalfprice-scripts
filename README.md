# underhalfprice-scripts
Under Half Price Data feed automation and Ingestion

## To run from command
```
py merchant_footasylum.py
```

File is sample datafeed_525247.csv to parse and output under half price items into datafeed_uhp_output.csv

Source and Destination file location are updated by changing the filename in the following lines:

## Input CSV:
Edit lines 41:

```
with open('datafeed_525247.csv') as csv_file:
```

## Output CSV:
And line 81:

```
with open( 'datafeed_uhp_output.csv', "w") as csv_file:
```


