import streamlit as st
import requests
import json
from datetime import datetime, date
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Optional

# Configuration
API_BASE_URL = "http://localhost:3000/api"  # Change this to your deployed API URL

# Page configuration
st.set_page_config(
    page_title="Health & Wellness Buddy",
    page_icon="🏃‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #c3e6cb;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #f5c6cb;
    }
</style>
""", unsafe_allow_html=True)

def make_api_request(endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Optional[Dict]:
    """Make API request to the backend"""
    try:
        url = f"{API_BASE_URL}{endpoint}"
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PATCH":
            response = requests.patch(url, json=data)
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🏃‍♂️ Health & Wellness Buddy</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Dashboard", "Wellness Goals", "Daily Tasks", "Progress Tracking", "Workout Log", "Nutrition Log", "AI Insights"]
    )
    
    if page == "Dashboard":
        show_dashboard()
    elif page == "Wellness Goals":
        show_wellness_goals()
    elif page == "Daily Tasks":
        show_daily_tasks()
    elif page == "Progress Tracking":
        show_progress_tracking()
    elif page == "Workout Log":
        show_workout_log()
    elif page == "Nutrition Log":
        show_nutrition_log()
    elif page == "AI Insights":
        show_ai_insights()

def show_dashboard():
    st.header("📊 Dashboard")
    
    # Get data for dashboard
    goals = make_api_request("/wellness-goals")
    tasks = make_api_request("/daily-tasks")
    progress = make_api_request("/progress?limit=7")
    
    # Create metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Active Goals",
            value=len(goals) if goals else 0,
            delta="+2 this week" if goals and len(goals) > 0 else None
        )
    
    with col2:
        completed_tasks = len([task for task in tasks if task.get('completed', False)]) if tasks else 0
        total_tasks = len(tasks) if tasks else 0
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        st.metric(
            label="Today's Progress",
            value=f"{completed_tasks}/{total_tasks}",
            delta=f"{completion_rate:.1f}%"
        )
    
    with col3:
        st.metric(
            label="Streak Days",
            value="5",
            delta="+1 day"
        )
    
    with col4:
        st.metric(
            label="Weekly Workouts",
            value="3",
            delta="+1 this week"
        )
    
    # Recent activity
    st.subheader("Recent Activity")
    if progress:
        df = pd.DataFrame(progress)
        df['created_at'] = pd.to_datetime(df['created_at'])
        df = df.sort_values('created_at', ascending=False).head(5)
        
        for _, row in df.iterrows():
             created_at = pd.to_datetime(row['created_at'])
             st.write(f"📝 {row['notes']} - {created_at.strftime('%Y-%m-%d')}")
        # for index, row in df.head(10).iterrows():
        # created_at = pd.to_datetime(row['created_at'])
        # created_at_str = created_at.strftime('%Y-%m-%d') if pd.notnull(created_at) else "❌ No date"
        # st.write(f"📝 {row['notes']} - 📅 {created_at_str}")

    else:
        st.info("No recent activity to display")

def show_wellness_goals():
    st.header("🎯 Wellness Goals")
    
    # Create new goal form
    with st.expander("Create New Goal", expanded=False):
        with st.form("new_goal_form"):
            goal_type = st.selectbox(
                "Goal Type",
                ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility", "Mental Health", "Nutrition", "Other"]
            )
            target_value = st.number_input("Target Value", min_value=0.0, step=0.1)
            target_unit = st.text_input("Unit (e.g., kg, miles, minutes)")
            target_date = st.date_input("Target Date")
            description = st.text_area("Description")
            
            submitted = st.form_submit_button("Create Goal")
            
            if submitted:
                goal_data = {
                    "goalType": goal_type,
                    "targetValue": target_value,
                    "targetUnit": target_unit,
                    "targetDate": target_date.isoformat(),
                    "description": description,
                    "status": "active"
                }
                
                result = make_api_request("/wellness-goals", "POST", goal_data)
                if result:
                    st.success("Goal created successfully!")
                    st.rerun()
    
    # Display existing goals
    goals = make_api_request("/wellness-goals")
    
    if goals:
        for goal in goals:
            with st.container():
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.subheader(f"🎯 {goal['goalType']}")
                    st.write(f"**Target:** {goal['targetValue']} {goal['targetUnit']}")
                    st.write(f"**Due:** {goal['targetDate']}")
                    st.write(f"**Description:** {goal['description']}")
                
                with col2:
                    st.write(f"**Status:** {goal['status']}")
                
                with col3:
                    if st.button(f"View Progress", key=f"progress_{goal['id']}"):
                        st.session_state.selected_goal = goal['id']
                        st.rerun()
    else:
        st.info("No wellness goals found. Create your first goal above!")

def show_daily_tasks():
    st.header("📋 Daily Tasks")
    
    # Get today's tasks
    tasks = make_api_request("/daily-tasks")
    
    if tasks:
        # Create task completion form
        with st.form("task_completion_form"):
            for task in tasks:
                completed = st.checkbox(
                    task['task'],
                    value=task['completed'],
                    key=f"task_{task['id']}"
                )
                
                # Update task if status changed
                if completed != task['completed']:
                    make_api_request(f"/daily-tasks/{task['id']}", "PATCH", {"completed": completed})
            
            submitted = st.form_submit_button("Update Tasks")
            if submitted:
                st.success("Tasks updated successfully!")
                st.rerun()
        
        # Progress visualization
        completed_count = len([task for task in tasks if task['completed']])
        total_count = len(tasks)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric(
                label="Completion Rate",
                value=f"{completed_count}/{total_count}",
                delta=f"{(completed_count/total_count*100):.1f}%" if total_count > 0 else "0%"
            )
        
        with col2:
            # Progress bar
            progress = completed_count / total_count if total_count > 0 else 0
            st.progress(progress)
    else:
        st.info("No daily tasks found. Tasks will be generated automatically.")

def show_progress_tracking():
    st.header("📈 Progress Tracking")
    
    # Add new progress entry
    with st.expander("Add Progress Entry", expanded=False):
        with st.form("progress_entry_form"):
            goal_id = st.number_input("Goal ID", min_value=1, value=1)
            metric_value = st.number_input("Metric Value", min_value=0.0, step=0.1)
            metric_type = st.selectbox("Metric Type", ["weight", "distance", "time", "reps", "other"])
            notes = st.text_area("Notes")
            
            submitted = st.form_submit_button("Add Progress Entry")
            
            if submitted:
                progress_data = {
                    "goalId": goal_id,
                    "metricValue": metric_value,
                    "metricType": metric_type,
                    "notes": notes
                }
                
                result = make_api_request("/progress", "POST", progress_data)
                if result:
                    st.success("Progress entry added successfully!")
                    st.rerun()
    
    # Display progress history
    progress = make_api_request("/progress?limit=30")
    
    if progress:
        df = pd.DataFrame(progress)
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        # Progress over time chart
        st.subheader("Progress Over Time")
        fig = px.line(df, x='created_at', y='metricValue', 
                     title="Progress Trend",
                     labels={'metricValue': 'Metric Value', 'created_at': 'Date'})
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent entries table
        st.subheader("Recent Entries")
        st.dataframe(
            df[['created_at', 'metricValue', 'metricType', 'notes']].head(10),
            use_container_width=True
        )
    else:
        st.info("No progress entries found. Add your first entry above!")

def show_workout_log():
    st.header("💪 Workout Log")
    
    # Add new workout
    with st.expander("Log New Workout", expanded=False):
        with st.form("workout_form"):
            workout_type = st.selectbox(
                "Workout Type",
                ["Cardio", "Strength Training", "Flexibility", "HIIT", "Yoga", "Other"]
            )
            duration = st.number_input("Duration (minutes)", min_value=1, value=30)
            calories_burned = st.number_input("Calories Burned", min_value=0, value=200)
            notes = st.text_area("Workout Notes")
            
            submitted = st.form_submit_button("Log Workout")
            
            if submitted:
                workout_data = {
                    "workoutType": workout_type,
                    "duration": duration,
                    "caloriesBurned": calories_burned,
                    "notes": notes
                }
                
                result = make_api_request("/workouts", "POST", workout_data)
                if result:
                    st.success("Workout logged successfully!")
                    st.rerun()
    
    # Display workout history
    workouts = make_api_request("/workouts?limit=20")
    
    if workouts:
        df = pd.DataFrame(workouts)
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        # Workout summary
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_workouts = len(df)
            st.metric("Total Workouts", total_workouts)
        
        with col2:
            total_duration = df['duration'].sum()
            st.metric("Total Duration", f"{total_duration} min")
        
        with col3:
            total_calories = df['caloriesBurned'].sum()
            st.metric("Total Calories", f"{total_calories}")
        
        # Workout type distribution
        st.subheader("Workout Type Distribution")
        workout_counts = df['workoutType'].value_counts()
        fig = px.pie(values=workout_counts.values, names=workout_counts.index, 
                     title="Workout Types")
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent workouts table
        st.subheader("Recent Workouts")
        st.dataframe(
            df[['created_at', 'workoutType', 'duration', 'caloriesBurned', 'notes']].head(10),
            use_container_width=True
        )
    else:
        st.info("No workout sessions found. Log your first workout above!")

def show_nutrition_log():
    st.header("🥗 Nutrition Log")
    
    # Add new nutrition entry
    with st.expander("Log Nutrition Entry", expanded=False):
        with st.form("nutrition_form"):
            meal_type = st.selectbox(
                "Meal Type",
                ["Breakfast", "Lunch", "Dinner", "Snack", "Other"]
            )
            food_items = st.text_area("Food Items")
            calories = st.number_input("Calories", min_value=0, value=300)
            protein = st.number_input("Protein (g)", min_value=0.0, value=20.0, step=0.1)
            carbs = st.number_input("Carbs (g)", min_value=0.0, value=30.0, step=0.1)
            fats = st.number_input("Fats (g)", min_value=0.0, value=10.0, step=0.1)
            notes = st.text_area("Notes")
            
            submitted = st.form_submit_button("Log Nutrition Entry")
            
            if submitted:
                nutrition_data = {
                    "mealType": meal_type,
                    "foodItems": food_items,
                    "calories": calories,
                    "protein": protein,
                    "carbs": carbs,
                    "fats": fats,
                    "notes": notes
                }
                
                result = make_api_request("/nutrition", "POST", nutrition_data)
                if result:
                    st.success("Nutrition entry logged successfully!")
                    st.rerun()
    
    # Display nutrition history
    nutrition_logs = make_api_request("/nutrition?limit=20")
    
    if nutrition_logs:
        df = pd.DataFrame(nutrition_logs)
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        # Nutrition summary
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_entries = len(df)
            st.metric("Total Entries", total_entries)
        
        with col2:
            avg_calories = df['calories'].mean()
            st.metric("Avg Calories", f"{avg_calories:.0f}")
        
        with col3:
            total_protein = df['protein'].sum()
            st.metric("Total Protein", f"{total_protein:.1f}g")
        
        with col4:
            total_carbs = df['carbs'].sum()
            st.metric("Total Carbs", f"{total_carbs:.1f}g")
        
        # Macro distribution
        st.subheader("Macro Distribution")
        fig = go.Figure(data=[
            go.Bar(name='Protein', x=df['created_at'], y=df['protein']),
            go.Bar(name='Carbs', x=df['created_at'], y=df['carbs']),
            go.Bar(name='Fats', x=df['created_at'], y=df['fats'])
        ])
        fig.update_layout(barmode='stack', title="Daily Macro Intake")
        st.plotly_chart(fig, use_container_width=True)
        
        # Recent entries table
        st.subheader("Recent Nutrition Entries")
        st.dataframe(
            df[['created_at', 'mealType', 'foodItems', 'calories', 'protein', 'carbs', 'fats']].head(10),
            use_container_width=True
        )
    else:
        st.info("No nutrition entries found. Log your first entry above!")

def show_ai_insights():
    st.header("🤖 AI Insights")
    
    # Get AI insights
    insights = make_api_request("/insights")
    
    if insights:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.subheader("Today's AI Insights")
        st.write(insights.get('insights', 'No insights available'))
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Additional insights sections
        if 'recommendations' in insights:
            st.subheader("Recommendations")
            for rec in insights['recommendations']:
                st.write(f"💡 {rec}")
        
        if 'motivation' in insights:
            st.subheader("Motivation")
            st.write(f"💪 {insights['motivation']}")
    else:
        st.info("No AI insights available. Complete some tasks to generate insights!")
    
    # Manual insight generation
    if st.button("Generate New Insights"):
        with st.spinner("Generating insights..."):
            insights = make_api_request("/insights")
            if insights:
                st.success("New insights generated!")
                st.rerun()

if __name__ == "__main__":
    main() 