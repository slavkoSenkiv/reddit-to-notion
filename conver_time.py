# <editor-fold desc="Description">
from praw.models import MoreComments
import praw
import re

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

# reddit_content_url = 'https://www.reddit.com/r/Fire/comments/qphl2s/a_subreddit_which_focuses_on_people_who_wish_to/'
reddit_content_url = 'https://www.reddit.com/r/Fire/comments/qphl2s/comment/hjufomf/?utm_source=share&utm_medium=web2x&context=3'
submission = reddit.submission(url=reddit_content_url)
# </editor-fold>


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


def check_find_and_print_comment(comment):
    print(comment.id)
    print(comment.body.replace('\n', ''))
    if comment.id == get_content_piece_id():
        print('yes we got comment id, the comment is ')
        print(comment.body.replace('\n', ''))


print(submission.title)
print(submission.selftext.replace('\n', ''))
print(submission.id)
print(submission.score)

for comment in submission.comments:
    check_find_and_print_comment(comment)
    for reply1 in comment.replies:
        check_find_and_print_comment(reply1)
        for reply2 in comment.replies:
            check_find_and_print_comment(reply2)
            for reply3 in comment.replies:
                check_find_and_print_comment(reply3)
                for reply4 in comment.replies:
                    check_find_and_print_comment(reply4)




