import { useEffect, useState, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../services/api";

function ResumeDetails() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [resume, setResume] = useState(null);

  const loadResume = useCallback(async () => {
    try {
      const response = await api.get(`/api/resumes/${id}`);
      setResume(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to load resume");
    }
  }, [id]);

  useEffect(() => {
    loadResume();
  }, [loadResume]);

  if (!resume) {
    return <h3 className="text-center mt-5">Loading...</h3>;
  }

  return (
    <div className="container mt-5">
      <button
        className="btn btn-secondary mb-3"
        onClick={() => navigate("/resumes")}
      >
        ← Back
      </button>

      <div className="card p-4 shadow">
        <h2>{resume.name}</h2>

        <p><b>Email:</b> {resume.email}</p>
        <p><b>Phone:</b> {resume.phone}</p>
        <p><b>Education:</b> {resume.education}</p>
        <p><b>Skills:</b> {resume.skills}</p>
        <p><b>Experience:</b> {resume.experience}</p>
        <p><b>Projects:</b> {resume.projects}</p>

        <hr />

        <h3>Generated Resume</h3>

        <pre style={{ whiteSpace: "pre-wrap" }}>
          {resume.generatedResume}
        </pre>
      </div>
    </div>
  );
}

export default ResumeDetails;