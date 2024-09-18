import { useState, useEffect } from 'react';

const Loader = () => {
  const [dots, setDots] = useState(1);

  useEffect(() => {
    const interval = setInterval(() => {
      setDots((prevDots) => (prevDots === 3 ? 1 : prevDots + 1));
    }, 500);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="text-3xl font-bold text-gray-600">
        Loading{'.'.repeat(dots)}
      </div>
    </div>
  );
};

export default Loader;
