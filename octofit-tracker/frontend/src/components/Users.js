import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_CODESPACE_NAME
      ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`
      : 'http://localhost:8000/api/users/';
    
    console.log('Fetching from:', apiUrl);
    
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Users data:', data);
        const usersArray = data.results || data;
        setUsers(usersArray);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="text-center mt-4">Loading users...</div>;
  }

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Team ID</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td>{user.team_id || 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Users;
