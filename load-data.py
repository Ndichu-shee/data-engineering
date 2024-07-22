import boto3
import json

def load_data(data):
    print("*******")
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table("StudentDetails")
    for item in data:
        name = item["name"]
        country = item["country"]
        print(f"adding student details {name}::{country}")
        table.put_item(Item=item)


if __name__ == "__main__":
    with open("json_data.csv") as json_file:
        students_list = json.load(json_file)
    load_data(students_list)
