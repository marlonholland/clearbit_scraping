import requests as rq
import os


def img_scraper(img_urls=[], size='128', local_dir='test'):
    """ 
    A function that utilizes the clearbit API found here: https://logo.clearbit.com/<URL>

    Parameters: 
    img_urls (list): A list of URL's you want to grab icons from
    size (string): The pixel size you want your logo to be
    local_dir (string): The location you want to save your logo.
    """

    if not os.path.isdir(local_dir):
        os.mkdir(local_dir)
    for index, url in enumerate(img_urls):
        r = rq.get(f'https://logo.clearbit.com/{url}?size = {size}')
        with open(local_dir + '/' + str(index+1) + '.jpg', 'wb+') as f:
            f.write(r.content)
        f.close()

