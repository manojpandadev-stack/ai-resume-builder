import { useCallback, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function MyResumes() {
  const navigate = useNavigate();

  const [resumes, setResumes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [sortOrder, setSortOrder] = useState("desc");
  const [page, setPage] = useState(0);
  const [totalPages, setTotalPages] = useState(0);

  const fetchResumes = useCallback(async () => {
    setLoading(true);

    try {
      const response = await api.get(`/api/resumes?page=${page}&size=5`);

      if (response.data.content) {
        setResumes(response.data.content);
        setTotalPages(response.data.totalPages);
      } else {
        setResumes(response.data);
        setTotalPages(1);
      }
    } catch (error) {
      console.error(error);
      alert("Failed to load resumes");
    } finally {
      setLoading(false);
    }
  }, [page]);

  useEffect(() => {
    fetchResumes();
  }, [fetchResumes]);

  const deleteResume = async (id) => {
    if (!window.confirm("Are you sure you want to delete this resume?")) {
      return;
    }

    try {
      await api.delete(`/api/resumes/${id}`);
      alert("Resume deleted successfully!");
      fetchResumes();
    } catch (error) {
      console.error(error);
      alert("Delete failed");
    }
  };

  const filteredResumes = resumes
    .filter((resume) =>
      (resume.name || "")
        .toLowerCase()
        .includes(search.toLowerCase())
    )
    .sort((a, b) =>
      sortOrder === "desc"
        ? b.id - a.id
        : a.id - b.id
    );

  return (
    <div className="container mt-5">

      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2 className="text-primary">
          📄 My Saved AI Resumes
        </h2>

        <button
          className="btn btn-primary"
          onClick={() => navigate("/")}
        >
          ← Resume Builder
        </button>
      </div>


      <div className="mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Search by name..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>


      <div className="mb-3">
        <select
          className="form-select"
          value={sortOrder}
          onChange={(e) => setSortOrder(e.target.value)}
        >
          <option value="desc">Newest First</option>
          <option value="asc">Oldest First</option>
        </select>
      </div>

      <div className="card shadow">
        <div className="card-body">

          <table className="table table-striped table-hover align-middle">

            <thead className="table-dark">
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th width="250">Actions</th>
              </tr>
            </thead>

            <tbody>

              {loading ? (
                <tr>
                  <td colSpan="5" className="text-center">
                    Loading resumes...
                  </td>
                </tr>
              ) : filteredResumes.length === 0 ? (
                <tr>
                  <td colSpan="5" className="text-center text-danger">
                    No resumes found.
                  </td>
                </tr>
              ) : (
                filteredResumes.map((resume) => (
                  <tr key={resume.id}>
                    <td>{resume.id}</td>
                    <td>{resume.name}</td>
                    <td>{resume.email}</td>
                    <td>{resume.phone}</td>

                    <td>

                      <button
                        className="btn btn-success btn-sm me-2"
                        onClick={() => navigate(`/resumes/${resume.id}`)}
                      >
                        View
                      </button>

                      <button
                        className="btn btn-warning btn-sm me-2"
                        onClick={() => navigate(`/resumes/edit/${resume.id}`)}
                      >
                        Edit
                      </button>

                      <button
                        className="btn btn-danger btn-sm"
                        onClick={() => deleteResume(resume.id)}
                      >
                        Delete
                      </button>

                    </td>
                  </tr>
                ))
              )}

            </tbody>

          </table>
          <div className="d-flex justify-content-between align-items-center mt-3">

            <button
              className="btn btn-secondary"
              disabled={page === 0}
              onClick={() => setPage(page - 1)}
            >
              ← Previous
            </button>

            <span className="fw-bold">
              Page {page + 1} of {totalPages}
            </span>

            <button
              className="btn btn-secondary"
              disabled={page + 1 >= totalPages}
              onClick={() => setPage(page + 1)}
            >
              Next →
            </button>
          </div>
        </div>
      </div>

    </div>
  );
}

export default MyResumes;