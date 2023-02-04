import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Slider from "../../components/imageSlider/ImageSlider";
import "./home.css"
import BottomBar from "../../components/bottombar/Bottombar"



export default function Home(){
    return(
        <>
            <Topbar/>

            <div className="homeContainer">
                <Slider/>
            </div>
            <BottomBar/>

     </>

    )
}