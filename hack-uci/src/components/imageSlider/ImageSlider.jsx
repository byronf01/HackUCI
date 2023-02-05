import "./ImageSlider.css";
import SimpleImageSlider from "react-simple-image-slider";
import useWindowDimensions from "./windowDimensions";
const images = [ {url: "/Assets/Test1.jpg"} , {url: "/Assets/Test2.jpg"}, {url: "/Assets/Test3.jpg"}]



export default function Slider() {
    const { height, width } = useWindowDimensions();
    return (
        <div className="sliderContainer">
            <SimpleImageSlider        className="ImageSlider"
                width={width}
                height={height}
                images={images}
                showBullets={true}
                showNavs={true}
                loop={true}
                autoPlay={true}
                useGPURender={true}
                />

        </div>

    )

}