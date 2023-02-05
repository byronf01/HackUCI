import React, { Component } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import ReactDOM from "react-dom";
import Home from "./pages/home/Home";
import Calendar from './pages/home/calendar/calendar';
import Club from './pages/Clubs/Club';
import Error from './pages/home/Error';
import Layout from './components/topbar/layout';
 
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="Calendar" element={<Calendar />} />
          {/* <Route path="Profile" element={<Club />} /> */}
          <Route path="Post" element={<Club />} />
          <Route path="*" element={<Error />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));