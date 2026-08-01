import api from "../services/api";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function ResumeBuilder()  {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    education: "",
    skills: "",
    experience: "",
    projects: "",
  });
  const clearForm = () => {
  setForm({
    name: "",
    email: "",
    phone: "",
    education: "",
    skills: "",
    experience: "",
    projects: "",
  });

  setResume("");
  setAnalysis("");
  setCoverLetter("");
};

 const [resume, setResume] = useState("");
const [analysis, setAnalysis] = useState("");
const [coverLetter, setCoverLetter] = useState("");
const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const generateResume = async () => {
    setLoading(true);

    try {
    const response = await api.post(
  "http://localhost:8080/api/ai/generate",
  form
     );

    setResume(response.data.content);

  } catch (error) {
    console.error(error);
    alert("Error generating resume");
  } finally {
    setLoading(false);
  }
  };

      const analyzeResume = async () => {
    setLoading(true);
    try {
      const response = await api.post(
  "http://localhost:8080/api/ai/analyze",
  {
    content: resume
  }
   );

setAnalysis(response.data.content);
    } catch (error) {
      console.error(error);
      alert("Error analyzing resume");
    }finally{
      setLoading(false);
    }
  };

   const generateCoverLetter = async () => {
  try {
    const response = await api.post(
      "http://localhost:8080/api/ai/cover-letter",
      form
    );

    setCoverLetter(response.data.content);

  } catch (error) {
    console.error(error);
    alert("Error generating cover letter");
  }
};

