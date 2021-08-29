import json
from logging import exception
import boto3

def sort_by_value(d, value):
    return sorted(d, key = lambda x: x[value])

def upload_to_s3(bucket_name, key, body):
    response = s3.put_object(
        Body=body,
        Bucket= bucket_name,
        Key=key
    )
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    if status_code == 200:
        print("Successfully uploaded...")
    else:
        print("Failed...")

try:
    s3 = boto3.client('s3')
    bucket_name = 'bec-poc-pipeline'

    json_object = [{"name":"John", "age":'30', "city":"New York" }, {"name":"AJohn", "age":'31', "city":"New York"}, {"name":"BJohn", "age":'32', "city":"New York"}]
    # sort by name
    sort_by_name=sort_by_value(json_object, "name")
    sort_name_json = json.dumps(sort_by_name)
    print(sort_name_json)

    # upload json file
    upload_to_s3(bucket_name, 'file.json', sort_name_json)

    ## csv
    main = []
    keys = [ key for key in json_object[0] ]
    main.append(keys)
    for d in json_object:
        l = []
        for key in keys:
            l.append(d[key])
        main.append(l)
        # list.append()
    print(main)
    nl = []
    for l in main:
        nl.append(','.join(l))
    print(nl)
    csv_str = '\n'.join(nl)
    upload_to_s3(bucket_name, 'file.csv', csv_str)


except Exception as exp:
    print(str(exp))