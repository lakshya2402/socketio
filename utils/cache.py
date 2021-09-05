cache_maintainer = {}


def update_user_cache(user_id, data):
    print(data)
    if cache_maintainer.get(user_id) is None:
        cache_maintainer[user_id] = data
        return False
    else:
        return True


def get_user_details(user_id):
    return cache_maintainer.get(user_id)


chatroom_messages = {}


def update_chatroom_chats(chatroom_id, data):
    print(data)
    if chatroom_messages.get(chatroom_id) is None:
        chatroom_messages[chatroom_id] = data
        return False
    else:
        return True


def get_chatroom_chats(chatroom_id):
    return chatroom_messages.get(chatroom_id)
