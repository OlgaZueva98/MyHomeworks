import sys
import gensim, logging
import urllib.request
import networkx as nx
import matplotlib.pyplot as plt 


def download_model():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    urllib.request.urlretrieve('http://rusvectores.org/static/models/rusvectores2/ruscorpora_mystem_cbow_300_2_2015.bin.gz', 'ruscorpora_mystem_cbow_300_2_2015.bin.gz')

    m = 'ruscorpora_mystem_cbow_300_2_2015.bin.gz'
    if m.endswith('.vec.gz'):
        model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
    elif m.endswith('.bin.gz'):
        model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
    else:
        model = gensim.models.KeyedVectors.load(m)

    model.init_sims(replace=True)
    return model


def sem_field(model):
    words = ['красный_A', 'алый_A', 'багровый_A', 'багряный_A', 'пунцовый_A']
    red_G = nx.Graph()
    red_G.add_nodes_from(words)
    for node_word in words:
        for word in words:
            if word in model:
                cos_dist = model.similarity(node_word, word)
                if cos_dist > 0.5:
                    red_G.add_edge(node_word, word)
                else:
                    print(word + ' is not present in the model')
    print('узлы', red_G.nodes())
    print('рёбра', red_G.edges())
    return red_G


def create_graph(red_G):
    pos=nx.spring_layout(red_G)
    nx.draw_networkx_nodes(red_G, pos, node_color='black', node_size=30)
    nx.draw_networkx_edges(red_G, pos, edge_color='purple')
    nx.draw_networkx_labels(red_G, pos, font_size=10, font_family='Arial')
    plt.axis('off')
    plt.show()

    #самые центральные слова
    centr_words = []
    deg_centr_words = nx.degree_centrality(red_G)
    for nodeid in sorted(deg_centr_words, key=deg_centr_words.get, reverse=True):
        centr_words.append(nodeid)
    print('Самые центральные слова графа:' + str(centr_words[0]) + ',' + str(centr_words[1]) + '.')

    #радиус графа
    print('Радиус графа:' + str(nx.radius(red_G)))

    #коэффициент кластеризации
    print('Коэффициент кластеризации:' + str(nx.average_clustering(red_G)))
    print(nx.transitivity(red_G))
      
def main():
    model = download_model()
    red_G = sem_field(model)
    create_graph(red_G)
    

if __name__ == '__main__':
    main()



      
