import React from 'react';
import './Header.css'; // Make sure to create a corresponding CSS file for styling
import logo from './AJ_Logo.svg';

const Header: React.FC = () => {
  return (
    <header className="header">
      <div className="logo">
        {/* {<img src={logo} className="app-logo" alt="Alex Jeter Logo" />} */}
        <h1>Social Media Analytics Dashboard</h1>
      </div>
      {/* If you have navigation or user account components, they can be added here */}
    </header>
  );
};

export default Header;
