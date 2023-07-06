from nextguild import Data 

def channels_test(bot):
    try:
        print("Test 2: Starting")
        server_id = 'aE9z41Kj'
        category_id = 703820
        message_id = "4925c0d7-4d71-4e57-981c-0e1f7d6b919d"
        name = "Test Channel"
        topic = "Test Topic"
        is_public = True
        channel_type = ["announcements", "chat", "calendar", "forums", "media", "docs", "voice", "list", "scheduling", "stream"]

        #creating channels
        print("Creating Channels")
        ids = []
        for type in channel_type:
            ids.append(Data(bot.create_channel(server_id=server_id, channel_type=type, name=name, topic=topic, is_public=is_public)).id)
        ids.append(Data(bot.create_channel(message_id=message_id, channel_type="chat", name=name)).id)
        for id in ids:
            bot.delete_channel(id)

        #updating channels
        print("Updating Channels")
        id = Data(bot.create_channel(server_id=server_id, channel_type="chat", name=name)).id
        data = Data(bot.update_channel(id, name="Updated Channel", topic="Updated Topic", is_public=False))
        if not data.updated_at:
            raise Exception("No updated_at in response")
        if not data.updated_by:
            raise Exception("No updated_by in response")
        bot.delete_channel(id)

        #getting channels
        print("Getting Channels")
        data = Data(bot.create_channel(server_id=server_id, channel_type="chat", name=name, topic=topic, is_public=True))
        if not data.id:
            raise Exception("No id in response")
        if not data.type:
            raise Exception("No type in response")
        if not data.name:
            raise Exception("No name in response")
        if not data.topic:
            raise Exception("No topic in response")
        if not data.created_at:
            raise Exception("No created_at in response")
        if not data.created_by:
            raise Exception("No created_by in response")
        if not data.server_id:
            raise Exception("No server_id in response")
        if not data.group_id:
            raise Exception("No group_id in response")
        if not data.is_public:
            raise Exception("No is_public in response")
        bot.delete_channel(data.id)
        

        print("Test 2: Passed")
    except Exception as e:
        print("Test 2: Failed", e)