import "./post.css"
import MoreVertIcon from '@mui/icons-material/MoreVert';

export default function Post(post) {
    const handlePostButtonClick = () => {
    };
    console.log(post.post.description)
    return (
        <div className="post">
            <div className="postWrapper">
                <div className="postTop">
                    <div className="postTopLeft">
                        <img className="postProfileImage" src="/Assets/Profile1.jpg" />
                        <span className="postUsername">Random Person</span>
                        <span className="postDate">{post.post.date}</span>
                    </div>
                    <div className="postTopRight"></div>
                    <MoreVertIcon />
                </div>
                <div className="postCenter">
                    <span className="postDescription">{post.post.description}
                    </span>
                    <img className="postImage" src="/Assets/Image1.png" />
                </div>

                <div className="postBottom">
                    <div className="postbottomLeft">
                        <img className="heartIcon" src="/Assets/Heart.png" alt="" />
                        <img className="likeIcon" src="/Assets/Like.png" alt="" />
                        <span className="postlikeCounter">{post.post.likes} people liked it</span>
                    </div>
                    <div className="postbottomRight"></div>
                    <span className="postCommentText">{post.post.comments} Comments</span>
                    <button id="post-button" onClick={handlePostButtonClick}>Post</button>
                </div>

            </div>

        </div>
    )
}
