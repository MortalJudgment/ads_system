import React, { useState, useContext } from 'react';
import { UserContext } from '../../contexts/UserContext';
import InterestSelector from '../InterestSelector/InterestSelector';
import { validateEmail, validateUsername} from '../../utils/validators';
import './Login.css';

function Login() {
  const { setUser } = useContext(UserContext);
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [email, setEmail] = useState('');
  const [interests, setInterests] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateUsername(name) && age && validateEmail(email) && interests.length >= 2) {
      setUser({ name, age, email, interests });
    } else {
      alert('Please fill all fields correctly and select at least 2 interests.');
    }
  };

  return (
    <div className="login-container">
      <form onSubmit={handleSubmit} className="login-form">
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <InterestSelector interests={interests} setInterests={setInterests} />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;