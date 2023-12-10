template = '''
<style>
.chat-message {
    padding: 2rem;
    border-radius: 1rem;
    margin-bottom: 1rem;
    display: flex;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.chat-message.user {
    background-color: #d6e9f3;
}
.chat-message.bot {
    background-color: #f5f5f5;
}
.chat-message .avatar {
    width: 15%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #000;
    font-family: Arial, sans-serif;
    font-size: 1.2rem;
}
</style>
'''

bot_avatar = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzGQJP3QhW4fwxM_AHrWtdkXYDCnUFkz57IzGnuC1ftk8FKg1g7J9tpUOhhHoI9AQZujo&usqp=CAU" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_avatar = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://e7.pngegg.com/pngimages/114/356/png-clipart-time-student-recruitment-learning-professional-others-service-vector-icons.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

