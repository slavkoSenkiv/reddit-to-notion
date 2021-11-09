import praw
from praw.models import MoreComments
from notion.client import NotionClient
from notion.block import NumberedListBlock
import time
from notion.block import TextBlock
from notion.block import ToggleBlock
import datetime
# <editor-fold desc="get credentials and auth">
reddit_credentials_path = '/Users/ysenkiv/Code/access files/personal/reddit/reddit auth.txt'

with open(reddit_credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    client_id = lines[0].strip()
    client_secret = lines[1].strip()
    username = lines[2].strip()
    password = lines[3].strip()

reddit = praw.Reddit(
    user_agent="Comment Extraction (by u/USERNAME)",
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password)

notion_credentials_path = '/Users/ysenkiv/Code/access files/personal/notion/token_v2.txt'
with open(notion_credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    token_v2 = lines[0].strip()
client = NotionClient(token_v2=token_v2)
# </editor-fold>
# <editor-fold desc="reddit variables">
url = 'https://www.reddit.com/r/Fire/comments/qphl2s/a_subreddit_which_focuses_on_people_who_wish_to/'
# url = "https://www.reddit.com/r/passive_income/comments/lm1vnc/comment/gnspihn/"
submission = reddit.submission(url=url)
submission.comment_sort = "top"
submission.comments.replace_more(limit=None)
# </editor-fold>
# <editor-fold desc="notion veriables">
page = client.get_block('https://www.notion.so/slavkosenkiv/test-page-6c252540395e433f83d3cd21dabfad9f')
# notion_table = client.get_collection_view("https://www.notion.so/slavkosenkiv/a805791e57204b63a4480712d06c824a?v=5538526eae9943f5a28210eb06ec1ecd")
# row = notion_table.collection.add_row()
# </editor-fold>
# <editor-fold desc="functions">


def unix_to_human_time(comment):
    human_time = datetime.datetime.utcfromtimestamp(int(comment.created_utc)).strftime('%d.%m.%y')
    return human_time


def is_op(comment):
    if comment.is_submitter:
        return 'is OP'
    return ''


# </editor-fold>


go_deep()







