#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI


def spaces(n):
    print('\n' * n)

    
def get_content():

    comment = input('Insert text: ')
    title = input('Insert title: ')
    description = input('Insert description: ')
    site = input('Insert URL site: ')
    image = input('Insert URL image: ')

    return comment, title, description, site, image


def publish_text_on_profile(access_token, post_text):
	linkedin = PyLinkedinAPI(access_token)
	data = linkedin.publish_profile_comment(post_text)
	spaces(1)
	print(data)


def publish_content_on_profile(access_token):
    linkedin = PyLinkedinAPI(access_token)
    comment, title, description, site, image = get_content()

    data = linkedin.publish_profile(comment,
                                    title=title,
                                    description=description,
                                    submitted_url=site,
                                    submitted_image_url=image)

    spaces(1)
    print(data)	