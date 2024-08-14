import React, { useState } from 'react';
import axios from 'axios';

const ChatbotInterface = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const sendMessage = async () => {
        if (input.trim() === '') return;

        const newMessages = [...messages, { text: input, sender: 'user' }];
        setMessages(newMessages);
        setInput('');

        try {
            const response = await axios.post('/api/chatbot', { message: input });
            setMessages([...newMessages, { text: response.data, sender: 'bot' }]);
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    return (
        <div className="chatbot-interface">
            <div className="message-container">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <div className="input-container">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
                />
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default ChatbotInterface;
