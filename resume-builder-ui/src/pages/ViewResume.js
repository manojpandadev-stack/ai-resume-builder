import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../services/api";

function ViewResume() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [resume, setResume] = useState(null);

  useEffect(() => {
    loadResume();
  }, []);

  const loadResume = async () => {
    try {
      const response = await api.get(`/api/resumes/${id}`);
      setResume(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to load resume");
    }
  };

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

      <div className="card shadow p-4">
        <h2>{resume.name}</h2>

        <p><b>Email:</b> {resume.email}</p>
        <p><b>Phone:</b> {resume.phone}</p>
        <p><b>Education:</b> {resume.education}</p>
        <p><b>Skills:</b> {resume.skills}</p>
        <p><b>Experience:</b> {resume.experience}</p>
        <p><b>Projects:</b> {resume.projects}</p>

        <hr />

        <h4>Generated Resume</h4>

        <pre style={{ whiteSpace: "pre-wrap" }}>
          {resume.generatedResume}
        </pre>
      </div>

    </div>
  );
}

export default ViewResume;