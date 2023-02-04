import "./topbar.css";
import {PersonSearchOutlined, Person3Outlined, ChatBubbleOutline, Notifications} from "@mui/icons-material";

export default function Topbar() {
    return(
        <div className="topbarContainer">
            <div className="topbarLeft">
                <span className="logo">DeadlyHacks</span>
            </div>
            <div className="topbarCenter">
                <div className="searchbar">
                    <PersonSearchOutlined className="searchIcon"/>
                    <input 
                        placeholder="Search for club or post"
                        className="searchInput"/>
            </div>
            <div>


            </div>
            <div className="topbarRight">
                <div className="topbarLinks">
                    <span className = "topbarLink">Clubs</span>
                    <span className = "topbarLink">Friends</span>
                </div>
                <div className="topBarIcons">
                    <div className="topbarIconItem">
                        <Person3Outlined />
                        <span className="topbarIconBadge">1</span>
                    </div>
                    <div className="topbarIconItem">
                        <ChatBubbleOutline />
                        <span className="topbarIconBadge">1</span>
                    </div>
                    <div className="topbarIconItem">
                        <Notifications />
                        <span className="topbarIconBadge">1</span>
                    </div>
                </div>
            </div>

            <img src="/Assets/Image1.png" alt="" className="topbarImg"/>    
        </div>   
        </div>

    )

}