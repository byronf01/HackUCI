import "./topbar.css";
import SearchIcon from '@mui/icons-material/Search';
import { BrowserRouter, Route, NavLink } from "react-router-dom";



export default function Topbar() {
    return (
      <div className="topbarContainer">
        <ul className="topbarLeft">
              <li>
                <NavLink to="/" className="logo">DeadlyHacks</NavLink>
              </li>
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
        {/* <div className="topbarRight"> */}
          {/* <div className="topbarLinks"> */}
          <nav>
            <ul className="topbarRight">
            <li>
                <NavLink to="/clubs" className="topbarLinks">Clubs</NavLink>
              </li>
              <li>
                <NavLink to="/post" className="topbarLinks">Post</NavLink>
              </li>
              <li>
                <NavLink to="/calendar" className="topbarLinks">Calendar</NavLink>
              </li>
            </ul>
          </nav>
            {/* <span className="topbarLink">Friends</span>
            <span className="topbarLink">Events</span>
            <span className="topbarLink">Calander</span> */}
          {/* </div> */}
        {/* </div> */}
          <img src="/Assets/Image1.png" alt="" className="topbarImg"/>
        </div>
    );
  }