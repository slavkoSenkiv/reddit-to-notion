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
url = 'https://www.reddit.com/r/Python/comments/qon3cz/i_made_a_spotify_playlist_downloader/'
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


def get_comment_info(comment):
    comment_text = comment.body.replace('\n', '')
    comment_time = unix_to_human_time(comment)
    text = f"{comment.score} | {comment_text}\n" \
           f"{comment.author} {is_op(comment)}>{comment_time}\n"
    return text


def add(level, comment, block_type=NumberedListBlock):
    child = level.children.add_new(block_type, title=get_comment_info(comment))
    return child


def go_deep():
    for reply_0 in submission.comments:
        if isinstance(reply_0, MoreComments):
            continue
        note_1 = add(page, reply_0, ToggleBlock)

        for reply_1 in reply_0.replies:
            if isinstance(reply_1, MoreComments):
                continue
            note_2 = add(note_1, reply_1)

            for reply_2 in reply_1.replies:
                if isinstance(reply_2, MoreComments):
                    continue
                note_3 = add(note_2, reply_1)

                for reply_3 in reply_2.replies:
                    if isinstance(reply_3, MoreComments):
                        continue
                    note_4 = add(note_3, reply_1)

                    for reply_4 in reply_3.replies:
                        if isinstance(reply_4, MoreComments):
                            continue
                        note_5 = add(note_4, reply_1)
# </editor-fold>


go_deep()







