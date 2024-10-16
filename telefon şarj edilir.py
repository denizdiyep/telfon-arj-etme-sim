import time

def telefon_sarj_et():
    print("Telefon şarj etme işlemi başlatılıyor...")
    
    # Başlangıç şarj durumu
    sarj_durumu = 0
    max_sarj = 100  # Maksimum şarj seviyesi
    
    while sarj_durumu < max_sarj:
        print(f"Şarj durumu: {sarj_durumu}%")
        time.sleep(5)  # 5 saniye bekleme süresi
        sarj_durumu += 20  # Her seferinde %20 şarj ekle

        # Şarj tamamlandığında mesaj ver
        if sarj_durumu >= max_sarj:
            sarj_durumu = max_sarj  # Son değeri maksimuma ayarla
            print(f"Şarj durumu: {sarj_durumu}%")
            print("Telefon tamamen şarj oldu!")

# Telefon şarj etme simülasyonunu başlat
telefon_sarj_et()
