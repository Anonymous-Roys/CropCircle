import React from 'react';
import { useState, useEffect } from 'react';
import '@fortawesome/fontawesome-free/css/all.min.css';
import { Link } from 'react-router-dom';
import'../../styles/Farmer/Farmer.css'
import leafImage from '../../assets/images/leaf.png';

const FarmerLayout = ({ children }) => {
    const [isCollapsed, setIsCollapsed] = useState(false);


  useEffect(() => {
    setTimeout(() => document.body.classList.add('sidebar-visible'), 50);
  }, []);

  useEffect(() => {
    setTimeout(() => document.body.classList.add('content-visible'), 100);
  }, [children]);
  
  

  
  const toggleSidebar = () => {
    setIsCollapsed(!isCollapsed);
  };


  return (
    <div className={`layout ${isCollapsed ? 'collapsed' : ''}`}>
      <aside className="sidebar">
        <div className="sidebar-header">
          <div className="logo-icon">
          <img src={leafImage}  style={{ width: '35px', height: '40px' }} />

          </div>
          <button className="collapse-btn" onClick={toggleSidebar}>
            <i className="fas fa-chevron-left"></i>
            
          </button>
        </div>
        
        <nav className="menu">
          <ul>
          <li className="menu-item">
            <Link to="/farmer/overview">
                <i className="fas fa-chart-pie"></i>
                <span id='link'>Overview</span>
              </Link>
            </li>
            <li className="menu-item">
            <Link to="/farmer/product">
                <i className="fas fa-box"></i>
                <span id='link'>Products</span>
              </Link>
            </li>
            <li className="menu-item">
            <Link to="/farmer/orders">
                <i className="fas fa-shopping-cart"></i>
                <span id='link'>Orders</span>
              </Link>
              </li>
          </ul>
        </nav>

        <div className="sidebar-footer">
          <ul>
            <li className="menu-item">
              <i className="fas fa-cog"></i>
              <span>Settings</span>
            </li>
            <li className="menu-item">
              <i className="fas fa-sign-out-alt"></i>
              <span>Log Out</span>
            </li>
          </ul>
        </div>
      </aside>

      <main className="main-content">
        <header className="header">
          <div className="search-bar">
            <input type="text" placeholder="Search for product, customer, etc..." />
            <i className="fas fa-search search-icon"></i>
          </div>
          <div className="user-info">
            <div className='not-icon'>
                <i class="fa-regular fa-bell"></i>
            </div>
         
            <img src="https://placehold.co/40x40" alt="User profile" className="user-avatar" />
            <div className="user-details">
              <p className="user-name">Evelyn</p>
              <p className="user-role">Farmer</p>
            </div>
          </div>
        </header>

        <section className="products-section">
        {children}
        </section>

      </main>
    </div>
  );
}

export default FarmerLayout;
