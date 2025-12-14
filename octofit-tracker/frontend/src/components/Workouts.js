import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_CODESPACE_NAME
      ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`
      : 'http://localhost:8000/api/workouts/';
    
    console.log('Fetching from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Workouts data:', data);
        const workoutsArray = data.results || data;
        setWorkouts(workoutsArray);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="text-center mt-4">Loading workouts...</div>;
  }

  return (
    <div className="container mt-4">
      <h2>Workouts</h2>
      <div className="row">
        {workouts.map(workout => (
          <div key={workout.id} className="col-md-6 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{workout.name}</h5>
                <p className="card-text">{workout.description}</p>
                <p className="card-text">
                  <strong>Difficulty:</strong> <span className="badge bg-primary">{workout.difficulty}</span>
                </p>
                <p className="card-text">
                  <strong>Target Muscles:</strong> {workout.target_muscles && workout.target_muscles.join(', ')}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;
