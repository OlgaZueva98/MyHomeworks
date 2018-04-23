import urllib.request
import json
import matplotlib
import matplotlib.pyplot as plt
import re


def load_posts():
    count_num = 200
    posts = []
    post_texts = []
    while len(posts) < count_num:
        req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-33744144&count=100&offset=1&v=5.74&access_token=480a3a47480a3a47480a3a475b4868bdb04480a480a3a4712d6f5432d8eb5412cfb33f5') 
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        data = json.loads(result)
        posts += data['response']['items']
        with open('post_texts.txt', 'w', encoding = 'utf-8') as f:
            for post in posts:
                post_texts = [post['text']]
                for t in post_texts:
                    f.write(t + '\n#\n')

    return posts, post_texts
  
def load_comments(posts):
    count_num = 200
    comments = [[] for post in posts]
    users_id = []
    for idx, item in enumerate(posts):
        while len(comments[idx]) < count_num:
            req = urllib.request.Request('https://vk.com/dev/wall.getComments?owner_id=-33744144&post_id=posts[idx]&count=100&extended=1&v=5.74&access_token=480a3a47480a3a47480a3a475b4868bdb04480a480a3a4712d6f5432d8eb5412cfb33f5')
            response = urllib.request.urlopen(req)
            result = response.read().decode('utf-8', 'ignore')
            data = json.loads(result)
            comments += data['response']['items']
            with open ('comm_texts.txt', 'w', encoding = 'utf-8') as f:
                for comm in comments:
                    comm_texts = [comm['text']]
                    for c in comm_texts:
                        f.write(c + '\n#\n')
            for user in comments:
                user_id = [user['from_id']]
                users_id.append(user_id)
    return comments, comm_texts, users_id


def post_comm_length(post_texts, comm_texts):
    length = {}
    post_length = []
    comm_length = []
    for idx, text in enumerate(post_texts):
        text = text.split()
        post_length.append(len(text))
    for idx, comm in enumerate(comm_texts):
        comm = comm.split()
        comm_length.append(len(comm))
    length[post_length] = comm_length

    with open('length.txt', 'w', encoding = 'utf-8') as f:
        f.write(length)

    return length, post_length, comm_length


def average_length(comm_texts):
    for idx, comm in enumerate(comm_text, 1):
        if len(comm_text[idx]) != 0:
            aver_length = len(comm_text.split())//len(comm_text[idx])
    return aver_length

def corr_graph(post_length, aver_length):
    plt.scatter(post_length, aver_length)
    plt.title('Соотношение длины поста со средней длиной комментариев')
    plt.ylabel('Средняя длина комментариев')
    plt.xlabel('Длина поста')
    plt.savefig('corr_graph', dpi='300', format='png')
    plt.close()
    
def users_inf(users_id):
    cities = []
    bdates = []
    ages = []
    req = urllib.request.Request('https://api.vk.com/method/users.get?v=5.74&user_ids={}&fields=home_town,bdate'.format(str(users_id)))
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    if 'home_town' not in (data['response'][0]):
        continue
    else:
        cities.append(data['response'][0]['home_town'])
    if bdate not in data['response']:
        continue
    else:
        bdates.append(data['response']['bdate'])

    regex = re.compile('[1|2][0|9][(0|1)|(3-9)][0-9]')
    bd_year = re.search(regex, bdates)
    if bd_year:
        ages.append(2018 - int(bd_year))
    else:
        ages.append('-')
    return cities, ages     
        
    
def main():
    posts, post_texts = load_posts()
    comments, comm_texts, users_id = load_comments(posts)
    length, post_length, comm_length = post_comm_length(post_texts, comm_texts)
    aver_length = average_length(comm_texts)
    corr_graph(post_length, aver_length)
    cities, ages = users_inf(users_id)

if __name__ == '__main__':
    main()
