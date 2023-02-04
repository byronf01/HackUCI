import "./club.css";
import Topbar from "../../components/topbar/Topbar";
import Feed from "../../components/feed/Feed";
import Sidebar from "../../components/sidebar/Sidebar";
//import Rightbar from "../../components/rightbar/Rightbar"




export default function Club() {
    return(
        <>
            <Topbar />
            <div className = "clubContainer">
                <Sidebar />
                <Feed />

            </div>
        
        </>

    )

}