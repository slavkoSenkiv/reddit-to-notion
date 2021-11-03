from notion.client import NotionClient
from notion.block import TextBlock


# <editor-fold desc="get credentials and auth">
credentials_path = '/Users/ysenkiv/Code/access files/personal/notion/token_v2.txt'
with open(credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    token_v2 = lines[0].strip()
client = NotionClient(token_v2=token_v2)
# </editor-fold>


client = NotionClient(token_v2="2663bdfac52d99078bb528ac7f5047574a4c1419b2ff2dc6da1ea467e6bb300030fb2a2e70adfb9da4cd3d15882bdcb63c5d364e6d687ea0cca4a7a51f051e93530019a1cd15dec8c3abb2e64e98")

page = client.get_block("https://www.notion.so/slavkosenkiv/test-notion_py-a7cfa4acd0284bb592ba271ffec21e83")

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "1"

newchild = page.children.add_new(TodoBlock, title="Something to get done")
newchild.checked = True
text = 'qwert'
newchild1 = page.children.add_new(TextBlock, title='qwert')
