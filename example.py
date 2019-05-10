from nyt_comments import retrieve_comment_json, comment_body_list
'''
A sample of what it does.
You probably want to run it over a loop of articles. 
You might also store the fields you want in a CSV file for later use or export.
'''
article_url='https://www.nytimes.com/2019/04/20/business/boeing-dreamliner-production-problems.html'#  URL of the article you want to get
comments=retrieve_comment_json(article_url) #grab comments

comment_texts = comment_body_list(comments) #grab text

with open("comments.txt", "w") as file:
    for comment in comment_texts: #loop through the list
        file.write(comment) #write comment to file 

