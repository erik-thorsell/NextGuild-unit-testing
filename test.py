from nextguild import *
from tests.client.messages import messages_test
from tests.client.channels import channels_test
from tests.client.servers import servers_test
from tests.client.users import users_test


bot = Client('token')
events = Events(bot)

messages_test(bot)
channels_test(bot)
servers_test(bot)
users_test(bot)