import boto3


def create_movie_table(table_name):
    dynamodb = boto3.client("dynamodb")
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {"AttributeName": "name", "KeyType": "HASH"},
            {"AttributeName": "country", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "name", "AttributeType": "S"},
            {"AttributeName": "country", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    return table


table_name = "StudentDetails"
create_movie_table(table_name=table_name)
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(table_name)
print(f"table status {table.table_status}")
