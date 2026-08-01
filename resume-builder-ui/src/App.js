import { Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import ResumeBuilder from "./components/ResumeBuilder";
import ProtectedRoute from "./components/ProtectedRoute";
import MyResumes from "./pages/MyResumes";
import ResumeHistory from "./pages/ResumeHistory";
import ResumeDetails from "./pages/ResumeDetails";
import EditResume from "./pages/EditResume";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <Routes>

      {/* Public Routes */}
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      {/* Dashboard */}
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      {/* Resume Builder */}
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <ResumeBuilder />
          </ProtectedRoute>
        }
      />

      {/* Resume History */}
      <Route
        path="/history"
        element={
          <ProtectedRoute>
            <ResumeHistory />
          </ProtectedRoute>
        }
      />

      {/* My Resumes */}
      <Route
        path="/resumes"
        element={
          <ProtectedRoute>
            <MyResumes />
          </ProtectedRoute>
        }
      />

      {/* View Resume Details */}
      <Route
        path="/resumes/:id"
        element={
          <ProtectedRoute>
            <ResumeDetails />
          </ProtectedRoute>
        }
      />

      {/* Edit Resume */}
      <Route
        path="/resumes/edit/:id"
        element={
          <ProtectedRoute>
            <EditResume />
          </ProtectedRoute>
        }
      />

      {/* Redirect Unknown Routes */}
      <Route path="*" element={<Navigate to="/" />} />

    </Routes>
  );
}

export default App;