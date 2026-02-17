# Cloud Threat Detection System (AWS + Python)

A cloud-based monitoring and alerting system that ingests authentication logs from AWS CloudWatch Logs and detects suspicious login behavior using rule-based analysis.

## Architecture

CloudWatch Logs → Metric Filter → Python Detection Engine → Alert Report

## Features
- AWS CloudWatch log ingestion
- Metric filters for failed login monitoring
- Python detection engine using boto3
- Failed login burst detection (time-based rule)
- Automated alert generation

## Technologies Used
- AWS CloudWatch Logs
- Python
- boto3
- AWS IAM
- CloudWatch Metric Filters

## How to Run

```bash
pip install -r requirements.txt
python -m src.detector.main
```

## Example Detection
Detects multiple failed login attempts within a defined time window and generates alerts.

## Future Improvements
- CloudWatch Alarms
- Lambda-based automation
- Slack/email alerting