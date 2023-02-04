import "./topbar.css";
import SearchIcon from '@mui/icons-material/Search';


export default function Topbar() {
    return (
      <div className="topbarContainer">
        <div className="topbarLeft">
          <span className="logo">DeadlyHacks</span>
        </div>
        <div className="topbarCenter">
          <div className="searchbar">
            <SearchIcon className="searchIcon" />
            <input
              placeholder="Search for Club Posting"
              className="searchInput"
            />
          </div>
        </div>
        <div className="topbarRight">
          <div className="topbarLinks">
            <span className="topbarLink">Clubs</span>
            <span className="topbarLink">Friends</span>
            <span className="topbarLink">Events</span>
            <span className="topbarLink">Calander</span>
          </div>
        
          </div>
          <img src="/Assets/Image1.png" alt="" className="topbarImg"/>
        </div>
    );
  }