# Backend Wizards — Stage 0 Task: Dynamic Profile Endpoint

HNGi13 Backend Internship Stage 0 task!  
This project implements a RESTful API endpoint that returns my profile information along with a dynamic cat fact fetched from an external API.

---

## Project Overview

**Endpoint:**  
`GET /me`

**Features:**  
- Returns profile info in strict JSON format
- Fetches a new cat fact from [Cat Facts API](https://catfact.ninja/fact) on every request
- Provides current UTC timestamp in ISO 8601 format
- Handles external API errors gracefully

---

## Response Format

```json
{
  "status": "success",
  "user": {
    "email": "lwltjdn@gmail.com",
    "name": "Lawal Tajudeen Ogunsola",
    "stack": "Python/Django REST Framework"
  },
  "timestamp": "2025-10-21T12:34:56.789Z",
  "fact": "A random cat fact from Cat Facts API"
}
```

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Requests

---

## Project Structure

```

```

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone git@github.com:lawalTheWest/HNG_backend_stage_0.git
   cd backend_profile_project
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python3 manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python3 manage.py runserver
   ```

6. **Test the endpoint**
   - Open [http://127.0.0.1:8000/me/](http://127.0.0.1:8000/me/) in your browser or use Postman.

---

## Dependencies

See the `requirements.txt`

---

## Environment Variables

No environment variables are required for local development.

---

## API Documentation

### GET `/me`

- **Description:** Returns profile info and a dynamic cat fact.
- **Response:**  
  - `200 OK` with JSON as shown above
  - Content-Type: `application/json`
- **Error Handling:**  
  - If Cat Facts API fails, returns a fallback message in the `fact` field.

---

## Testing

test the endpoint using Postman or curl or run the py-test:


```bash
curl http://127.0.0.1:8000/me/
```

```python3
python3 manage.py test api

```

---

## Codebase Highlights

- **`api/views.py`**  
  Implements the `/me` endpoint, fetches cat facts, and formats the response.

- **`api/urls.py`**  
  Routes `/me/` to the profile endpoint.

- **`backend_profile_project/urls.py`**  
  Includes API app URLs.

---

## Checklist for this project

- [x] Working GET `/me` endpoint
- [x] Strict response format
- [x] Dynamic timestamp and cat fact
- [x] Error handling
- [x] Clear README and setup instructions

---

## Author

- **Name:** Lawal Tajudeen Ogunsola
- **Email:** lwltjdn@gmail.com
- **Stack:** Python/Django REST Framework

---

## LinkedIn Post

Don't forget to create a rich post on LinkedIn, Dev.to, Hashnode, Medium, or X (Twitter) detailing your work process and learnings!

---