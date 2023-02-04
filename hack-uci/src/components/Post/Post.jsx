import "./post.css"
import MoreVertIcon from '@mui/icons-material/MoreVert';

export default function Post() {
    return (
        <div className="post">
            <div className="postWrapper">
                <div className="postTop">
                    <div className="postTopLeft">
                    <img className="postProfileImage" src="/Assets/Profile1.jpg"/>
                        <span className="postUsername">Random Person</span>
                        <span className="postDate">Days Ago</span>
                    </div>
                    <div className="postTopRight"></div>
                    <MoreVertIcon/>
                </div>
                <div className="postCenter">
                    <span className="postText">
                        Testing First Post
                    </span>
                    <img className="postImage" src="/Assets/Image1.png"/>
                </div>

                <div className="postBottom">
                    <div className="postbottomLeft">
                        <img className="heartIcon"src="/Assets/Heart.png" alt=""/>
                        <img className="likeIcon"src="/Assets/Like.png" alt=""/>
                        <span className="postlikeCounter">40 people liked it</span>
                    </div>
                    <div className="postbottomRight"></div>
                        <span className="postCommentText">12 Comments</span>
                </div>

            </div>
            
        </div>


    )

}

/*<img className="postProfileImage" src="/Assets/Profile1.jpg"/>*/