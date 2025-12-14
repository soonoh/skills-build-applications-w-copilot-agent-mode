import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_CODESPACE_NAME
      ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`
      : 'http://localhost:8000/api/teams/';
    
    console.log('Fetching from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Teams data:', data);
        const teamsArray = data.results || data;
        setTeams(teamsArray);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="text-center mt-4">Loading teams...</div>;
  }

  return (
    <div className="container mt-4">
      <h2>Teams</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {teams.map(team => (
            <tr key={team.id}>
              <td>{team.name}</td>
              <td>{team.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Teams;
