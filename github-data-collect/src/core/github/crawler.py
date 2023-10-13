import csv

from github import Github
from config.environments import FIRST_TOKEN_GITHUB, INITIAL_USER

# Authenticate with your GitHub access token
g = Github(FIRST_TOKEN_GITHUB)

# Get the user object for the user you want to check
user = g.get_user(INITIAL_USER)

# Get the list of users that the specified user is following
following = user.get_following()

# Create a CSV file to store the user information
csv_filename = "./data/initial_users_data.csv"

# Define the header for the CSV file
csv_header = [
    "Nome de usuário",
    "ID",
    "AvatarURL",
    "GravatarID",
    "URL",
    "HTMLURL",
    "FollowersURL",
    "FollowingURL",
    "GistsURL",
    "StarredURL",
    "SubscriptionsURL",
    "OrganizationsURL",
    "ReposURL",
    "EventsURL",
    "ReceivedEventsURL",
    "Type",
    "SiteAdmin",
    "Name",
    "Company",
    "Blog",
    "Location",
    "Email",
    "Hireable",
    "Bio",
    "PublicRepos",
    "PublicGists",
    "Followers",
    "Following",
    "CreatedAt",
    "UpdatedAt",
    "Following Users",
    "Followers Users",
]

# Open the CSV file and write the header
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_header)

    # Write the user information for each user in the following list
    for user in following:
        following_users = [u.login for u in user.get_following()]
        followers_users = [u.login for u in user.get_followers()]
        
        user_info = [
            user.login,
            user.id,
            user.avatar_url,
            user.gravatar_id,
            user.url,
            user.html_url,
            user.followers_url,
            user.following_url,
            user.gists_url,
            user.starred_url,
            user.subscriptions_url,
            user.organizations_url,
            user.repos_url,
            user.events_url,
            user.received_events_url,
            user.type,
            user.site_admin,
            user.name,
            user.company,
            user.blog,
            user.location,
            user.email,
            user.hireable,
            user.bio,
            user.public_repos,
            user.public_gists,
            len(followers_users),
            len(following_users),
            user.created_at,
            user.updated_at,
            ", ".join(following_users),  # Combine following users into a string
            ", ".join(followers_users),  # Combine followers users into a string
        ]
        writer.writerow(user_info)

print(f"User information saved to {csv_filename}")