import json
import re
import os


def load_pairs():
    thai_eng_dict = {} 
    regex_thai = '<a href=\'/id/[0-9]+\'>()</a>'
    regex_eng = '<td>([A-Za-z]+)</td>'
    regexH = '.*?\.html'
    thai = re.compile(regex_thai, flags = re.DOTALL)
    eng = re.compile(regex_eng, flags = re.DOTALL)
    file_tree = os.walk('/thai_pages')
    for root, dirs, files in file_tree:
        for f in files:
            file_name = f.find(regexH)
            with open(file_name, 'r', encoding = 'utf-8') as file:
                html = file.read()
                thai_words = thai.findall(html)
                eng_words = eng.findall(html)
                thai_eng_dict[thai_words] = eng_words
                                                                                                 
    
def write_json():
    with open('thai_eng_dict.txt', 'w', encoding = 'utf-8') as file:
        file.write(json.load(thai_eng_dict), ensure_ascii=False)

        
def main():
    if __name__ == '__main__':
        main()              



































