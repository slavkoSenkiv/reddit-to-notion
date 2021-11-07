import praw
from praw.models import MoreComments
from notion.client import NotionClient
from notion.block import TextBlock
import datetime
import re

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
url = 'https://www.reddit.com/r/passive_income/comments/lm1vnc/warren_buffett_says_if_you_dont_find_a_way_to/'
# url = "https://www.reddit.com/r/passive_income/comments/lm1vnc/comment/gnspihn/"
submission = reddit.submission(url=url)
submission.comment_sort = "top"
submission.comments.replace_more(limit=None)
# </editor-fold>
comments_num = 0
text = ''
# <editor-fold desc="notion veriables">
notion_table = client.get_collection_view("https://www.notion.so/slavkosenkiv/a805791e57204b63a4480712d06c824a?v=5538526eae9943f5a28210eb06ec1ecd")
row = notion_table.collection.add_row()
# </editor-fold>

# <editor-fold desc="functions">


def is_op(comment):
    if comment.is_submitter:
        return 'is OP'
    return ''


def unix_to_human_time(comment):
    human_time = datetime.datetime.utcfromtimestamp(int(comment.created_utc)).strftime('%d.%m.%y')
    return human_time


def print_comment(comment, indent):
    global comments_num
    global text
    comment_text = comment.body.replace('\n', '')
    comment_time = unix_to_human_time(comment)
    comments_num += 1
    text += f"{'|   ' * indent}{comment_text} \n" \
            f"{'|   ' * indent}{comment.score} {comment_time} {comment.author} {is_op(comment)} {comment.id}\n"
    row.children.add_new(TextBlock, title=text)


def go_deep():
    for reply_0 in submission.comments:
        if isinstance(reply_0, MoreComments):
            continue
        print_comment(reply_0, 0)
        for reply_1 in reply_0.replies:
            if isinstance(reply_1, MoreComments):
                continue
            print_comment(reply_1, 1)
            for reply_2 in reply_1.replies:
                if isinstance(reply_2, MoreComments):
                    continue
                print_comment(reply_2, 2)
                for reply_3 in reply_2.replies:
                    if isinstance(reply_3, MoreComments):
                        continue
                    print_comment(reply_3, 3)
                    for reply_4 in reply_3.replies:
                        if isinstance(reply_4, MoreComments):
                            continue
                        print_comment(reply_4, 4)
                        for reply_5 in reply_4.replies:
                            if isinstance(reply_5, MoreComments):
                                continue
                            print_comment(reply_5, 5)
                            for reply_6 in reply_5.replies:
                                if isinstance(reply_6, MoreComments):
                                    continue
                                print_comment(reply_6, 6)
                                for reply_7 in reply_6.replies:
                                    if isinstance(reply_7, MoreComments):
                                        continue
                                    print_comment(reply_7, 7)
                                    for reply_8 in reply_7.replies:
                                        if isinstance(reply_8, MoreComments):
                                            continue
                                        print_comment(reply_8, 8)
                                        for reply_9 in reply_8.replies:
                                            if isinstance(reply_9, MoreComments):
                                                continue
                                            print_comment(reply_9, 9)
                                            for reply_10 in reply_9.replies:
                                                if isinstance(reply_10, MoreComments):
                                                    continue
                                                print_comment(reply_10, 10)
                                                for reply_11 in reply_10.replies:
                                                    if isinstance(reply_11, MoreComments):
                                                        continue
                                                    print_comment(reply_11, 11)
                                                    for reply_12 in reply_11.replies:
                                                        if isinstance(reply_12, MoreComments):
                                                            continue
                                                        print_comment(reply_12, 12)


def comment_properties_migration():
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
    row.subreddit = str(submission.subreddit)
    row.comments = submission.num_comments
    row.score = submission.score
    row.created = datetime.datetime.utcfromtimestamp(int(submission.created_utc)).date()
    row.author = str(submission.author)
    row.link = f'https://www.reddit.com{submission.permalink}'


# </editor-fold>


if '/gnspihn/' in url:
    saved_comment_id = reddit.comment(url=url)
    text += comment_properties_migration()
    go_deep()
    start_of_the_comment = saved_comment_id.body
    rest_of_the_comment = text.split(start_of_the_comment)[1]
    text += start_of_the_comment + rest_of_the_comment
else:
    post_properties_migration()

go_deep()
# row.children.add_new(TextBlock, title=text)









