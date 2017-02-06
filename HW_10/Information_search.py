import urllib.request
import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for at in attrs:
                if at[0].upper() == 'TITLE':
                    if at[1].upper().find('ЯЗЫК') == -1:
                        write_in_file(at[1]+'\n')
                           
        
def search_capital():
    data = ''
    f = open('Россия — Википедия.html', 'r', encoding = 'utf-8')
    for r in f:
        if (r.startswith('<p>')) and (r.upper().find('TITLE=\"СТОЛИЦА\">СТОЛИЦА<')>-1):
            data = data + r
    f.close()
    
    myparser = MyHTMLParser()
    myparser.feed(data)
    myparser.close()
        

def write_in_file(text):
    f = open('Capital.txt', 'a', encoding='utf-8')
    f.write(text)
    f.close()
    
def main():
    search_capital()
    
if __name__ == "__main__":
    main()

#<p><a href="/wiki/%D0%A1%D1%82%D0%BE%D0%BB%D0%B8%D1%86%D0%B0" title="Столица">Столица</a>&#160;— <a href="/wiki/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0" title="Москва">Москва</a>. <a href="/wiki/%D0%9E%D1%84%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA" title="Официальный язык">Государственный язык</a>&#160;— <a href="/wiki/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA" title="Русский язык">русский</a>.<span class="noprint" title="#Языки" style="margin-left: 3px;"><a href="#.D0.AF.D0.B7.D1.8B.D0.BA.D0.B8" title="#Языки"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/45/Arrow_Blue_Right_001.svg/10px-Arrow_Blue_Right_001.svg.png" width="10" height="10" style="vertical-align: baseline" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/45/Arrow_Blue_Right_001.svg/15px-Arrow_Blue_Right_001.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/45/Arrow_Blue_Right_001.svg/20px-Arrow_Blue_Right_001.svg.png 2x" data-file-width="100" data-file-height="100" /></a></span></p>
