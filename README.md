# Guidance for Task: Comment Moderation & Author Notification API

## Project Overview

This FastAPI project represents a blogging platform backend service. The service includes existing support for articles and aims to expand functionality to handle comment management and real-time notification simulation for article authors upon new comment submissions.

---

## Task Requirements

You are expected to:

1. **Implement Comment Endpoints**
   - **Add a POST endpoint** to allow users to submit comments tied to a specific article.
   - **Add a GET endpoint** to list comments for a given article.
   - **Organize routes** using FastAPI routers for modularity.

2. **Validation & Persistence**
   - **Validate** incoming comment data using Pydantic models.
   - **Store** all comments using SQLAlchemy ORM with proper linkage to existing articles.
   - Ensure comments link only to valid articles.

3. **Author Notifications**
   - On new comment submission, **trigger a FastAPI background task** to simulate sending an email notification to the article's author.
   - The simulation should log or visibly represent a successful notification (no actual email sending is needed).

4. **Custom Error Handling**
   - All errors (e.g., missing article, invalid input) must return custom structured responses.

5. **API Documentation**
   - Ensure OpenAPI docs reflect all endpoints, models, input examples, and custom error responses.

6. **Dependency Injection & Modularity**
   - Use dependency injection for DB session management.
   - Maintain modularity across routers and models.

---

## Your Implementation Guide

- **You will need to connect the API endpoints and validation logic.**
- FastAPI routers for comments and notifications are already in the project structure.
- SQLAlchemy models are partially provided; assume the `Article` model exists as described in the comments.
- There are placeholder schemas and a background notification simulation utility ready to use.

---

## Verifying Your Solution

- **Add and list comments** using API requests to see if data is correctly validated, stored, and associated with valid articles.
- **Check server logs or output** after submitting a comment to verify the background task is triggered for author notification.
- **Test error conditions** (posting to non-existent articles, invalid payloads) to confirm custom error responses are returned.
- **Inspect OpenAPI docs** (if enabled) to ensure models, endpoints, and example responses appear correctly.
- **Review code structure** to ensure proper use of routers, dependency injection, and modular components.

---

## Additional Info

- Do **not** modify or add to any Article-related code outside of connecting relationships if needed for comment features.
- No actual email should be sent; logging or a print statement is sufficient for simulating notifications.

Use this guidance and project structure to fulfill all task requirements.