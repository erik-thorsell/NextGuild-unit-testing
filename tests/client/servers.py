from nextguild import Data

def servers_test(bot):
    try:
        server_id = 'aE9z41Kj'
        user_id = '409LrYQd'

        print("Test 3: Starting")

        #getting servers
        print("Getting Servers")
        data = Data(bot.get_server(server_id))
        if not data.id:
            raise Exception("No id in response")
        if not data.owner_id:
            raise Exception("No owner_id in response")
        if not data.name:
            raise Exception("No name in response")
        if not data.url:
            raise Exception("No url in response")
        if not data.default_channel_id:
            raise Exception("No default_channel_id in response")
        if not data.created_at:
            raise Exception("No created_at in response")
        
        #getting server members
        print("Getting Server Members")
        data = Data(list(bot.get_server_members(server_id))[0])
        if not data.id:
            raise Exception("No id in response")
        if not data.type:
            raise Exception("No type in response")
        if not data.name:
            raise Exception("No name in response")
        if not data.avatar:
            raise Exception("No avatar in response")
        if not data.role_ids:
            raise Exception("No role_ids in response")
        
        #getting server member
        print("Getting Server Member")
        data = Data(bot.get_server_member(server_id, user_id))
        if not data.id:
            raise Exception("No id in response")
        if not data.type:
            raise Exception("No type in response")
        if not data.name:
            raise Exception("No name in response")
        if not data.avatar:
            raise Exception("No avatar in response")
        if not data.role_ids:
            raise Exception("No role_ids in response")
        
        print("Test 3: Passed")
    except Exception as e:
        print("Test 3: Failed", e)
    
