import "./rightbar.css";

export default function Rightbar() {
    return (
        <div className="rightbar">
            <div className="rightbarWrapper">
                <div className="trendingCategoriesContainer">
                    <div className='Sports'>
                        <span className="SportsText">
                            Sports
                        </span>
                    </div>
                    <div className="Academics">
                        <span className="AcademicsText">Academics</span>
                    </div>
                    <div className="Music">
                        <span className="MusicText">Music</span>
                    </div>
                </div>
            </div>
        </div>
    )

}