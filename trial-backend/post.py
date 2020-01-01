import webbrowser
def search(term):
   url = "https://www.google.com.tr/search?q={}".format(term)
   webbrowser.open_new_tab(url)
