import "./ImageSlider.css";
import SimpleImageSlider from "react-simple-image-slider";

const images = [ {url: "/Assets/Test1.jpg"} , {url: "/Assets/Test2.jpg"}, {url: "/Assets/Test3.jpg"}]

export default function Slider() {
    return (
        <div className="sliderContainer">
            <SimpleImageSlider        className="ImageSlider"
                width={1600}
                height={700}
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