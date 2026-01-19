## Architecture Overview

This system monitors AWS spending using AWS Budgets and Cost Explorer. 
When spending exceeds defined thresholds, alerts are sent via Amazon SNS.
A scheduled AWS Lambda function generates weekly cost reports and stores them securely in Amazon S3.
