import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import jwt_decode from "jwt-decode";

const Home = () => {
  const [username, setUsername] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (token) {
      try {
        // Decode the JWT token
        const decodedToken = jwt_decode(token);

        // Log the decoded token to check its content
        console.log(decodedToken);

        // Check if 'username' exists in the decoded token
        if (decodedToken && decodedToken.username) {
          setUsername(decodedToken.username);
        } else {
          console.error("Username not found in token");
        }
      } catch (error) {
        console.error("Error decoding token:", error);
      }
    }
  }, []);

  const handleLogout = () => {
    // Remove token from localStorage to log out
    localStorage.removeItem("token");

    // Redirect the user to the login page
    navigate("/login");
  };

  return (
    <div className="home-container">
      <div className="home-greeting-container">
        <h1 className="home-greeting">Welcome, {username || "Guest"}</h1>
      </div>
      <div className="home-content">
        <p>Explore your dashboard, manage your profile, and more!</p>
        <button className="btn-logout" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </div>
  );
};

export default Home;
