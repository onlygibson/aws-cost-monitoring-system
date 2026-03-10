import boto3
import json
from datetime import date, timedelta

ce = boto3.client('ce')
s3 = boto3.client('s3')

BUCKET_NAME = 'aws-cost-reports-gibson'

def lambda_handler(event, context):
    end = date.today()
    start = end - timedelta(days=7)

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    file_name = f"weekly-report-{end}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(response, indent=2),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': f'Report saved to S3 as {file_name}'
    }

