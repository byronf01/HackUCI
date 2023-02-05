import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import "./home.css"
import BottomBar from "../../components/bottombar/Bottombar"
 
const Error = () => {
   return(
      <>
         <Topbar/>

         <div className="largeError">
            <span>Error: Page does not exist!</span>
         </div>
         <BottomBar/>
      </>

   );
}
 
export default Error;