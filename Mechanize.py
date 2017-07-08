import mechanize
br = mechanize.Browser();
br.set_handle_robots(False);
br.open('https://www.google.com');
for f in br.forms():
    print f 