from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import CollectionViewPageBlock
from notion import block
import notion
# <editor-fold desc="get credentials and auth">
credentials_path = '/Users/ysenkiv/Code/access files/personal/notion/token_v2.txt'
with open(credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    token_v2 = lines[0].strip()
client = NotionClient(token_v2=token_v2)
page = client.get_block("https://www.notion.so/slavkosenkiv/test-43eaf29368604c33982e8c552f6b19bb")
cv = client.get_collection_view("https://www.notion.so/slavkosenkiv/935a6bc705a340f381218492c8d862ba?v=010a11d8666e4a4b889260ea5ee3a07f")
# </editor-fold>

text = 'random text\n here'


row = cv.collection.add_row()
row.name = "Just some data4"
row.tags = ['tag3']
row.children.add_new(TextBlock, title=text)