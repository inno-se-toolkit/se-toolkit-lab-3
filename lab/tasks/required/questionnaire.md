# Questionnaire — API Exploration

Fill in each answer below. Replace `___` with the correct value.

## Items endpoints

### GET /items

1. HTTP method: GET
2. Path: /items
3. Status code (success): 200
4. Response type (array or object): [
  {
    "parent_id": null,
    "type": "course",
    "description": "A course on SE principles and practices.",
    "created_at": "2026-02-20T15:09:12.312659",
    "id": 1,
    "title": "Software Engineering",
    "attributes": {
      "instructors": [
        "Alice Johnson"
      ]
    }
  },
  {
    "parent_id": 1,
    "type": "lab",
    "description": "Learn Git basics: commits, branches, merging.",
    "created_at": "2026-02-20T15:09:12.314114",
    "id": 2,
    "title": "Version Control with Git",
    "attributes": {
      "start": "2025-09-08T09:00:00",
      "finish": "2025-09-14T23:59:00"
    }
  },
  {
    "parent_id": 1,
    "type": "lab",
    "description": "Design RESTful APIs using HTTP methods and status codes.",
    "created_at": "2026-02-20T15:09:12.314114",
    "id": 3,
    "title": "REST API Design",
    "attributes": {
      "start": "2025-09-15T09:00:00",
      "finish": "2025-09-21T23:59:00"
    }
  },
  {
    "parent_id": 1,
    "type": "lab",
    "description": "Containerize applications using Docker and Docker Compose.",
    "created_at": "2026-02-20T15:09:12.314114",
    "id": 4,
    "title": "Docker Fundamentals",
    "attributes": {
      "start": "2025-09-22T09:00:00",
      "finish": "2025-09-28T23:59:00"
    }
  },
  {
    "parent_id": 1,
    "type": "lab",
    "description": "Connect a web application to a PostgreSQL database.",
    "created_at": "2026-02-20T15:09:12.314114",
    "id": 5,
    "title": "Database Integration",
    "attributes": {
      "start": "2025-09-29T09:00:00",
      "finish": "2025-10-05T23:59:00"
    }
  },
  {
    "parent_id": 5,
    "type": "task",
    "description": "Write and run automated tests for Python applications.",
    "created_at": "2026-02-20T15:09:12.315355",
    "id": 6,
    "title": "Testing with pytest",
    "attributes": {}
  },
  {
    "parent_id": 4,
    "type": "task",
    "description": "Basic server management and security hardening.",
    "created_at": "2026-02-20T15:09:12.315355",
    "id": 7,
    "title": "Linux Server Administration",
    "attributes": {}
  },
  {
    "parent_id": 6,
    "type": "step",
    "description": "Automate testing and deployment with GitHub Actions.",
    "created_at": "2026-02-20T15:09:12.315355",
    "id": 8,
    "title": "CI/CD Pipelines",
    "attributes": {}
  }
]

### GET /items/{item_id}

1. Status code (item found): 200
2. Status code (item not found): 404

### POST /items

1. HTTP method: Post
2. Status code (created successfully): 201

### PUT /items/{item_id}

1. HTTP method: Put
2. Status code (updated successfully): 200

## Authentication

1. What happens when you call an endpoint without the API key? (status code): ___
2. Where do you set the API key value for Docker Compose? (file name): ___
