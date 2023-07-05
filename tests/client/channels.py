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
        bot.update_channel(id, name="Updated Channel", topic="Updated Topic", is_public=False)
        bot.delete_channel(id)

        #getting channels
        print("Getting Channels")
        data = Data(bot.create_channel(server_id=server_id, channel_type="chat", name=name, topic=topic, is_public=False))
        if not data.id:
            raise Exception("No id in response")
        if not data.type:
            raise Exception("No type in response")
        if not data.name:
            raise Exception("No name in response")
        

        print("Test 2: Passed")
    except Exception as e:
        print("Test 2: Failed", e)