import pandas as pd
from jinja2 import Environment, FileSystemLoader

user_nick = 'justonlyfun'

liked_posts = pd.read_csv(f"parsed_data/{user_nick}/liked_posts.csv", sep=",")
created_posts = pd.read_csv(f"parsed_data/{user_nick}/created_posts.csv", sep=",")
reposted_posts = pd.read_csv(f"parsed_data/{user_nick}/reposted_posts.csv", sep=",")
comments = pd.read_csv(f"parsed_data/{user_nick}/comments.csv", sep=",")

environment = Environment(loader=FileSystemLoader('templates'))

template_name = "report_template.html"
template = environment.get_template(template_name)
context = {
    "user": "Alexey Ortin",
    "liked_posts": liked_posts.to_dict('records'),
    "created_posts": created_posts.to_dict('records'),
    "reposted_posts": reposted_posts.to_dict('records'),
    "comments": comments.to_dict('records'),
}

file_path = f"reports/report-{user_nick}.html"

with open(file_path, mode="w", encoding="utf-8") as results:
    results.write(template.render(context))
    print(f"... wrote {file_path}")