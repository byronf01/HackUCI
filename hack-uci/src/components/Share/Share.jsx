import React, { useState } from 'react';
import "./share.css";
import PermMediaIcon from '@mui/icons-material/PermMedia';

export default function Share() {
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    };

    const handlePublishButtonClick = () => {
        console.log(inputValue);
    };

    return (
        <div className="share">
            <div className="shareWrapper">
                <div className="shareTop">
                    <img className="shareClubImg" src="/Assets/Profile1.jpg" alt="" />
                    <input placeholder="Hey UCI Clubs - Share Your Exciting Events and Adventures" className="shareInput" onChange={handleInputChange} />
                </div>
                <hr className="shareHr" />
                <div className="shareButton"></div>
                <div className="shareOptions">
                    <div className="shareOption">
                        <PermMediaIcon htmlColor="blue" className="shareIcon" />
                        <span className="shareOptionText">Photo/Video</span>
                    </div>
                    <button className="shareButton" onClick={handlePublishButtonClick}>Publish</button>
                </div>
            </div>
        </div>
    );
}