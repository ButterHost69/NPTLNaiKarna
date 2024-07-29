import discord
import json

BOT_TOKEN = None

CONFIG_JSON_PATH = "../config.json"
ANSWER_JSON_PATH = "../answers.json"

print("Checking if config.json ...")
try:
    with open(CONFIG_JSON_PATH, "r") as config:
        print("config.json found ...")
        BOT_TOKEN = json.load(config)['bot_token']

except:
    print("config.json not found ...\ncreating config.json ...")
    BOT_TOKEN = str(input("> Enter Discord Bot Token: "))
    config_data = {
        "bot_token": BOT_TOKEN,
        "users":[]
    }
    with open(CONFIG_JSON_PATH, "w") as config:
        json.dump(config_data, config, indent=4)

print(f"Discord Bot Token: {BOT_TOKEN}")


# answers.json config struture
# 
# {
#       ``` Manual Entries ```
#       "subject/couse name" : 
#        {
#               ``` URLs for Scrappers```
#               ``` Manual Entries ```
#               "links" : "link:here/url",
#               "answers" : {
#                   ``` These are weeks ```
#                   ``` Automatic Entries ```
#                   1 : {
#                           1 : "a",
#                           2 : "b",
#                           3 : "c",
#                       },
#                   2 : {
#                           1 : "a",
#                           2 : "b",
#                           3 : "c",
#                       },
#                },
#        },
# }

try:
    with open(ANSWER_JSON_PATH) as _:
        pass
except:
    with open(ANSWER_JSON_PATH, "w") as file:
        course_name = input("\n> Enter Course Name: ")
        answers_data = {
            course_name : {
                "url_name":"place/url/here",
                "answers":{}
            }
        }
        json.dump(answers_data, file, indent=4)
    

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

client = discord.Client(intents=intents)

# [] Submit :
#   [] Login NPTEL 
#     [] -> OPEN Course 
#         [] -> Check Last Not Done Week 
#             [] -> Select Answers 
#                 []-> Submit

# Register :
# [X] Register Discord Username : gmail email id ; password

# Get Score :
# [] Show All Scores

DSMR_COURSE_URL = 'https://onlinecourses.nptel.ac.in/noc24_cs133/announcements?force=true'
AAD_COURSE_URL = 'https://onlinecourses.nptel.ac.in/noc24_cs116/announcements?force=true'

help_message = """
NPTEL Kardega Tera... Tu bas Name de aur Answer bhejte reh

register user -> 
                 ``/bot register nptl_gmail_id nptl_gmail_password``
submit answer -> 
                 ``/bot answers course_name week0``
                     ``1 a``
                     ``2 b``
                     ``3 c``
"""

def add_answer_to_answers_json(course_name, week_no, answer):
    with open(ANSWER_JSON_PATH, "r") as file:
        json_data = json.load(file)
        try:
            # new_answer = json_data[course_name]['answers']
            json_data[course_name]['answers'][week_no] = answer
            with open(ANSWER_JSON_PATH, "w") as write_file:
                json.dump(json_data, write_file, indent=4)
        except Exception as e:
            print(e)

def format_answer(week_no, answer_array):
    i = 0
    week_ans = {}
    while i < len(answer_array):
        week_ans[i] = answer_array[i+1]
        i += 2
    print({week_no: week_ans})
    return week_ans
    




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f"{message.content} - {message.author}")
    if message.content.startswith('/bot'):
        words = message.content.replace("\n", " ")
        words = words.split(" ")
        if len(words) >= 2:
            command = words[1]
            content = message.content.replace("/bot","")
            if command == "help":
                await message.channel.send(help_message)
            
            elif command == "answers":
                # Question and answers
                course_name = words[2]
                week_no = words[3]
                answers = words[4:]
                try:
                    add_answer_to_answers_json(course_name, week_no ,format_answer(week_no, answers))
                    print(f"User: {message.author} Has Sumbitted the Answers\n{answers} for {course_name} {week_no}")
                    await message.channel.send("Answers Added !!")
                except Exception as e:
                    print(e)
                    await message.channel.send("Answers not Added !! Error Occured !!")

            
            elif command == "register":
                email = words[2]
                password = words[3]
                new_user = {
                    "username" : message.author.name,
                    "email" : email,
                    "password" : password
                }
                with open(CONFIG_JSON_PATH, "r") as config:
                    config_data = json.load(config)
                    config_data['users'].append(new_user)
                    with open(CONFIG_JSON_PATH, "w") as config:
                        json.dump(config_data, config, indent=4)
                    print(f"New User Added: {new_user['username']}")
                    await message.channel.send(f"Tereko Hamne Hamare System Me Daldiya @{message.author}\n")
            
            else :
                await message.channel.send(content)
        
        else:
            await message.channel.send("Hello !!")



client.run(BOT_TOKEN)