const saveResume = async () => {

  if (!resume) {
    alert("Please generate a resume first.");
    return;
  }

  try {

    await api.post("/api/resumes", {
      name: form.name,
      email: form.email,
      phone: form.phone,
      education: form.education,
      skills: form.skills,
      experience: form.experience,
      projects: form.projects,
      generatedResume: resume
    });

    alert("Resume saved successfully!");

  } catch (error) {
    console.error(error);
    alert(error.response?.data?.message || "Failed to save resume");
  }
};

      const downloadPdf = async () => {
     try {
      
      const response = await api.post(
  "http://localhost:8080/pdf/download",
  {
    content: resume
  },
  {
    responseType: "blob"
  }
    );

      const url = window.URL.createObjectURL(response.data);
      const link = document.createElement("a");

      link.href = url;
      link.setAttribute("download", "resume.pdf");

      document.body.appendChild(link);
      link.click();
      link.remove();

      window.URL.revokeObjectURL(url);
    } catch (error) {
  console.log(error);
  console.log(error.response);

  alert(error.message);
}
};

 return (
  <div className="container py-5">
    <div className="card shadow-lg p-4">

      <div className="d-flex justify-content-end mb-3">
        <button
          className="btn btn-danger"
          onClick={() => {
            localStorage.removeItem("token");
            window.location.href = "/login";
          }}
        >
          <i className="bi bi-box-arrow-right me-2"></i>
          Logout
        </button>
      </div>

      <h1 className="text-center text-primary mb-2">
        🤖 AI Resume Builder
      </h1>

      <p className="text-center text-secondary mb-4">
        Generate AI-powered resumes, ATS reports, cover letters and PDF downloads instantly.
      </p>
      <div className="row">

        <div className="col-md-6 mb-3">
          <label className="form-label">Name</label>
          <input
            type="text"
            name="name"
            className="form-control"
            placeholder="Enter Name"
            onChange={handleChange}
          />
        </div>

        <div className="col-md-6 mb-3">
          <label className="form-label">Email</label>
          <input
           type="email"
            name="email"
            className="form-control"
            placeholder="Enter Email"
           value={form.email}
           onChange={handleChange}

/>
        </div>

        <div className="col-md-6 mb-3">
          <label className="form-label">Phone</label>
          <input
            type="text"
            name="phone"
            className="form-control"
            placeholder="Enter Phone"
            onChange={handleChange}
          />
        </div>

        <div className="col-12 mb-3">
          <label className="form-label">Education</label>
          <textarea
            name="education"
            className="form-control"
            rows="3"
            onChange={handleChange}
          />
        </div>

        <div className="col-12 mb-3">
          <label className="form-label">Skills</label>
          <textarea
            name="skills"
            className="form-control"
            rows="3"
            onChange={handleChange}
          />
        </div>

        <div className="col-12 mb-3">
          <label className="form-label">Experience</label>
          <textarea
            name="experience"
            className="form-control"
            rows="3"
            onChange={handleChange}
          />
        </div>

        <div className="col-12 mb-4">
          <label className="form-label">Projects</label>
          <textarea
            name="projects"
            className="form-control"
            rows="3"
            onChange={handleChange}
          />
        </div>

      </div>

      <div className="d-flex flex-wrap gap-2 mb-4">

 {/* Navigation Buttons */}
<div className="d-flex justify-content-between align-items-center mb-4">

  <div className="d-flex gap-2">

    <button
      className="btn btn-dark"
      onClick={() => navigate("/dashboard")}
    >
      Dashboard
    </button>

    <button
      className="btn btn-success"
      onClick={() => navigate("/resumes")}
    >
      My Resumes
    </button>

    <button
      className="btn btn-info"
      onClick={() => navigate("/history")}
    >
      History
    </button>

  </div>

  <button
    className="btn btn-danger"
    onClick={() => {
      localStorage.removeItem("token");
      window.location.href = "/login";
    }}
  >
    Logout
  </button>

</div>

<hr />

{/* Resume Action Buttons */}
<div className="d-flex flex-wrap gap-2 mb-4">

  <button
    className="btn btn-primary"
    onClick={generateResume}
    disabled={loading}
  >
    <i className="bi bi-file-earmark-text me-2"></i>
    {loading ? "Generating..." : "Generate Resume"}
  </button>

  <button
    className="btn btn-success"
    onClick={analyzeResume}
    disabled={loading}
  >
    <i className="bi bi-bar-chart-line me-2"></i>
    {loading ? "Analyzing..." : "Analyze Resume"}
  </button>

  <button
    className="btn btn-warning"
    onClick={generateCoverLetter}
    disabled={loading}
  >
    <i className="bi bi-envelope-paper me-2"></i>
    {loading ? "Generating..." : "Cover Letter"}
  </button>

  <button
    className="btn btn-info"
    onClick={saveResume}
  >
    <i className="bi bi-save me-2"></i>
    Save Resume
  </button>

  <button
    className="btn btn-danger"
    onClick={downloadPdf}
    disabled={loading}
  >
    <i className="bi bi-download me-2"></i>
    Download PDF
  </button>

  <button
    className="btn btn-secondary"
    onClick={clearForm}
  >
    <i className="bi bi-arrow-clockwise me-2"></i>
    Clear
  </button>

</div>


      </div>

      <div className="card mb-3">
        <div className="card-header bg-primary text-white">
          Generated Resume
        </div>
        <div className="card-body">
          <div
  style={{
    whiteSpace: "pre-wrap",
    maxHeight: "400px",
    overflowY: "auto",
    padding: "15px",
    background: "#f8f9fa",
    borderRadius: "10px",
    border: "1px solid #dee2e6",
  }}
>
  {resume}
            </div>
        </div>
      </div>

      <div className="card mb-3">
        <div className="card-header bg-success text-white">
          ATS Analysis
        </div>
        <div className="card-body">
          <div
  style={{
    whiteSpace: "pre-wrap",
    maxHeight: "300px",
    overflowY: "auto",
    padding: "15px",
    background: "#eef8ff",
    borderRadius: "10px",
    border: "1px solid #dee2e6",
  }}
>
  {analysis}
</div>
        </div>
      </div>

      <div className="card">
        <div className="card-header bg-warning">
          Cover Letter
        </div>
        <div className="card-body">
          <div
  style={{
    whiteSpace: "pre-wrap",
    maxHeight: "300px",
    overflowY: "auto",
    padding: "15px",
    background: "#fff8e6",
    borderRadius: "10px",
    border: "1px solid #dee2e6",
  }}
>
  {coverLetter}
</div>
        </div>
      </div>

    </div>

  </div>
);
}

export default ResumeBuilder;