import React from 'react';
import '../../styles/Sales.css';
import testSvg from '../../assets/chart-line.svg';
import truck from '../../assets/truck-fast.svg';
import cart from '../../assets/cart-shopping.svg';
import list from '../../assets/list-check.svg';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons';

const SalesAnalytics = ({ products }) => {
  // Calculate total sales
  const totalSales = products.reduce((sum, product) => sum + product.quantity * product.price, 0);

  // Identify the top-selling product
  const topSellingProduct = products.length
    ? products.reduce((topProduct, product) =>
        product.quantity * product.price > topProduct.quantity * topProduct.price ? product : topProduct
      )
    : null;

  // Filter products to count only completed deliveries
  const completedDeliveries = products.filter(product => product.description === 'Completed').length;

  return (
    <>
      <h2>Sales Analytics</h2>
      <div className="overview">
        <div className="saleAnalysis">
          <div className="totalSale">
            <p><strong>¢{totalSales.toFixed(2)}</strong></p>
            <h3>Sales <img src={testSvg} alt="Sales Chart Icon" /></h3>
          </div>
          <div className="totalSale">
            <p><strong>{products.length}</strong></p>
            <h3>Orders <img src={truck} alt="Truck Icon" /></h3>
          </div>
          <div className="topSellingProduct">
            <p><strong>{topSellingProduct?.name || "No Sales Yet"}</strong></p>
            <h3>Top Selling Product <img src={cart} alt="Shopping Cart Icon" /></h3>
          </div>
          <div className="totalSale">
            <p><strong>{completedDeliveries}</strong></p>
            <h3>Deliveries Made <img src={list} alt="Checklist Icon" /></h3>
          </div>
        </div>

        <h1>Recent Orders</h1>
        <table>
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Price</th>
              <th>Payment Mode</th>
              <th>Transaction Status</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product, index) => (
              <tr key={index}>
                <td>{product.name}</td>
                <td>{product.quantity}</td>
                <td>¢{product.price}</td>
                <td>{product.paymentMode}</td>
                <td>{product.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
        
        <a href="#" className="link">More detail <FontAwesomeIcon icon={faArrowRight} /></a>
      </div>
    </>
  );
};

export default SalesAnalytics;
