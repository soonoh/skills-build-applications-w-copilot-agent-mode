# OctoFit Tracker

A fitness tracking application built with Django REST Framework and React, featuring superhero-themed data!

## Features

- **User Management**: Track superhero users from Marvel and DC teams
- **Team Management**: View and manage fitness teams
- **Activity Logging**: Log and track various fitness activities
- **Leaderboard**: See who's leading in fitness points
- **Workout Suggestions**: Browse personalized workout recommendations

## Tech Stack

### Backend
- Python 3.12
- Django 4.1.7
- Django REST Framework 3.14.0
- MongoDB (via Djongo)
- CORS Headers

### Frontend
- React 18
- React Router DOM
- Bootstrap 5
- Modern ES6+ JavaScript

## Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- MongoDB (running on localhost:27017)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd octofit-tracker/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Populate the database with test data:
   ```bash
   python manage.py populate_db
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd octofit-tracker/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The application will open at `http://localhost:3000`

## API Endpoints

- **GET /api/users/** - List all users
- **GET /api/teams/** - List all teams
- **GET /api/activities/** - List all activities
- **GET /api/leaderboard/** - View leaderboard
- **GET /api/workouts/** - List workout suggestions

All endpoints support full CRUD operations (GET, POST, PUT, DELETE).

## Development

### Running in VS Code

Use the provided launch configurations:
- **Launch Django Backend** - Starts the Django server
- **Launch React Frontend** - Starts the React development server

### Running in GitHub Codespaces

The application is pre-configured for GitHub Codespaces with:
- Automatic port forwarding (3000, 8000, 27017)
- MongoDB setup via Docker
- Environment-aware URL configuration

## Sample Data

The database comes pre-populated with superhero-themed data including:
- 10 users (5 from Team Marvel, 5 from Team DC)
- 2 teams (Marvel and DC)
- 20 activities (various superhero training exercises)
- 10 leaderboard entries
- 5 workout suggestions

## Architecture

```
octofit-tracker/
├── backend/
│   ├── venv/                   # Python virtual environment
│   ├── octofit_tracker/        # Django project
│   │   ├── models.py           # Data models
│   │   ├── serializers.py      # REST serializers
│   │   ├── views.py            # API views
│   │   ├── urls.py             # URL routing
│   │   ├── settings.py         # Django settings
│   │   └── management/
│   │       └── commands/
│   │           └── populate_db.py  # Database seeding
│   └── requirements.txt        # Python dependencies
└── frontend/
    ├── public/                 # Static files
    ├── src/
    │   ├── components/         # React components
    │   │   ├── Users.js
    │   │   ├── Teams.js
    │   │   ├── Activities.js
    │   │   ├── Leaderboard.js
    │   │   └── Workouts.js
    │   ├── App.js              # Main app component
    │   ├── App.css             # Styles
    │   └── index.js            # Entry point
    └── package.json            # Node dependencies
```

## Notes

- The SECRET_KEY and CORS settings are configured for development only
- For production deployment, ensure proper security configurations
- MongoDB must be running before starting the backend server
- The application uses environment variables for Codespace URL configuration

## License

MIT
