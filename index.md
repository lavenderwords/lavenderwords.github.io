---
layout: page
title: Hello World!
tagline: LIFE NOTEs 
---
{% include JB/setup %}

## NOTEs LIST

My blog!!

<ul class="posts">
    <li class="forkme"><div><iframe src="http://markdotto.github.com/github-buttons/github-btn.html?user=plusjade&repo=jekyll-bootstrap&type=fork&count=true"
                                    allowtransparency="true" frameborder="0" scrolling="0" width="95px" height="20px"></iframe></div></li>

  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## My Journey On Map

[Tour Tracking on Google Map](https://mapsengine.google.com/map/edit?mid=zw4FUKSEFMDQ.ke6qqKluFO9U)


