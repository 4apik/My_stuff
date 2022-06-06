import requests
import pygal

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code:', r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' + 
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {'title': response_dict['title'], 
                        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
                        'comments': response_dict.get('descendants', 0)}
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)


names, plot_dicts = [], []
#print("\nSelected information about each repository:")
for repo_dict in submission_dicts:
    names.append(repo_dict['title'])
    plot_dict = {'value': repo_dict['comments'], 
                 'xlink': repo_dict['link']}
    plot_dicts.append(plot_dict)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config)
chart.title = "Number of comments on HN discussions"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file("comments_chart.svg")
