import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../services/api";

function EditResume() {
  const { id } = useParams();
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

  useEffect(() => {
    loadResume();
    // eslint-disable-next-line react-hooks/exhaustive-deps
}, []);

  const loadResume = async () => {
    try {
      const response = await api.get(`/api/resumes/${id}`);
      setForm(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to load resume");
    }
  };

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const updateResume = async () => {
    try {
      await api.put(`/api/resumes/${id}`, form);
      alert("Resume updated successfully!");
      navigate("/resumes");
    } catch (error) {
      console.error(error);
      alert("Update failed");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card p-4 shadow">

        <h2>Edit Resume</h2>

        <input
          className="form-control mb-3"
          name="name"
          value={form.name}
          onChange={handleChange}
          placeholder="Name"
        />

        <input
          className="form-control mb-3"
          name="email"
          value={form.email}
          onChange={handleChange}
          placeholder="Email"
        />

        <input
          className="form-control mb-3"
          name="phone"
          value={form.phone}
          onChange={handleChange}
          placeholder="Phone"
        />

        <textarea
          className="form-control mb-3"
          name="education"
          value={form.education}
          onChange={handleChange}
          placeholder="Education"
        />

        <textarea
          className="form-control mb-3"
          name="skills"
          value={form.skills}
          onChange={handleChange}
          placeholder="Skills"
        />

        <textarea
          className="form-control mb-3"
          name="experience"
          value={form.experience}
          onChange={handleChange}
          placeholder="Experience"
        />

        <textarea
          className="form-control mb-3"
          name="projects"
          value={form.projects}
          onChange={handleChange}
          placeholder="Projects"
        />

        <button
          className="btn btn-success"
          onClick={updateResume}
        >
          Update Resume
        </button>

      </div>
    </div>
  );
}

export default EditResume;