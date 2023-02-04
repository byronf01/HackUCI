import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Slider from "../../components/imageSlider/ImageSlider";
import "./home.css"


const images = [ {url: "/Assets/Test1.jpg"}, {url: "/Assets/Test2.jpg"}, {url: "/Assets/Test3.jpg"}]


export default function Home(){
    return(
        <>
            <Topbar/>
            <Slider/>
                
            <div className="homeContainer">
                <Sidebar/>
            </div>
     </>

    )
}