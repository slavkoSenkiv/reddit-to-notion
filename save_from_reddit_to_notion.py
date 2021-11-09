import praw
import datetime
import re
from praw.models import MoreComments
from notion.client import NotionClient
from notion.block import NumberedListBlock
from notion.block import TextBlock
from notion.block import ToggleBlock

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
reddit_content_url = 'https://www.reddit.com/r/Fire/comments/qphl2s/a_subreddit_which_focuses_on_people_who_wish_to/'
submission = reddit.submission(url=reddit_content_url)
submission.comment_sort = "top"
submission.comments.replace_more(limit=None)
# </editor-fold>

# <editor-fold desc="notion veriables">
table_url = "https://www.notion.so/slavkosenkiv/a805791e57204b63a4480712d06c824a?v=5538526eae9943f5a28210eb06ec1ecd"
notion_table = client.get_collection_view(table_url)
row = notion_table.collection.add_row()
# </editor-fold>

text = ''
# <editor-fold desc="functions">


def is_op(comment):
    if comment.is_submitter:
        return 'is OP'
    return ''


def get_reddit_content_type(url=reddit_content_url):
    if 'context=3' not in url:  # is it post?
        return 'post'
    if 'context=3' in url:  # is it comment/reply?
        return 'branch'


def get_content_piece_id(url=reddit_content_url):
    if get_reddit_content_type() == 'post':
        post_id_pattern = re.compile(r'/comments/[a-z0-9]{6}/')
        match_object = post_id_pattern.search(url)
        post_id = match_object.group()[10:16]
        return post_id
    if get_reddit_content_type() == 'branch':
        comment_id_pattern = re.compile(r'/[a-z0-9]{7}/\?')
        match_object1 = comment_id_pattern.search(url)
        comment_id = match_object1.group()[1:8]
        return comment_id


def unix_to_human_time(comment):
    human_time = datetime.datetime.utcfromtimestamp(int(comment.created_utc)).strftime('%d.%m.%y')
    return human_time


def get_comment_info(comment):
    comment_text = comment.body.replace('\n', '')
    comment_time = unix_to_human_time(comment)
    text = f"{comment.score} | {comment_text}\n" \
           f"{comment.author} {is_op(comment)}>{comment_time}\n"
    return text


def add_child(level, comment, block_type=NumberedListBlock):
    child = level.children.add_new(block_type, title=get_comment_info(comment))
    return child


def append_text(comment, indent):
    global text
    comment_text = comment.body.replace('\n', '')
    comment_time = unix_to_human_time(comment)
    text += f"{'|   ' * indent}{comment.score}-{comment_text} {comment_time} {comment.author} {is_op(comment)}\n"


def comment_properties_migration():
    row.title = submission.title
    row.type = get_reddit_content_type()
    row.subreddit = str(submission.subreddit)
    row.score = get_content_piece_id().score
    row.comments = submission.num_comments
    row.author = str(submission.author)
    row.created = datetime.datetime.utcfromtimestamp(int(submission.created_utc)).date()
    row.link = f'https://www.reddit.com{submission.permalink}'

    return f'''this is saved submission comment or reply, not submission itself
        submission title: {submission.title}
        subreddit: {submission.subreddit}
        comment score: {saved_comment_id.score}
        comment created: {unix_to_human_time(saved_comment_id)}
        comment author: {saved_comment_id.author}
        comment text: {saved_comment_id.body}
        link: https://www.reddit.com{saved_comment_id.permalink}'''


def post_properties_migration():
    row.title = submission.title
    row.type = get_reddit_content_type()
    row.subreddit = str(submission.subreddit)
    row.score = submission.score
    row.comments = submission.num_comments
    row.author = str(submission.author)
    row.created = datetime.datetime.utcfromtimestamp(int(submission.created_utc)).date()
    row.link = f'https://www.reddit.com{submission.permalink}'


def go_deep_and_add_children():
    for reply_0 in submission.comments:
        if isinstance(reply_0, MoreComments):
            continue
        note_1 = add_child(row, reply_0, ToggleBlock)

        for reply_1 in reply_0.replies:
            if isinstance(reply_1, MoreComments):
                continue
            note_2 = add_child(note_1, reply_1)

            for reply_2 in reply_1.replies:
                if isinstance(reply_2, MoreComments):
                    continue
                note_3 = add_child(note_2, reply_1)

                for reply_3 in reply_2.replies:
                    if isinstance(reply_3, MoreComments):
                        continue
                    note_4 = add_child(note_3, reply_1)

                    for reply_4 in reply_3.replies:
                        if isinstance(reply_4, MoreComments):
                            continue
                        note_5 = add_child(note_4, reply_1)


def go_deep_and_append_text():
    for reply_0 in submission.comments:
        if isinstance(reply_0, MoreComments):
            continue
        append_text(reply_0, 0)
        for reply_1 in reply_0.replies:
            if isinstance(reply_1, MoreComments):
                continue
            append_text(reply_1, 1)
            for reply_2 in reply_1.replies:
                if isinstance(reply_2, MoreComments):
                    continue
                append_text(reply_2, 2)
                for reply_3 in reply_2.replies:
                    if isinstance(reply_3, MoreComments):
                        continue
                    append_text(reply_3, 3)
                    for reply_4 in reply_3.replies:
                        if isinstance(reply_4, MoreComments):
                            continue
                        append_text(reply_4, 4)
                        for reply_5 in reply_4.replies:
                            if isinstance(reply_5, MoreComments):
                                continue
                            append_text(reply_5, 5)


# </editor-fold>

save_format = '1'  # input('1 - faster but simple text\n2 - longer but organized toggle:\n')

if 'context=3' not in reddit_content_url:  # is it post?
    if save_format == '1':
        post_properties_migration()
        go_deep_and_append_text()
        row.children.add_new(TextBlock, title=text)
    if save_format == '2':
        post_properties_migration()
        go_deep_and_add_children()
if 'context=3' in reddit_content_url:  # is it comment/reply?
    pass









