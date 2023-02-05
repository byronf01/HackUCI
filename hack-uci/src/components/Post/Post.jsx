import "./post.css";
import MoreVertIcon from '@mui/icons-material/MoreVert';
import {Users} from "../../test_data";
import {useState} from "react";



export default function Post(post) {
    const handlePostButtonClick = () => {
    };
    function checkUsers(Users) {
        const user_length = Users.length;
        for (var i=0; i<user_length; ++i){
            if (Users[i].userID == post.post.authorID){
                return Users[i].username;
            };
        }
        return null;
    }

    const[like,setLike] = useState(post.post.likes);
    const[isLiked,setIsLiked] = useState(false);

    const likeHandler = () => {
        setLike(isLiked ? like - 1 : like + 1);
        setIsLiked(!isLiked)
    }

    return (
        <div className="post">
            <div className="postWrapper">
                <div className="postTop">
                    <div className="postTopLeft">
                        <img className="postProfileImage" src="/Assets/Profile1.jpg" />
                        <span className="postUsername">
                            {checkUsers(Users)}
                            </span>
                        <span className="postDate">{post.post.date}</span>
                    </div>
                    <div className="postTopRight"></div>
                    <MoreVertIcon />
                </div>
                <div className="postCenter">
                    <span className="postDescription">{post.post.description}
                    </span>
                    <img className="postImage" src={post.post.image} />
                </div>

                <div className="postBottom">
                    <div className="postbottomLeft">
                        <img className="heartIcon" src="/Assets/Heart.png" onClick={likeHandler} alt="" />
                        <img className="likeIcon" onClick={likeHandler} src="/Assets/Like.png" alt="" />
                        <span className="postlikeCounter">{like} people liked it</span>
                    </div>
                    <div className="postbottomRight"></div>
                    <span className="postCommentText">{post.post.comments} Comments</span>
                    <button id="post-button" onClick={handlePostButtonClick}>Post</button>
                </div>

            </div>

        </div>
    )
}
