import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Register() {
  const navigate = useNavigate();

  const [user, setUser] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value,
    });
  };

  const handleRegister = async () => {
    if (!user.name || !user.email || !user.password) {
      alert("Please fill all fields");
      return;
    }

    setLoading(true);

    try {
      const response = await api.post("/auth/register", user);

      alert(response.data.message || "Registration Successful!");

      setUser({
        name: "",
        email: "",
        password: "",
      });

      navigate("/login");
    } catch (error) {
      console.error(error);

      alert(
        error.response?.data?.message ||
        error.response?.data?.error ||
        "Registration Failed"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <div
        className="card shadow p-4 mx-auto"
        style={{ maxWidth: "500px" }}
      >
        <h2 className="text-center mb-4">Register</h2>

        <input
          type="text"
          name="name"
          className="form-control mb-3"
          placeholder="Enter Name"
          value={user.name}
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          className="form-control mb-3"
          placeholder="Enter Email"
          value={user.email}
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          className="form-control mb-3"
          placeholder="Enter Password"
          value={user.password}
          onChange={handleChange}
        />

        <button
          className="btn btn-primary w-100"
          onClick={handleRegister}
          disabled={loading}
        >
          {loading ? "Registering..." : "Register"}
        </button>

        <p className="text-center mt-3">
          Already have an account?
          <button
            className="btn btn-link"
            onClick={() => navigate("/login")}
          >
            Login
          </button>
        </p>
      </div>
    </div>
  );
}

export default Register;