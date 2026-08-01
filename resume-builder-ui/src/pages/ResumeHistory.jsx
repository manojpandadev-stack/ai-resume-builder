import { useEffect, useState } from "react";
import { getResumes } from "../services/resumeService";

function ResumeHistory() {
  const [resumes, setResumes] = useState([]);

  useEffect(() => {
    loadResumes();
  }, []);

  const loadResumes = async () => {
    try {
      const response = await getResumes();

      if (response.data.content) {
        setResumes(response.data.content);
      } else {
        setResumes(response.data);
      }
    } catch (error) {
      console.error(error);
      alert("Failed to load resumes");
    }
  };

  return (
    <div className="container mt-5">
      <h2>Saved Resumes</h2>

      {resumes.length === 0 ? (
        <p>No resumes found.</p>
      ) : (
        resumes.map((resume) => (
          <div key={resume.id} className="card p-3 mb-3">
            <h4>{resume.name}</h4>
            <p><b>Email:</b> {resume.email}</p>
            <p><b>Projects:</b> {resume.projects}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default ResumeHistory;