import React, {useState, useEffect} from 'react';
import axios from 'axios';

const IssuesList = () => {
    const[issues, setIssues] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    //fetch issues from Django API
    useEffect(() => {
        const fetchIssues = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/issues/');
                setIssues(response.data);
                setLoading(false);
            }   catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };
        fetchIssues();
    }, []);
    //Display loading state
    if (loading) {
        return <div>Loading...</div>;
    }
    //Render the list of issues
    return (
        <div>
          <h1>Issues List</h1>
          <ul>
            {issues.map((issue) => (
              <li key={issue.id}>
                <h3>{issue.title}</h3>
                <p>{issue.description}</p>
              </li>
            ))}
          </ul>
        </div>
      );
    
};

export default IssuesList;
