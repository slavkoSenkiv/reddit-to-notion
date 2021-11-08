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
'''text = """|   Real 
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
# text_list = text.split('\n')
# print(text)'''
"""for reply in text_list:
    if reply.startswith('|  '):
        new_list.append(reply)
    if reply.startswith('|  '):
        new_list.append(reply)"""
old_list = ['1a', '2b', '3c', '2d', '3e', '1f', '2g', '1h', '2i', '3g', '2k', '3m', '1l', '1n', '2o']
print(old_list)
new_list = []

for item in old_list:

    if item.startswith('1'):
        new_list.append([item])
        print(new_list)

        second_item_after_first_lvl = old_list[old_list.index(item) + 1]
        if second_item_after_first_lvl.startswith('2'):
            new_list[new_list.index([item])].append([second_item_after_first_lvl])
            print(new_list)

            if old_list.index(second_item_after_first_lvl) + 1 <= len(old_list) - 1:
                third_item_after_second_lvl = old_list[old_list.index(second_item_after_first_lvl) + 1]
                if third_item_after_second_lvl.startswith('3'):
                    print(third_item_after_second_lvl)



print(new_list)



