# aws-cost-monitoring-system

Built an automated AWS cost monitoring system using AWS Budgets, SNS, Lambda, Cost Explorer, and Amazon S3 to track spending, send alerts at defined thresholds, and generate scheduled cost reports.

## Architecture Overview

This system monitors AWS spending using AWS Budgets and Cost Explorer.  
When spending exceeds defined thresholds, alerts are sent via Amazon SNS.  
A scheduled AWS Lambda function generates weekly cost reports and stores them securely in Amazon S3.

## Architecture Flow

AWS Services  
→ AWS Cost Explorer & AWS Budgets  
→ Budget Thresholds (50%, 80%, 100%)  
→ Amazon SNS (Email/SMS Alerts)  
→ AWS Lambda (Weekly Cost Report Automation)  
→ Amazon S3 (Cost Report Storage)
