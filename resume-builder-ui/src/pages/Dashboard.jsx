import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Dashboard() {
  const navigate = useNavigate();

  const [totalResumes, setTotalResumes] = useState(0);
  const [latestResume, setLatestResume] = useState(null);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const response = await api.get("/api/resumes?page=0&size=100");

      const data = response.data.content
        ? response.data.content
        : response.data;

      setTotalResumes(data.length);

      if (data.length > 0) {
        setLatestResume(data[data.length - 1]);
      }
    } catch (error) {
      console.error(error);
      alert("Failed to load dashboard");
    }
  };

  return (
    <div className="container mt-5">

      <h2 className="text-primary mb-4">
        📊 AI Resume Builder Dashboard
      </h2>

      <div className="row">

        <div className="col-md-4">
          <div className="card shadow text-center p-4">
            <h1>{totalResumes}</h1>
            <h5>Total Resumes</h5>
          </div>
        </div>

        <div className="col-md-8">
          <div className="card shadow p-4">

            <h4 className="mb-3">Latest Resume</h4>

            {latestResume ? (
              <>
                <p><strong>Name:</strong> {latestResume.name}</p>
                <p><strong>Email:</strong> {latestResume.email}</p>
                <p><strong>Phone:</strong> {latestResume.phone}</p>
              </>
            ) : (
              <p>No resumes available.</p>
            )}

          </div>
        </div>

      </div>

      <div className="d-flex flex-wrap gap-3 mt-4">

        <button
          className="btn btn-primary"
          onClick={() => navigate("/")}
        >
          📝 Resume Builder
        </button>

        <button
          className="btn btn-success"
          onClick={() => navigate("/resumes")}
        >
          📄 My Resumes
        </button>

        <button
          className="btn btn-info"
          onClick={() => navigate("/history")}
        >
          🕒 Resume History
        </button>

        <button
          className="btn btn-warning"
          onClick={loadDashboard}
        >
          🔄 Refresh
        </button>

        <button
          className="btn btn-danger"
          onClick={() => {
            localStorage.removeItem("token");
            window.location.href = "/login";
          }}
        >
          🚪 Logout
        </button>

      </div>

    </div>
  );
}

export default Dashboard;