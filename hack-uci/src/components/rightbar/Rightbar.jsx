import "./rightbar.css";
import SportsBaseballIcon from '@mui/icons-material/SportsBaseball';
import SchoolIcon from '@mui/icons-material/School';
import SportsEsportsIcon from '@mui/icons-material/SportsEsports';
import MusicNoteIcon from '@mui/icons-material/MusicNote';

export default function Rightbar() {
    return (
        <div className="rightbar">
            <div className="rightbarWrapper">
                <div className="trendingCategoriesContainer">
                        <span className="Title">Trending Tags</span>
                        <ul className="rightbarList">
                            <li className="rightbarListItem">
                                <SportsBaseballIcon classname="rightsidebarIcon"/>
                                <span className="rightbarListItemText">Sports</span>

                            </li>
                            <li className="rightbarListItem">
                                <SchoolIcon classname="rightsidebarIcon"/>
                                <span className="rightbarListItemText">Academics</span>

                            </li>
                            <li className="rightbarListItem">
                                <SportsEsportsIcon classname="rightsidebarIcon"/>
                                <span className="rightbarListItemText">Video Games</span>

                            </li>
                            <li className="rightbarListItem">
                                <MusicNoteIcon classname="rightsidebarIcon"/>
                                <span className="rightbarListItemText">Music</span>

                            </li>

                        </ul>
                </div>
                <div className="trendingClubsContainer">
                    <span className="Title">Top Clubs</span>
                    <ul className="rightbarList">
                            <li className="rightbarListItem">
                            <img className="rightbarClub" src="/Assets/UCISAA.png" />
                                <span className="rightbarListItemText">UCI SAA</span>
                               


                            </li>
                            <li className="rightbarListItem">
                            <img className="rightbarClub" src="/Assets/HackAtUCI.png" />
                                <span className="rightbarListItemText">Hack at UCI</span>
                                

                            </li>
                            <li className="rightbarListItem">
                            <img className="rightbarClub" src="/Assets/HikingClub.png" />
                                <span className="rightbarListItemText">Hiking Club</span>


                            </li>
                            <li className="rightbarListItem">
                                <img className="rightbarClub" src="/Assets/AlphaKappaPsi.png" />

                                <span className="rightbarListItemText">Alpha Kappa Psi</span>


                            </li>

                        </ul>
                </div>
            </div>
        </div>
    )

}