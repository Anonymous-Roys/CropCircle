import React, { useState } from "react";
import { FaBell, FaUser, FaSearch } from "react-icons/fa";

const orders = [
  {
    customer: "John Doe",
    email: "john.doe@example.com",
    status: "Delivered",
    item: "Red Tomato",
    payment: "Card payment",
    price: "GH₵182.94",
    date: "Jan 17, 2022",
  },
  {
    customer: "Jane Smith",
    email: "jane.smith@example.com",
    status: "Delivered",
    item: "Pepper",
    payment: "Card payment",
    price: "GH₵99.00",
    date: "Jan 17, 2022",
  },
  {
    customer: "Michael Brown",
    email: "michael.brown@example.com",
    status: "Pending",
    item: "Cabbage",
    payment: "Cash on delivery",
    price: "GH₵50.00",
    date: "Jan 18, 2022",
  },
  {
    customer: "Emily Johnson",
    email: "emily.johnson@example.com",
    status: "Cancelled",
    item: "Onions",
    payment: "Card payment",
    price: "GH₵120.00",
    date: "Jan 19, 2022",
  },
];

export default function OrderTracking() {
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredStatus, setFilteredStatus] = useState("All");
  const [selectedOrder, setSelectedOrder] = useState(null);

  const getStatusColor = (status) => {
    switch (status) {
      case "Delivered":
        return "bg-green-200";
      case "Pending":
        return "bg-yellow-200";
      case "Cancelled":
        return "bg-red-200";
      default:
        return "bg-gray-200";
    }
  };

  const getDotColor = (status) => {
    switch (status) {
      case "Delivered":
        return "bg-green-600";
      case "Pending":
        return "bg-yellow-600";
      case "Cancelled":
        return "bg-red-600";
      default:
        return "bg-gray-600";
    }
  };

  const filteredOrders = orders.filter(
    (order) =>
      (order.status.toLowerCase().includes(searchTerm.toLowerCase()) ||
        order.item.toLowerCase().includes(searchTerm.toLowerCase()) ||
        order.payment.toLowerCase().includes(searchTerm.toLowerCase())) &&
      (filteredStatus === "All" || order.status === filteredStatus)
  );

  const closeModal = () => setSelectedOrder(null);

  return (
    <div className="bg-gray-100 min-h-screen p-2 py-2">
      <header className="flex justify-between items-center border rounded-lg bg-stone-200 p-1">
        <h1 className="text-3xl font-semibold text-green-700">CropCircle</h1>
        <div className="flex items-center gap-4">
          <div className="relative">
            <FaSearch className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500" />
            <input
              type="text"
              placeholder="Search for product, customer, etc..."
              className="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-green-500"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
          <button className="relative text-gray-600 hover:text-gray-800">
            <FaBell className="h-6 w-6 text-gray-500 hover:text-yellow-500" />
            <span className="absolute top-0 right-0 px-1 text-xs font-bold text-white bg-red-500 rounded-full">
              3
            </span>
          </button>
          <div className="flex items-center gap-2">
            <img
              src="https://randomuser.me/api/portraits/women/44.jpg"
              alt="User"
              className="h-10 w-10 rounded-full border-2 border-green-500"
            />
            <div>
              <p className="text-gray-700 font-medium">Sarah</p>
              <p className="text-gray-500 text-sm">Welcome back</p>
            </div>
          </div>
        </div>
      </header>

      <main className="mt-10">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-3xl font-semibold">Orders</h2>
          <select
            value={filteredStatus}
            onChange={(e) => setFilteredStatus(e.target.value)}
            className="border p-2 px-3 py-1 rounded-lg border-gray-300 text-gray-600"
          >
            <option value="All">All</option>
            <option value="Delivered">Delivered</option>
            <option value="Pending">Pending</option>
            <option value="Cancelled">Cancelled</option>
          </select>
        </div>

        <div className="bg-white rounded shadow-md overflow-hidden">
          {filteredOrders.map((order, index) => (
            <div
              key={index}
              className="flex items-center justify-between p-4 border-b border-gray-200 cursor-pointer"
              onClick={() => setSelectedOrder(order)}
            >
              <span
                className={`flex items-center ${getStatusColor(order.status)} px-3 py-1 rounded-full text-gray-700 font-medium text-xs`}
              >
                <span className={`w-3 h-2 rounded-full ${getDotColor(order.status)} mr-2`}></span>
                {order.status}
              </span>
              <div>
                <p className="text-gray-700 font-medium">{order.item}</p>
                <p className="text-gray-500 text-sm">{order.payment}</p>
              </div>
              <div className="text-right">
                <p className="text-gray-700 font-medium">{order.price}</p>
                <p className="text-gray-500 text-sm">{order.date}</p>
              </div>
            </div>
          ))}
        </div>
      </main>

      {selectedOrder && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div className="bg-white rounded-lg p-8 w-1/2 shadow-lg">
            <h2 className="text-3xl font-bold text-center mb-6">Order Detail</h2>
            <div className="space-y-6 shadow-lg hover:shadow-xl p-6 bg-white border border-gray-200 rounded-lg">
              <div className="flex justify-between">
                <span className="font-medium text-gray-700">Customer</span>
                <div className="text-right">
                  <p className="text-gray-900 font-medium">{selectedOrder.customer}</p>
                  <p className="text-sm text-gray-500">{selectedOrder.email}</p>
                </div>
              </div>
              <div className="flex justify-between">
                <span className="font-medium text-gray-700">Payment Method</span>
                <p className="text-gray-900 font-medium">{selectedOrder.payment}</p>
              </div>
              <div className="flex justify-between">
                <span className="font-medium text-gray-700">Date</span>
                <p className="text-gray-900 font-medium">{selectedOrder.date}</p>
              </div>
              <div className="flex justify-between">
                <span className="font-medium text-gray-700">Order Status</span>
                <span
                  className={`px-3 py-1 rounded-full text-sm font-medium ${
                    selectedOrder.status === "Delivered"
                      ? "bg-green-100 text-green-600"
                      : selectedOrder.status === "Pending"
                      ? "bg-yellow-100 text-yellow-600"
                      : "bg-red-100 text-red-600"
                  }`}
                >
                  {selectedOrder.status}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="font-medium text-gray-700">Total Price</span>
                <p className="text-gray-900 font-medium">{selectedOrder.price}</p>
              </div>
            </div>

            <div className="mt-8 flex justify-center gap-4">
              <button
                className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
                onClick={closeModal}
              >
                Close
              </button>
              <button
                className="px-6 py-2 bg-green-500 text-white rounded hover:bg-green-600"
                onClick={() => {
                  alert("Order marked as complete!");
                  closeModal();
                }}
              >
                Complete
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
