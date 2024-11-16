import React from "react";
import { NavLink } from "react-router-dom";

const UnderDevelopment = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen px-4 bg-gray-50">
      {/* Icon or Illustration */}
      <div className="mb-8">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="w-24 h-24 text-gray-600"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          strokeWidth="2"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M12 8c1.656 0 3 1.344 3 3s-1.344 3-3 3-3-1.344-3-3 1.344-3 3-3zm0 0c4.418 0 8 3.582 8 8H4c0-4.418 3.582-8 8-8zm0 0V4m0 16v-4"
          />
        </svg>
      </div>

      {/* Text */}
      <h1 className="mb-4 text-3xl font-bold text-gray-800 md:text-5xl">
        Page Under Development
      </h1>
      <p className="max-w-lg mb-6 text-lg text-center text-gray-600">
        We are working hard to bring this page to life. Check back later to see
        what’s new!
      </p>

      {/* Button */}
      <NavLink
        to="/"
        className="px-6 py-3 text-lg text-white transition duration-300 bg-green-600 rounded-lg shadow-md hover:bg-green-700 focus:outline-none focus:ring-4 focus:ring-green-500 focus:ring-opacity-50"
      >
        Return to Homepage
      </NavLink>
    </div>
  );
};

export default UnderDevelopment;
