// Home.tsx
import React, { useState } from 'react';
import './Home.css';

export default function Home() {
  const [selectedOption, setSelectedOption] = useState('');

  const handleOrder = () => {
    if (selectedOption) {
      alert(`Order placed for: ${selectedOption}`);
    } else {
      alert('Please select a website option.');
    }
  };

  return (
    <div className="home-container">
      <h1 className="home-title">Welcome to Our Service</h1>

      <div className="dropdown-container">
        <label htmlFor="website-select">Choose a website</label>
        <select
          id="website-select"
          value={selectedOption}
          onChange={(e) => setSelectedOption(e.target.value)}
        >
          <option value="">-- Select website --</option>
          <option value="Portfolio">Portfolio</option>
          <option value="E-commerce">E-commerce</option>
          <option value="Blog">Blog</option>
          <option value="Landing Page">Landing Page</option>
        </select>
      </div>

      <button className="order-button" onClick={handleOrder}>
        Order
      </button>
    </div>
  );
}