from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import ToggleBlock
import re
import datetime
"""for reply in text_list:
    if reply.startswith('|  '):
        comment_1 = notion_page.children.add_new(ToggleBlock, title=reply)
    if reply.startswith('|  |   '):
        comment_2 = comment_1.children.add_new(ToggleBlock, title=reply)
        toggle_1 = notion_page.children.add_new(ToggleBlock, title='1')
toggle_2 = toggle_1.children.add_new(ToggleBlock, title='2')"""
# <editor-fold desc="vetiables">
notion_credentials_path = '/Users/ysenkiv/Code/access files/personal/notion/token_v2.txt'
with open(notion_credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    token_v2 = lines[0].strip()
client = NotionClient(token_v2=token_v2)
notion_page = client.get_block('https://www.notion.so/slavkosenkiv/test-page-6c252540395e433f83d3cd21dabfad9f')

# </editor-fold>
text = """|   Real curious what those stars stand for
|   |   Yukon
|   I was offered a Yukon project for $10.61/hr but I am still stuck in the - IN PROGRESS - status. How does qualification work? I've been doing stuff in the academy but when I am done with a quiz it boots me back to my project home screen, I try to go back to the academy to try to finish the academy stuff but then I just have to re-take the quizzes I've done. There wasn't really explanation when it came to the qualification process.
|   |   i dont know if your project is about page quality rating, if it is, you'll get email about your exam date. a 3 part exam. then after you finish that they will email you if you passed or not. if you passed you'll get access to yukon page in appen. there will be detailed email about how to work. maybe you missed the email? did you get exam?
|   |   |   I didn't get any emails or an exam date. It is for a Search Engine Evaluator but in the academy stuff I am doing stuff for page quality, well the stuff I get to do.
|   My worst experiences with Appen are when I study for several hours to pass an exam, then I pass it, and then I find out that the project has been terminated or no work ever comes my way. Appen really doesn't give a fuck about you.
|   I get $12.50 while gf gets $14
|   >  i was expecting i can grind working 8 hours a day   I want to see your face when you find out about NRT!
|   |   what is NRT?
|   |   |   No Rater Tasks. Basically, there isn't always work available, often for hours at a time. When work runs out, there is no real way of telling when it will come back, or how much of it there will be. Depending on your locale this could be a little problem, or a big problem.There are also account restrictions, for example, new raters are typically limited to a certain number of daily hours, as well as things like botting, that can spoil your day. Botting is when some algorithm in the system decides it doesn't like your work and locks you out until a manual audit of it is completed. This can take hours or days,  Edit: I can see that you've most likely already encountered these problems, so this will really mostly benefit others who are curious,
|   |   |   |   I've been 'botted' on my favorite project and they haven't been able to do the manual review for weeks."""
test_text = """|   Real 
|   |   Yukon
|   I was
|   |   i dont know
|   |   |   I didn't get
|   My worst
|   I get $12.50
|   >  i was expecting
|   |   what is NRT?
|   |   |   No Rater Tasks. 
|   |   |   |   I've been 'botted'"""

text_list = test_text.split('\n')
print(text_list)
new_list = []
for reply in text_list:
    if reply.startswith('|  '):
        new_list.append(reply)
    if reply.startswith('|  '):
        new_list.append(reply)




