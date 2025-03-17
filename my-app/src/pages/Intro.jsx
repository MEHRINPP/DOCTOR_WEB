import { useNavigate } from "react-router-dom";

const Intro = () => {
  const navigate = useNavigate();
  return (
    <div className="intro-container">
      <div className="intro-content">
        <h1>Welcome to Our App</h1>
        <button className="btn-signup" onClick={() => navigate('/signup')}>
          Sign Up
        </button>
        <button className="btn-login" onClick={() => navigate('/login')}>
          Login
        </button>
      </div>
    </div>
  );
};

export default Intro;
