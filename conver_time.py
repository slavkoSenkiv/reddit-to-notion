import re
post_url = 'https://www.reddit.com/r/Fire/comments/qphl2s/a_subreddit_which_focuses_on_people_who_wish_to/'
comment_url = 'https://www.reddit.com/r/passive_income/comments/lm1vnc/warren_buffett_says_if_you_dont_find_a_way_to/gnspihn/?context=3'

post_id_pattern = re.compile(r'/comments/[a-z0-9]{6}/')
match_object = post_id_pattern.search(post_url)
post_is = match_object.group()[10:16]
print(post_is)


comment_id_pattern = re.compile(r'/[a-z0-9]{7}/\?')
match_object1 = comment_id_pattern.search(comment_url)
comment_id = match_object1.group()[1:8]
print(comment_id)
