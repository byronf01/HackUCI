import "./feed.css"
import Share from "../Share/Share";
import Post from "../Post/Post"
import posts from "../../test_data"

export default function Feed() {
    return (
        <div className="feed">
            <div className="feedWrapper">
                <Share/>
                {posts.map((p) => (
                    <Post key={p.id} post={p}/>
                ))}
            </div>
        </div>
    )
}