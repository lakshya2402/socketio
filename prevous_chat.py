from utils.cache import update_chatroom_chats, get_chatroom_chats
from utils.common import return_response
from utils.messageEncoder import translateMessage
from utils.mongo.mongo_client import MongoConfig
from utils.properties import DB_name


def get_previous_chat(count, room_id, user_name):
    if count is None:
        count = 1
    messages = get_chatroom_chats(room_id)
    if not messages["decrypted"]:
            for i in messages.get("messages"):
                temp_message = i.get("message")
                i["message"] = translateMessage(room_id, temp_message, 'decrypt')
            messages["decrypted"] = True
            update_chatroom_chats(room_id, messages)
    final_message = []
    if messages is not None:
        for i in messages.get("messages")[-50 * count:]:
            if i.get("sender") == user_name:
                i["sender"] = "you"
            final_message.append(i)
        return messages
    else:
        return []