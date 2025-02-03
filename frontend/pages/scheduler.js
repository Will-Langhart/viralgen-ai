import React, { useState } from 'react';

export default function Scheduler() {
    const [status, setStatus] = useState("");

    const schedulePost = async () => {
        const response = await fetch('/schedule', { method: 'POST' });
        const data = await response.json();
        setStatus(data.status);
    };

    return (
        <div>
            <h1>Schedule a Social Media Post</h1>
            <button onClick={schedulePost}>Schedule</button>
            <p>{status}</p>
        </div>
    );
}
