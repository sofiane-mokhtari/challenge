from instabot import Bot


bot = Bot()
bot.login(username="jeans_louis_louis_louis@outlook.com", password="jeans_louis")
user_id = bot.get_user_id_from_username("lego")
user_info = bot.get_user_followers (user_id)
print(user_info)
