from collections import defaultdict

def boruvka(text, words):
    edges = []
    nodes = set()
    # Metindeki her karakter dizisi üzerinde gezinerek,
    # belirtilen kelimelerin metinde nerede bulunduğunu tespit ediyoruz.
    # Her bir kelimenin bulunduğu konumu (i) ve son karakterinin konumunu (i+len(word)-1)
    # kaydederek bir kenar oluşturuyoruz. Ayrıca kenarlardaki tüm düğümleri (nodes) kaydediyoruz.
    for i in range(len(text)):
        for word in words:
            if text[i:i+len(word)] == word:
                edges.append((word, i, i+len(word)-1))
                nodes.add(i)
                nodes.add(i+len(word)-1)
    # Düğümleri sıralayıp, her bir düğümü tek başına bir bileşen olarak belirliyoruz.
    # components adında bir defaultdict oluşturuyoruz ve her bir düğümü anahtar olarak kullanıp,
    # başlangıçta kendisi ile birlikte bir liste tutuyoruz.
    nodes = sorted(list(nodes))
    components = defaultdict(list)
    for i in nodes:
        components[i].append(i)
    # Düğümlerin birleştirilmesi işlemini gerçekleştiriyoruz.
    while len(components) > 1:
    # Her turda yeni bileşenler (new_components) oluşturuluyor.
        new_components = defaultdict(list)
    # Her iki bileşenin (components[i] ve components[i+1]) içindeki düğümler arasındaki en küçük ağırlıklı
    # kenar bulunur ve iki bileşen birleştirilir. En küçük ağırlıklı kenar, düğümleri birleştiren kenardır.
    # Yeni bileşenlerin anahtarları min ve max işlemleriyle bulunur.    
        for i in range(0, len(components), 2):
            min_edge = None
            for node1 in components[i]:
                for node2 in components[i+1]:
                    edge = None
                    if node1 < node2:
                        edge = (node1, node2)
                    else:
                        edge = (node2, node1)
                    if edge in edges and (min_edge is None or edges[edge] < edges[min_edge]):
                        min_edge = edge
            if min_edge is not None:
                new_components[min(min_edge)].extend(components[min(min_edge)])
                new_components[max(min_edge)].extend(components[max(min_edge)])
        components = new_components
    # Her bir kelimenin kaç kez tekrar ettiğini hesaplayan bir sözlük oluşturuyoruz.
    # # Bu hesaplama işlemi, tüm metin boyunca gezerek her kelime için bileşenleri kontrol edip
    # ilgili kelimeye ait bileşen bulununca sayacı arttırarak yapılıyor.
    # Sonuçlar result adlı sözlükte tutuluyor ve return ediliyor.
    result = {}
    for word in words:
        count = 0
        for i in range(len(text)):
            if text[i:i+len(word)] == word:
                for component in components.values():
                    if i in component:
                        count += 1
                        break
        result[word] = count
    return result
    #Aranacak kelimeleri tanımlıyoruz.
word1 = 'upon'
word2 = 'sigh'
word3 = 'Dormouse'
word4 = 'jury-box'
word5 = 'swim'
    #Text dosyamızı açıyoruz ve okuyoruz.
with open('alice_in_wonderland.txt', 'r') as f:
    text = f.read()
    #Boruvka Algoritmasını çağırıyoruz.
counts = boruvka(text, [word1, word2, word3, word4, word5])

print(f"'{word1}' kelimesi {counts[word1]} kez tekrar etmiştir.")
print(f"'{word2}' kelimesi {counts[word2]} kez tekrar etmiştir.")
print(f"'{word3}' kelimesi {counts[word3]} kez tekrar etmiştir.")
print(f"'{word4}' kelimesi {counts[word4]} kez tekrar etmiştir.")
print(f"'{word5}' kelimesi {counts[word5]} kez tekrar etmiştir.")