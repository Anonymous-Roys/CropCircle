import React, { useState } from 'react';
import SalesAnalytics from '../components/Farmer/SalesAnalytics';

const Overview = () => {
  const [products] = useState([
    { name: 'Tomato', paymentMode: "Visa Card **** 4831", quantity: 100, price: 1.5, description: 'Completed' },
    { name: 'Orange', paymentMode: "Visa Card **** 4831", quantity: 150, price: 1.2, description: 'Completed' },
    { name: 'Banana', paymentMode: "Visa Card **** 4831", quantity: 120, price: 0.8, description: 'Pending' },
    { name: 'Mango', paymentMode: "Visa Card **** 4831", quantity: 80, price: 2.0, description: 'Cancelled' },
    { name: 'Grapes', paymentMode: "Visa Card **** 4831", quantity: 90, price: 2.5, description: 'Pending' }
  ]);

  return (
    <div>
      <SalesAnalytics products={products} />
    </div>
  );
};

export default Overview;
