import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const targetDate = new Date('2024-11-15T00:00:00').getTime();

  const [countdown, setCountdown] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0,
  });

  useEffect(() => {
    const interval = setInterval(() => {
      const now = new Date().getTime();
      const distance = targetDate - now;

      if (distance > 0) {
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        setCountdown({ days, hours, minutes, seconds });
      } else {
        clearInterval(interval);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [targetDate]);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    document.documentElement.classList.toggle('dark');
  };

  return (
    <div className={`min-h-screen flex flex-col items-center justify-center ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-900'}`}>
      <button
        className="mb-6 px-6 py-2 rounded-lg bg-blue-600 text-white hover:bg-blue-700 dark:bg-gray-800 dark:hover:bg-gray-700 transition"
        onClick={toggleDarkMode}
      >
        Toggle {darkMode ? 'Light' : 'Dark'} Mode
      </button>
      <h1 className="text-4xl font-extrabold mb-8">Countdown to Project Deployment</h1>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-6 text-center w-full max-w-2xl">
        <div className="flex flex-col items-center bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition">
          <span className="text-5xl font-bold">{countdown.days}</span>
          <p className="text-lg font-medium mt-2">Days</p>
        </div>
        <div className="flex flex-col items-center bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition">
          <span className="text-5xl font-bold">{countdown.hours}</span>
          <p className="text-lg font-medium mt-2">Hours</p>
        </div>
        <div className="flex flex-col items-center bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition">
          <span className="text-5xl font-bold">{countdown.minutes}</span>
          <p className="text-lg font-medium mt-2">Minutes</p>
        </div>
        <div className="flex flex-col items-center bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md transition">
          <span className="text-5xl font-bold">{countdown.seconds}</span>
          <p className="text-lg font-medium mt-2">Seconds</p>
        </div>
      </div>
    </div>
  );
}

export default App;
