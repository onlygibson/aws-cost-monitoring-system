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

## Challenges & Resolution

**Challenge:**  
While testing the Lambda function that generates weekly cost reports, the function failed with an `AccessDeniedException` when calling the AWS Cost Explorer API (`GetCostAndUsage`).

**Root Cause:**  
The IAM role attached to the Lambda function did not have permission to access AWS Cost Explorer. By default, Lambda execution roles do not include billing or cost management permissions.

**Resolution:**  
I updated the Lambda IAM execution role by attaching AWS-managed billing permissions that allow Cost Explorer access (`ce:GetCostAndUsage`). After updating the role, the Lambda function executed successfully and was able to retrieve cost data and store the report in Amazon S3.

**Outcome:**  
The system now successfully generates automated weekly cost reports, reinforcing proper IAM least-privilege configuration and service-to-service access in AWS.

