import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [projectName, setProjectName] = useState('');
  const [deadline, setDeadline] = useState('');
  const [numMembers, setNumMembers] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Prepare project data
    const projectData = {
      name: projectName,
      deadline: deadline,
      num_members: numMembers
    };

    try {
      // Send POST request to Flask backend
      const response = await fetch('http://127.0.0.1:5000/create_project', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(projectData) // Sending data as JSON
      });

      // Handle response
      const result = await response.json();
      setMessage(result.message); // Set the message to be displayed on success
    } catch (error) {
      console.error('Error:', error);
      setMessage('Error creating project!');
    }
  }

  return (
    <div>
      <h1>Group Project Manager</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Project Name:
          <input
            type="text"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Deadline:
          <input
            type="date"
            value={deadline}
            onChange={(e) => setDeadline(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Number of Members:
          <input
            type="number"
            value={numMembers}
            onChange={(e) => setNumMembers(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit">Create Project</button>
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}

export default App;
