#! python3
# reddit_saved_to_csv.py - Exports your saved Posts and Comments on Reddit to a csv file.
import praw, csv, codecs

reddit_credentials_path = '/Users/ysenkiv/Code/access files/personal/reddit/reddit auth.txt'

with open(reddit_credentials_path) as credentials_file:
    lines = credentials_file.readlines()
    client_id = lines[0].strip()
    client_secret = lines[1].strip()
    username = lines[2].strip()
    password = lines[3].strip()

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='Saved posts scraper by /u/' + username,
                     username=username,
                     password=password)

reddit_home_url = 'https://www.reddit.com'

saved_models = reddit.user.me().saved(limit=None) # models: Comment, Submission

reddit_saved_csv = codecs.open('reddit_saved.csv', 'w', 'utf-8') # creating our csv file

# CSV writer for better formatting
saved_csv_writer = csv.writer(reddit_saved_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
saved_csv_writer.writerow(['ID', 'Name', 'Subreddit', 'Type', 'URL', 'NoSFW']) # Column names


def handle(saved_models):
    count = 1
    for model in saved_models:
        subreddit = model.subreddit # Subreddit model that the Comment/Submission belongs to
        subr_name = subreddit.display_name
        url = reddit_home_url + model.permalink

        if isinstance(model, praw.models.Submission): # if the model is a Submission
            title = model.title
            noSfw = str(model.over_18)
            model_type = "#Post"
        else: # if the model is a Comment
            title = model.submission.title
            noSfw = str(model.submission.over_18)
            model_type = "#Comment"

        print('Model number ' + str(count) + ' is written to csv file.')
        saved_csv_writer.writerow([str(count), title, subr_name, model_type, url, noSfw])

        count += 1


handle(saved_models)
reddit_saved_csv.close()

print("\nCOMPLETED!")
print("Your saved posts are available in reddit_saved.csv file.")
