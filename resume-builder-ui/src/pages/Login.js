import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Login() {

  const navigate = useNavigate();

  const [user, setUser] = useState({
    email: "",
    password: ""
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value
    });
  };

  const handleLogin = async () => {

    if (!user.email || !user.password) {
      alert("Please enter email and password");
      return;
    }

    setLoading(true);

    try {

      const response = await api.post("/auth/login", user);

      localStorage.setItem("token", response.data.token);

      alert("Login Successful!");

      navigate("/");

    } catch (error) {

      console.error(error);

      alert(
        error.response?.data?.message ||
        "Invalid Email or Password"
      );

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="container mt-5">

      <div
        className="card shadow-lg p-4 mx-auto"
        style={{ maxWidth: "500px" }}
      >

        <h2 className="text-center text-primary mb-4">
          Login
        </h2>

        <input
          className="form-control mb-3"
          type="email"
          name="email"
          placeholder="Enter Email"
          value={user.email}
          onChange={handleChange}
        />

        <input
          className="form-control mb-3"
          type="password"
          name="password"
          placeholder="Enter Password"
          value={user.password}
          onChange={handleChange}
        />

        <button
          className="btn btn-success w-100"
          onClick={handleLogin}
          disabled={loading}
        >
          {loading ? "Logging in..." : "Login"}
        </button>

        <p className="text-center mt-3">
          Don't have an account?
          <button
            className="btn btn-link"
            onClick={() => navigate("/register")}
          >
            Register
          </button>
        </p>

      </div>

    </div>
  );
}

export default Login;