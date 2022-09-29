import datetime
import requests
import json
import os
import arxiv
from github import Github

def get_authors(authors, first_author = False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output

def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output    

def get_daily_papers(max_results=400):
    content = dict() 
    content_to_web = dict()

    # content
    output = dict()
    
    search_engine = arxiv.Search(
        query = "cat:astro-ph.EP",
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    count = 0
    today = datetime.date.today()
    dir = "./daily_papers/"+str(today.year) + "/" + str(today.month) + "/"
    try:
        os.makedirs(dir)
    except(FileExistsError):
        print("Made directory")

    file = dir+str(today.day)+".md"

    with open(file,"a+") as f:
        f.write("## ASTRO.PH.EP " + str(today) + "\n\n")

    for result in search_engine.results():
        paper_id            = result.get_short_id()
        paper_title         = result.title
        paper_url           = result.entry_id
        paper_abstract      = result.summary.replace("\n"," ")
        paper_authors       = get_authors(result.authors)
        paper_first_author  = get_authors(result.authors,first_author = True)
        primary_category    = result.primary_category
        publish_time        = result.published.date()
        update_time         = result.updated.date()
        comments            = result.comment

        print("Time = ", update_time ,
              " title = ", paper_title,
              " author = ", paper_first_author)
        if ((today - update_time).days > 1):
            continue

      
        print("Time = ", update_time ,
              " title = ", paper_title,
              " author = ", paper_first_author)
        
        
        file = dir+str(today.day)+".md"

        with open(file,"a+") as f:
            f.write("|Title | Authors | PDF Link | \n")
            f.write("|:-----------------------|:---------|:------|\n")
            f.write("|"+str(paper_title)+"|"+str(paper_first_author)+" et al.|"+str(paper_url)+"|\n")
            f.write(f"\n")
            f.write("### Abstract\n")
            f.write(paper_abstract)
            f.write("\n ### Key Points: \n")
            #Add: back to top
            top_info = f"## ASTROPHEP-" + str(today)
            f.write(f"<p align=right>(<a href={top_info}>back to top</a>)</p>\n\n")

    # data = {topic:content}
    # data_web = {topic:content_to_web}
    # return data,data_web \

get_daily_papers()