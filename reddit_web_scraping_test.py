import praw
import pandas as pd

# Read-only instance
reddit_read_only = praw.Reddit(client_id="omIBLzu_LMSI8biSbuJL7w",         # your client id
                               client_secret="psbeJ8BdtXlhVRVTYe5qVum37Z13SQ",      # your client secret
                               user_agent="siddhibansal9")        # your user agent
 
# Authorized instance
reddit_authorized = praw.Reddit(client_id="omIBLzu_LMSI8biSbuJL7w",         # your client id
                                client_secret="psbeJ8BdtXlhVRVTYe5qVum37Z13SQ",      # your client secret
                                user_agent="siddhibansal9",        # your user agent
                                username="siddhibansal9",        # your reddit username
                                password="Convergent@123")        # your reddit password

reddit_read_only = praw.Reddit(client_id="omIBLzu_LMSI8biSbuJL7w",		 # your client id
							client_secret="psbeJ8BdtXlhVRVTYe5qVum37Z13SQ",	 # your client secret
							user_agent="siddhibansal9")	 # your user agent


subreddit = reddit_read_only.subreddit("redditdev")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)
subreddit = reddit_read_only.subreddit("Python")

for post in subreddit.hot(limit=5):
	print(post.title)
	print()

posts = subreddit.top(time_filter="month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
			"ID": [], "Score": [],
			"Total Comments": [], "Post URL": []
			}

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
	
	# Text inside a post
	posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["ID"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
	# Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
	
	# URL of each post
	posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts

top_posts.to_csv("Top Posts.csv", index=True)
