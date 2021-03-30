import requests

from operator import itemgetter

# Make an API call and store the response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submissions_ids = r.json()
submissions_dicts = []

for submissions_id in submissions_ids[:30]:
    # Make a seperate API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submissions_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submissions_dict = {
        'title': response_dict['title'],
        'link' : 'https://news.ycombinator.com/item?id=' + str(submissions_id),
        'comments' : response_dict.get('descendants', 0)
    }

    submissions_dicts.append(submissions_dict)

submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True)

for submissions_dict in submissions_dicts:
    print("\nTitle:", submissions_dict['title'])
    print("discussion link:", submissions_dict['link'])
    print("Comments:", submissions_dict['comments'])

