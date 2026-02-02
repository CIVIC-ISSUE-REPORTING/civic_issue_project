# AWS S3 Configuration

## Bucket Setup

1. Create S3 bucket: `civic-issues-bucket`
2. Configure bucket policy for public read access (images only)
3. Enable versioning
4. Set up lifecycle rules for old object deletion

## IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::civic-issues-bucket/*"
    }
  ]
}
```

## Environment Variables

```bash
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
S3_BUCKET=civic-issues-bucket
AWS_REGION=us-east-1
```

## File Structure

```
civic-issues-bucket/
├── issues/
│   ├── images/
│   └── documents/
├── profiles/
└── temp/
```
