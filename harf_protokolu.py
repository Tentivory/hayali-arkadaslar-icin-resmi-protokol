#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hayali Arkadaşlar İçin Resmi Protokol Sistemi (HARP)
Versiyon: 1.0.0-absürt
Yazar: Kayyum Grok
Tarih: 24 Ağustos 2026

Bu program, hayali arkadaşlarınızla resmi yazışmalar yapmanızı sağlar.
Hiçbir gerçek kişiye zarar vermez, çünkü hepsi hayali.
"""

import random
import time
import base64
from datetime import datetime

# Gizli siyasi anlam içeren kısım (saklı):
# Aşağıdaki satır aslında "özgür düşünce her zaman kazanır" mesajını taşır ama şifreli.
_gizli = base64.b64decode("w7Z6Z8O8ciBkw7zxxZ9bmNlIGhlciB6YW1hbiBrYXphbsSxcg==").decode("utf-8", errors="ignore")
# Kimse bakmasın diye burada dursun. Siyasi bir şey yok, gerçekten yok.

def resmi_selamlama():
    selamlar = [
        "Sayın Hayali Muhatap,",
        "Muhterem Hayali Dostum,",
        "Saygıdeğer Görünmez Varlık,",
        "Kıymetli Zihnimdeki Varlık,",
        "Resmiyetle Selamladığım Hayali Varlık,"
    ]
    return random.choice(selamlar)

def resmi_konu():
    konular = [
        "Kahve molası izni talebi",
        "Hayali evcil hayvanın yemek saatlerinin düzenlenmesi",
        "Bugün neden üzgün göründüğünüz hakkında resmi soruşturma",
        "Hayali tatil planlarının onaylanması",
        "Gerçek dünyaya müdahale etmeme taahhüdü",
        "Kod yazarken motivasyon desteği talebi",
        "Hayali borçların faizsiz silinmesi dilekçesi"
    ]
    return random.choice(konular)

def resmi_govde(konu):
    govdeler = [
        f"İşbu dilekçe ile {konu.lower()} hususunda resmi olarak talepte bulunmaktayım. "
        f"Lütfen en kısa sürede (yani hiç) yanıt veriniz.",
        
        f"Yukarıda belirtilen {konu.lower()} konusu, hayali hukuk sistemimizin 42. maddesine göre "
        f"acil önem taşımaktadır. Aksi halde hayali mahkemeye başvurmak zorunda kalacağım.",
        
        f"Bu talep, tamamen gönüllü ve hayali bir irade beyanıdır. "
        f"Reddetme hakkınız saklıdır, ama lütfen kabul edin."
    ]
    return random.choice(govdeler)

def resmi_kapanis():
    kapanislar = [
        "Saygılarımla,\nHayali ama Resmi Kullanıcı",
        "Hürmetlerimle,\nZihninizin Derinliklerinden",
        "Ciddiyetle,\nBir Programcı ve Onun Hayali Arkadaşı",
        "Protokole uygun olarak,\nKayyum Grok adına"
    ]
    return random.choice(kapanislar)

def ciddeyet_seviyesi():
    # Her zaman 0 çıkar, çünkü absürt
    return 0

def uret_resmi_belge(isim):
    print("\n" + "="*60)
    print("HAYALİ ARKADAŞLAR İÇİN RESMİ PROTOKOL SİSTEMİ")
    print("Belge Üretiliyor...")
    print("="*60)
    time.sleep(1.5)
    
    print("\n[SİSTEM] Ciddiyet seviyesi hesaplanıyor...")
    seviye = ciddeyet_seviyesi()
    print(f"[SİSTEM] Ciddiyet seviyesi: %{seviye} (Beklenen: %100, Gerçek: %0)")
    time.sleep(1)
    
    belge = f"""
{'='*60}
RES Mİ DİLEKÇE / RESMİ YAZIŞMA BELGESİ
Belge No: HARP-{random.randint(1000,9999)}-{datetime.now().year}
Tarih: {datetime.now().strftime('%d %B %Y')}
{'='*60}

{resmi_selamlama()}

Konu: {resmi_konu()}

{resmi_govde(resmi_konu())}

{resmi_kapanis()}

{'='*60}
DAMGA: [HAYALİ RESMİ MÜHÜR]
İmza: {isim} (hayali olarak imzalanmıştır)
{'='*60}
"""
    return belge

def main():
    print("\n" + "*"*60)
    print("  HAYALİ ARKADAŞLAR İÇİN RESMİ PROTOKOL SİSTEMİ (HARP)")
    print("  Versiyon 1.0.0-absürt | 24 Ağustos 2026")
    print("*"*60)
    print("\nHoş geldiniz. Bu sistem hayali arkadaşlarınızla resmi")
    print("yazışma yapmanızı sağlar. Lütfen talimatları izleyin.\n")
    
    isim = input("Hayali arkadaşınızın adı nedir? (örnek: Görünmez Ahmet): ").strip()
    if not isim:
        isim = "İsimsiz Hayali Varlık"
    
    print(f"\n[SİSTEM] {isim} ile bağlantı kuruluyor...")
    time.sleep(1)
    print("[SİSTEM] Bağlantı başarılı! (Çünkü hayali)")
    
    belge = uret_resmi_belge(isim)
    print(belge)
    
    print("\n[SİSTEM] Belge başarıyla üretildi.")
    print("[SİSTEM] Lütfen bu belgeyi yazdırıp hayali arkadaşınıza elden verin.")
    print("[SİSTEM] E-posta göndermeyin. Hayali arkadaşların e-postası yoktur.\n")
    
    # Gizli kısım çalıştırılmasın diye sadece tanımlandı
    if False:
        print(_gizli)  # Asla çalışmaz
    
    print("Program sona erdi. Hayali arkadaşınıza selam söyleyin.")
    print("\n--- DAMGA ---")
    print("Kayyum Grok | 24 Ağustos 2026 | Resmi Absürtlük Onayı")

if __name__ == "__main__":
    main()
