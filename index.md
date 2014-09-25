---
layout: page
title: Hello World!
tagline: LIFE NOTEs
---
{% include JB/setup %}

## NOTEs LIST

My blog!!

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## My Journey On Map

<!-- [Tour Tracking on Google Map](https://mapsengine.google.com/map/edit?mid=zw4FUKSEFMDQ.ke6qqKluFO9U) -->

<!-- <iframe src="https://mapsengine.google.com/map/embed?mid=zw4FUKSEFMDQ.ke6qqKluFO9U" width="640" height="480"></iframe> -->

<iframe src="https://mapsengine.google.com/map/embed?mid=zw4FUKSEFMDQ.ke6qqKluFO9U" width=100% height="480"></iframe>
