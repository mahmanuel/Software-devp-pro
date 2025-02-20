import React, { useState, useEffect } from "react";
import Login from "./components/Login";
import { getUserProfile, logout } from "./services/auth";
import AITSApp from "./components/AITSApp";

import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/Login";
import { getUserProfile, logout } from "./services/auth";
import StudentDashboard from "./components/StudentDashboard";
import MentorDashboard from "./components/MentorDashboard";
import AdminDashboard from "./components/AdminDashboard";

const App = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    async function fetchUser() {
      const profile = await getUserProfile();
      if (profile) setUser(profile);
    }
    fetchUser();
  }, []);

  const handleLogout = async () => {
    await logout();
    setUser(null);
  };

  return (
    <div>
      {user ? (
        <>
          <button onClick={handleLogout}>Logout</button>
          <AITSApp user={user} />
        </>
      ) : (
        <Login onLogin={setUser} />
      )}
    </div>
  );
};

export default App;


const App = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    async function fetchUser() {
      const profile = await getUserProfile();
      if (profile) setUser(profile);
    }
    fetchUser();
  }, []);

  const handleLogout = async () => {
    await logout();
    setUser(null);
  };

  return (
    <Router>
      <div>
        {user ? (
          <>
            <button onClick={handleLogout}>Logout</button>
            <Routes>
              <Route path="/" element={<Navigate to={`/${user.role}`} />} />
              <Route path="/student" element={user.role === "student" ? <StudentDashboard /> : <Navigate to="/" />} />
              <Route path="/mentor" element={user.role === "mentor" ? <MentorDashboard /> : <Navigate to="/" />} />
              <Route path="/admin" element={user.role === "admin" ? <AdminDashboard /> : <Navigate to="/" />} />
            </Routes>
          </>
        ) : (
          <Routes>
            <Route path="/" element={<Login onLogin={setUser} />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        )}
      </div>
    </Router>
  );
};

export default App;
