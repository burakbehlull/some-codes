# pip install instaloader

import instaloader

loader = instaloader.Instaloader()

profile_name = input("Instagram Username: ")

loader.download_profile(profile_name, profile_pic_only=True)
