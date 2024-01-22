window.location.href = "https://www.facebook.com";
import webbrowser

url = "https://www.facebook.com"
webbrowser.open(url)
