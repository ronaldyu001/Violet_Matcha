// App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './components/Home/Home';
import Layout from './components/Layout/Layout';


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="home" element={<Home />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}