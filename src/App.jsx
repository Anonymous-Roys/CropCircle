import React from 'react';
import './App.css';
import Overview from "./pages/FarmerDashboard";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  
  return (
    <>
<div>
    <Router>
      <Routes>
        <Route path='/' element={<Overview />} />
      </Routes>
    </Router>

        
      </div>
      
     
    
    </>
  )
}

export default App;