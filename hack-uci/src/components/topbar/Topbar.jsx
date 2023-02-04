import "./topbar.css";
import SearchIcon from '@mui/icons-material/Search';
import { BrowserRouter, Route, NavLink } from "react-router-dom";



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
        {/* <div className="topbarRight"> */}
          {/* <div className="topbarLinks"> */}
          <nav>
            <ul className="topbarRight">
            <ui>
                <NavLink to="/profile" className="topbarLinks">Profile</NavLink>
              </ui>
              <ui>
                <NavLink to="/post" className="topbarLinks">Post</NavLink>
              </ui>
              <ui>
                <NavLink to="/calendar" className="topbarLinks">Calendar</NavLink>
              </ui>
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