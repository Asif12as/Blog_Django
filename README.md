# Blog_DjangO

# Django Blog Project

This project demonstrates the implementation of a Django-based blog application with user authentication and API endpoints. It consists of two apps: `blog` for managing blog posts and `users` for user authentication.

## Features

- User authentication using JWT without third-party libraries.
- Models for blog posts and comments with necessary fields.
- APIs for creating blog posts and comments, listing blog posts and their comments, and updating blog posts.

## Setup Instructions

1. Clone the repository: `git clone https://github.com/your-username/django-blog-project.git`
2. Navigate to the project directory: `cd django-blog-project`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## API Endpoints

1. **User Authentication**
   - `POST /api/token/`: Obtain a JWT token for authentication.
   - `POST /api/token/refresh/`: Refresh an existing JWT token.

2. **Blog Posts**
   - `GET /api/posts/`: List all blog posts.
   - `POST /api/posts/`: Create a new blog post (authentication required).
   - `PUT /api/posts/<post_id>/`: Update a blog post (authentication and author verification required).

3. **Comments**
   - `GET /api/posts/<post_id>/comments/`: List all comments on a blog post.
   - `POST /api/posts/<post_id>/comments/`: Create a comment on a blog post (authentication required).

## Note

- This project uses JWT authentication without third-party libraries. Instead, it utilizes the `pyjwt` library for JWT token generation.
- Make sure to set your own `SECRET_KEY` in the project's settings.
- Remember that this is a sample README. Feel free to modify and expand upon it as needed.

For more information about JWT, refer to the [JWT Official Website](https://jwt.io/introduction/).

Happy coding!
