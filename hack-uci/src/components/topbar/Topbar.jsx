import "./topbar.css";
import SearchIcon from '@mui/icons-material/Search';
import { BrowserRouter, Route, NavLink } from "react-router-dom";
import Login from "../../pages/Login/Login"



export default function Topbar() {
    return (
      <div className="topbarContainer">
        <ul className="topbarLeft">
              <ui>
                <NavLink to="/" className="logo">DeadlyHacks</NavLink>
              </ui>
          </ul>
        <div className="topbarCenter">
          <div className="searchbar">
            <SearchIcon className="searchIcon" />
            <input
              placeholder="Search for Club Posting"
              className="searchInput"
            />
          </div>
        </div>
          <nav>
            <ul className="nav-li">
            <ui>
                <NavLink to="/profile" className="nav-bar-link">Profile</NavLink>
              </ui>
              <ui>
                <NavLink to="/post" className="nav-bar-link">Post</NavLink>
              </ui>
              <ui>
                <NavLink to="/calendar" className="nav-bar-link">Calendar</NavLink>
              </ui>
            </ul>
          </nav>
          {/* <NavLink to="/login" className="nav-bar-link"> */}
          <img src="/Assets/Image1.png" alt="" className="topbarImg"/>
        </div>
    );
  }