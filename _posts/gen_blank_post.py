# this program generate a post for jekyll automatically
import time

name = ""
category = ""
tags = [""]

content = '''---
layout: post
'''
content += "category : " + category
content += '''
tagline: ""
comments: true
'''
i = len(tags)
content += "tags : ["
for tag in tags:
    content += tag
    i -= 1
    if i > 0:
        content += ","
content += "]"
content += '''
---

'''

def gen_post(name, post_content, t = time.localtime()):
    post_name = time.strftime("%Y-%m-%d",t)+"-"+name
    f = open(post_name,"w")
    f.write(post_content)
    f.close()

def parse_name(origin_name):
    name_list = origin_name.split()
    return '-'.join(name_list)+".md"

gen_post(parse_name(name),content)
