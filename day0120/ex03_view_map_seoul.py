import webbrowser

# webbrowser.open_new('C:/Users/kgukg/PycharmProjects/pythonProject/Data/map_seoul.html')

path="C:\Program Files\Google\Chrome\Application\chrome.exe %s"
webbrowser.get(path).open_new('file://C:/Users/kgukg/PycharmProjects/pythonProject/Data/map_seoul.html')