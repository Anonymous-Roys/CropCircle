import React from "react";
import { useNavigate } from "react-router-dom";
import FamerLoginBg from "../../assets/Background-images/pickled-cabbage-hands-smiling-male-farmer-man-farmer-holding-cabbage-green-foliage-harvest-concept 1.png";

const FarmerSignUp = () => {
  const navigate = useNavigate();

  const formData = {
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  };

  const [form, setForm] = React.useState(formData);
  const [error, setError] = React.useState("");
  const [emailError, setEmailError] = React.useState("");
  const [success, setSuccess] = React.useState("");
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function Handlechange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
    if (form.email) {
      if (!emailRegex.test(e.target.value)) {
        setEmailError("Please enter a valid email");
      }
    }
  }
  function HandleSubmit(e) {
    e.preventDefault();
    if (!form.name || !form.email || !form.password || !form.confirmPassword) {
      alert("Please fill the form");
      return;
    }
    // try {
    //   //const response = await post("http://localhost:8000/api/farmer/signup", form);
    //   if (response.status === 200) {
    //     navigate("/farmer/login");
    //     return;
    //   }
    //   setSuccess("Account created successfully");
    //   setError("");
    //   setForm(formData);
    // } catch (error) {
    //   setError("Something went wrong");
    // }
    console.log(form);
  }

  return (
    <div
      className="flex justify-end h-screen bg-auto bg-no-repeat"
      style={{
        backgroundImage: `url(${FamerLoginBg})`,
      }}
    >
      <div
        className="flex flex-col items-center md:w-1/2 bg-white sm:p-10 md:p-16 border border-green-400 "
        style={{
          borderBottomLeftRadius: "3.4rem",
          borderTopLeftRadius: "3.4rem",
        }}
      >
        <h2 className="text-3xl font-bold sm:mt-9 text-green-700 mb-2">
          Farmer Sign Up
        </h2>
        <h3 className="text-2xl font-semibold mb-4">Welcome to Crop Cicle</h3>
        <p className="text-gray-500 mb-6">lorem ipsum</p>
        <form onSubmit={HandleSubmit} className="space-y-4" action="">
          <input
            type="text"
            placeholder="Full Name"
            name="name"
            onChange={Handlechange}
            value={form.name}
            className="w-full px-4 py-3 border focus:outline-none focus:border-green-400 rounded"
          />
          <input
            type="email"
            placeholder="Email"
            name="email"
            value={form.email}
            onChange={Handlechange}
            className=" w-full px-4 py-3 border focus:outline-none focus:border-green-400 rounded"
          />
          <input
            type="password"
            placeholder="Password"
            value={form.password}
            name="password"
            onChange={Handlechange}
            className="w-full px-4 py-3 border focus:outline-none focus:border-green-400 rounded"
          />
          <input
            type="password"
            placeholder="Confirm Pasword"
            value={form.confirmPassword}
            onChange={Handlechange}
            name="confirmPassword"
            className="w-full px-4 py-3 border focus:outline-none focus:border-green-400 rounded"
          />
          <button
            type="submit"
            className="w-full bg-green-600 text-white py-4 rounded-md hover:bg-green-700"
          >
            Sign In
          </button>
        </form>
        <p className="text-center mt-4 text-sm text-gray-500">
          Already have an account?{" "}
          <button
            onClick={() => navigate("/farmer/login")}
            className="text-green-600 cursor-pointer"
          >
            Log In
          </button>
        </p>
      </div>
    </div>
  );
};

export default FarmerSignUp;
