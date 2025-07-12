# Health & Wellness Buddy - Streamlit Deployment

This repository now includes a Streamlit frontend for the Health & Wellness Buddy application, providing an interactive web interface for managing wellness goals, tracking progress, and getting AI-powered insights.

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-repo-url>
   cd HealthWellnessBuddy
   ```

2. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**:
   - Streamlit Frontend: http://localhost:8501
   - API Backend: http://localhost:5000

### Option 2: Local Development

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Express API backend** (in one terminal):
   ```bash
   npm run dev
   ```

3. **Start the Streamlit frontend** (in another terminal):
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Access the application**:
   - Streamlit Frontend: http://localhost:8501

## 📋 Features

### Dashboard
- Overview of wellness metrics
- Recent activity tracking
- Progress visualization

### Wellness Goals
- Create and manage wellness goals
- Track progress towards goals
- AI-powered goal recommendations

### Daily Tasks
- View and complete daily tasks
- Track completion rates
- Progress visualization

### Progress Tracking
- Log progress entries
- Visualize progress over time
- Track multiple metrics

### Workout Log
- Log workout sessions
- Track calories burned
- Analyze workout patterns

### Nutrition Log
- Log nutrition entries
- Track macronutrients
- Visualize nutrition data

### AI Insights
- Get personalized insights
- Receive recommendations
- Motivation messages

## 🐳 Deployment Options

### 1. Docker Deployment

Build and run the containers:
```bash
docker-compose up --build -d
```

### 2. Streamlit Cloud Deployment

1. Push your code to GitHub
2. Connect your repository to Streamlit Cloud
3. Set the main file path to `streamlit_app.py`
4. Deploy

### 3. Heroku Deployment

1. Create a `Procfile`:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. Deploy to Heroku:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### 4. Railway Deployment

1. Connect your GitHub repository to Railway
2. Set the build command: `pip install -r requirements.txt`
3. Set the start command: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`

## 🔧 Configuration

### Environment Variables

- `API_BASE_URL`: URL of your Express API backend (default: http://localhost:5000/api)

### Streamlit Configuration

The app uses a custom theme defined in `.streamlit/config.toml`:
- Primary color: Blue (#1f77b4)
- Background: White
- Secondary background: Light gray

## 📊 API Integration

The Streamlit app communicates with your Express API through the following endpoints:

- `GET /api/wellness-goals` - Fetch user goals
- `POST /api/wellness-goals` - Create new goal
- `GET /api/daily-tasks` - Fetch daily tasks
- `PATCH /api/daily-tasks/:id` - Update task completion
- `GET /api/progress` - Fetch progress entries
- `POST /api/progress` - Create progress entry
- `GET /api/workouts` - Fetch workout sessions
- `POST /api/workouts` - Log workout session
- `GET /api/nutrition` - Fetch nutrition logs
- `POST /api/nutrition` - Log nutrition entry
- `GET /api/insights` - Get AI insights

## 🛠️ Development

### Adding New Features

1. **Add new API endpoints** in `server/routes.ts`
2. **Update the Streamlit app** in `streamlit_app.py`
3. **Test locally** before deploying

### Customizing the UI

- Modify the CSS in the `st.markdown()` section
- Update the theme in `.streamlit/config.toml`
- Add new pages by extending the navigation

### Data Visualization

The app uses Plotly for interactive charts:
- Line charts for progress tracking
- Pie charts for workout distribution
- Bar charts for nutrition data

## 🔍 Troubleshooting

### Common Issues

1. **API Connection Error**:
   - Ensure the Express API is running
   - Check the `API_BASE_URL` configuration
   - Verify network connectivity

2. **Port Conflicts**:
   - Change ports in `docker-compose.yml`
   - Use different ports for local development

3. **Dependency Issues**:
   - Update `requirements.txt` with new dependencies
   - Rebuild Docker containers

### Logs

- **Streamlit logs**: Check the terminal output
- **Docker logs**: `docker-compose logs streamlit`
- **API logs**: `docker-compose logs api`

## 📈 Monitoring

The application includes health checks:
- Streamlit: `/_stcore/health`
- API: `/api/wellness-goals`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. 