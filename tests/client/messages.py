from nextguild import Embed, Data
import datetime

def messages_test(bot):
    try:
        print("Test 1: Starting")
        channel_id = "f03de35e-27de-49ef-a021-8748d205dc48"
        content = "Test Message"
        embed = Embed(title="Hello <@mb1K7oKd>", description="Test Embed")
        reply_message_id = ["4925c0d7-4d71-4e57-981c-0e1f7d6b919d"]
        is_private = True
        is_silent = True

        #sending messages
        print("Sending Messages")
        ids = []
        ids.append(Data(bot.send_message(channel_id, content)).id)
        ids.append(Data(bot.send_message(channel_id, content, embed=embed)).id)
        ids.append(Data(bot.send_message(channel_id, content, embed=embed, reply_message_ids=reply_message_id)).id)
        ids.append(Data(bot.send_message(channel_id, content, embed=embed, reply_message_ids=reply_message_id, is_private=is_private)).id)
        ids.append(Data(bot.send_message(channel_id, content, embed=embed, reply_message_ids=reply_message_id, is_silent=is_silent)).id)
        for id in ids:
            bot.delete_message(channel_id, id)
        
        print("Editing Messages")
        id = Data(bot.send_message(channel_id, content)).id
        bot.edit_message(channel_id, id, content="Edited Message")
        bot.edit_message(channel_id, id, embed=embed)
        bot.edit_message(channel_id, id, content="Edited Message", embed=embed)
        bot.delete_message(channel_id, id)

        print("Getting Messages")
        id = Data(bot.send_message(channel_id, content)).id
        bot.get_message(channel_id, id)
        response = Data(bot.send_message(channel_id, content, embed=embed, reply_message_ids=reply_message_id, is_silent=is_silent))
        if not response.id:
            raise Exception("No id in response")
        if not response.type:
            raise Exception("No type in response")
        if not response.server_id:
            raise Exception("No server_id in response")
        if not response.group_id:
            raise Exception("No group_id in response")
        if not response.channel_id:
            raise Exception("No channel_id in response")
        if not response.content:
            raise Exception("No content in response")
        if not response.embeds:
            raise Exception("No embed in response")
        if not response.mentions:
            raise Exception("No mentions in response")
        if not response.reply_message_ids:
            raise Exception("No reply_message_ids in response")
        if not response.is_private:
            raise Exception("No is_private in response")
        if not response.is_silent:
            raise Exception("No is_silent in response")
        if not response.created_at:
            raise Exception("No created_at in response")
        if not response.created_by:
            raise Exception("No created_by in response")
        bot.get_channel_messages(channel_id)
        bot.get_channel_messages(channel_id, limit=1)
        #before is the current time as an ISO 8601 timestamp
        timern = datetime.datetime.now()
        bot.get_channel_messages(channel_id, before="2021-01-01T00:00:00.000Z")
        #after is the current time as an ISO 8601 timestamp
        bot.get_channel_messages(channel_id, after=timern.isoformat())

        #purge
        print("Purging Messages")
        bot.purge(channel_id, 2)

        print("Test 1: Passed")
    except Exception as e:
        print("Test 1: Failed", e)
