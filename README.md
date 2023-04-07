# Boruvka

İlk önce bu kod, verilen bir metin ve bir kelime listesi ile metindeki kelime tekrar sayılarını hesaplayan bir fonksiyon olan "boruvka()" fonksiyonunu içerir.

Değişkenler:

"text": hesaplanacak kelime tekrarları olan metin.
"words": hesaplanacak kelimelerin listesi.
"edges": metindeki kelime dizilerinin tutulduğu kenar listesi.
"nodes": metindeki tüm kelime pozisyonlarını tutan küme.
"components": kelime pozisyonlarını tutan bileşenlerin listesi.


Algoritma Açıklaması:

İlk olarak, tüm kelime dizilerinin pozisyonları kenar olarak edges listesine eklenir ve metindeki tüm kelime pozisyonları nodes kümesine eklenir.
Sonra nodes kümesi sıralanır ve her bir kelime pozisyonu, o bileşenin adı olan components adlı bir sözlüğe atanır.
Daha sonra, bileşenlerin sayısı 1'den büyük olduğu sürece döngü devam eder.
Her turda, komponentler 2'li gruplar halinde alınır ve minimum ağırlığa sahip olan kenarlar components sözlüğündeki yeni bileşenlere eklenir.
Daha sonra, kelime dizilerinin tekrar sayılarını hesaplamak için "words" listesindeki her kelime için, kelime pozisyonları, componentlerin değerleri ile karşılaştırılır ve her kelime için tekrar sayısı bir sözlük olan "result" sözlüğüne eklenir.
Son olarak, fonksiyon "result" sözlüğünü döndürür.


Çalışma Zamanı Analizi:

İlk döngü, metnin boyutuna ve kelime listesinin boyutuna bağlı olarak O(N*M) olabilir.
Node'ların sıralanması O(NlogN) kadar sürer.
Döngüdeki "while" döngüsü O(N*M) kadar sürer.
Sözlük işlemleri, eklemeler ve aramalar O(1) sürer.
"result" sözlüğünün oluşturulması, metnin uzunluğuna ve kelime sayısına bağlı olarak O(N*M) kadar sürer.
Bu nedenle, toplam zaman karmaşıklığı O(NM) + O(NlogN) + O(NM) + O(1) + O(NM) = O(NM*logN) dir.
"shift-or" ve "boruvka" algoritmaları hakkında yeterli bilgi sağladım. Başka bir sorunuz var mı?
