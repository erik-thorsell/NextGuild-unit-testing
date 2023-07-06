from nextguild import Data

def users_test(bot):
    try:
        server_id = 'aE9z41Kj'
        user_id = '409LrYQd'

        print("Test 4: Starting")

        #update nickname
        print("Updating Nickname")
        data = Data(bot.update_nickname(server_id, user_id, 'test'))
        if not data.name:
            raise Exception("No name in response")
        
        #deleting nickname
        print("Deleting Nickname")
        bot.delete_nickname(server_id, user_id)

        #member has role
        print("Checking member has role...")
        if bot.member_has_role(server_id, user_id, 1234):
            raise Exception("Member has role issue 1")
        if bot.member_has_role(server_id, user_id, 1234, 'all'):
            raise Exception("Member has role issue 2")
        if not bot.member_has_role(server_id, user_id, 30136197):
            raise Exception("Member has role issue 3")
        if not bot.member_has_role(server_id, user_id, 30136197, 'all'):
            raise Exception("Member has role issue 4")
        if not bot.member_has_role(server_id, user_id, [30136197]):
            raise Exception("Member has role issue 5")
        if not bot.member_has_role(server_id, user_id, [30136197], 'all'):
            raise Exception("Member has role issue 6")
        if not bot.member_has_role(server_id, user_id, [30136197, 30136196]):
            raise Exception("Member has role issue 7")
        if not bot.member_has_role(server_id, user_id, [30136197, 30136196], 'all'):
            raise Exception("Member has role issue 8")
        if not bot.member_has_role(server_id, user_id, [30136197, 2]):
            raise Exception("Member has role issue 9")
        if bot.member_has_role(server_id, user_id, [30136197, 2], 'all'):
            raise Exception("Member has role issue 10")

        #member is owner
        print("Checking member is owner...")
        if bot.member_is_owner(server_id, user_id):
            raise Exception("Member is owner issue 1")
        if not bot.member_is_owner(server_id, 'mqEVqDXm'):
            raise Exception("Member is owner issue 2")
        
        print("Test 4: Passed")
    except Exception as e:
        print("Test 4: Failed", e)

    