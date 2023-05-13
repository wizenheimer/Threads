import requests


def check_link_rot(url):
    """
    Checks whether the given URL has a link rot.
    Link rot refers to the phenomenon where hyperlinks on the internet become outdated or broken over time.
    """
    try:
        response = requests.head(url)
        if response.status_code == requests.codes.ok:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False
