# MongoDB Collections

## Issues Collection (for flexible schema)

```json
{
  "_id": "ObjectId",
  "user_id": "string",
  "title": "string",
  "description": "string",
  "category": "string",
  "severity": "string",
  "status": "string",
  "location": {
    "type": "Point",
    "coordinates": [longitude, latitude]
  },
  "address": "string",
  "images": ["url1", "url2"],
  "department": "string",
  "assigned_worker_id": "string",
  "deadline": "ISODate",
  "votes": {
    "upvotes": 0,
    "downvotes": 0
  },
  "tags": ["tag1", "tag2"],
  "metadata": {
    "device": "string",
    "app_version": "string",
    "ml_predictions": {
      "category": "string",
      "severity": "string",
      "confidence": 0.95
    }
  },
  "created_at": "ISODate",
  "updated_at": "ISODate"
}
```

## User Activity Collection

```json
{
  "_id": "ObjectId",
  "user_id": "string",
  "action": "string",
  "resource": "string",
  "resource_id": "string",
  "timestamp": "ISODate",
  "metadata": {}
}
```

## Analytics Collection

```json
{
  "_id": "ObjectId",
  "date": "ISODate",
  "metrics": {
    "total_issues": 0,
    "resolved_issues": 0,
    "avg_resolution_time": 0,
    "by_category": {},
    "by_severity": {},
    "by_department": {}
  }
}
```

## Geospatial Indexes

```javascript
db.issues.createIndex({ location: "2dsphere" })
```

## Common Queries

```javascript
// Find issues near a location
db.issues.find({
  location: {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [longitude, latitude]
      },
      $maxDistance: 5000  // 5km radius
    }
  }
})

// Find issues by category and status
db.issues.find({
  category: "road",
  status: "pending"
})
```
