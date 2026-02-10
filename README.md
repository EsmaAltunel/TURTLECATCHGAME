# **Catch The Turtle (Python)**

Bu proje, Python'ın **Turtle Graphics** kütüphanesi kullanılarak geliştirilmiş, refleks tabanlı eğlenceli bir "kaplumbağa yakalama" oyunudur. Programlama temellerini ve olay tabanlı (event-driven) mantığı kavramak amacıyla geliştirilmiştir.

## **🎮 Oyunun Amacı**
Ekranda rastgele beliren ve hızla kaybolan kaplumbağayı 20 saniye içinde en çok kez tıklayarak yakalamaya çalışın. Her yakalama size +1 puan kazandırır!

## **Özellikler**

Proje şu temel programlama konseptlerini içerir:

### **1. Olay Yönetimi (Event Handling)**
* **Tıklama Kontrolü:** `t.onclick(handle_click)` fonksiyonu ile her kaplumbağanın tıklanabilir bir nesneye dönüştürülmesi.
* **Zamanlayıcılar:** `turtle.ontimer` kullanılarak hem kaplumbağaların yer değiştirmesi hem de geri sayım sisteminin eşzamanlı çalıştırılması.



### **2. Grafiksel Arayüz (GUI)**
* **Dinamik Skor Tablosu:** Oyuncunun yakaladığı kaplumbağa sayısının anlık olarak güncellenmesi.
* **Geri Sayım Sistemi:** 20 saniyeden geriye akan ve süre bittiğinde oyunu sonlandıran zamanlayıcı.
* **Görsel Tasarım:** "Light pink" arka plan ve özel turtle şekilleri ile basit ama etkili bir görsel sunum.

### **3. Algoritmik Yapı**
* **Rastgelelik:** `random.choice` ile kaplumbağa listesinden rastgele birinin seçilerek ekranda gösterilmesi.
* **Optimizasyon:** `turtle.tracer(0)` ve `turtle.tracer(1)` kullanılarak animasyonların daha akıcı olması sağlanmıştır.
