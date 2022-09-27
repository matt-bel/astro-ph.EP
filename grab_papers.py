import datetime
import requests
import json
import os
import arxiv


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

def get_daily_papers(max_results=20):
    """
    @param topic: str
    @param query: str
    @return paper_with_code: dict
    """

    # output 
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

    #     # eg: 2108.09112v1 -> 2108.09112
    #     ver_pos = paper_id.find('v')
    #     if ver_pos == -1:
    #         paper_key = paper_id
    #     else:
    #         paper_key = paper_id[0:ver_pos]    

    #     try:
    #         r = requests.get(code_url).json()
    #         # source code link
    #         if "official" in r and r["official"]:
    #             count += 1
    #             repo_url = r["official"]["url"]
    #             content[paper_key] = f"|**{update_time}**|**{paper_title}**|{paper_first_author} et.al.|[{paper_id}]({paper_url})|**[link]({repo_url})**|\n"
    #             content_to_web[paper_key] = f"- {update_time}, **{paper_title}**, {paper_first_author} et.al., Paper: [{paper_url}]({paper_url}), Code: **[{repo_url}]({repo_url})**"

    #         else:
    #             content[paper_key] = f"|**{update_time}**|**{paper_title}**|{paper_first_author} et.al.|[{paper_id}]({paper_url})|null|\n"
    #             content_to_web[paper_key] = f"- {update_time}, **{paper_title}**, {paper_first_author} et.al., Paper: [{paper_url}]({paper_url})"

    #         # TODO: select useful comments
    #         comments = None
    #         if comments != None:
    #             content_to_web[paper_key] = content_to_web[paper_key] + f", {comments}\n"
    #         else:
    #             content_to_web[paper_key] = content_to_web[paper_key] + f"\n"

    #     except Exception as e:
    #         print(f"exception: {e} with id: {paper_key}")

    # data = {topic:content}
    # data_web = {topic:content_to_web}
    # return data,data_web \

get_daily_papers()