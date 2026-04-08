import argparse
import sys

def calculate_victory_probability(scores):
    """
    Sun Tzu'nun 7 Karşılaştırması (The 7 Comparisons) temel alınarak 
    hesaplanan stratejik üstünlük skoru.
    """
    weights = {
        "tao": 0.25,        # Ahlaki Yasa / Vizyon Birliği
        "commander": 0.20,  # Liderlik Yetkinliği
        "heaven_earth": 0.15, # Pazar ve Altyapı Koşulları
        "discipline": 0.15,  # Süreç ve Disiplin (CI/CD, CRM vb.)
        "logistics": 0.15,   # Kaynak ve Lojistik Gücü
        "training": 0.10     # Yetkinlik ve Eğitim
    }
    
    total_score = sum(scores[k] * weights[k] for k in weights)
    return total_score

def main():
    print("Sun-Tzu Mastery: Stratejik Hesaplama Araci (v1.0)")
    print("-" * 50)
    
    parser = argparse.ArgumentParser(description='Stratejik Üstünlük Hesaplayıcı')
    parser.add_argument('--tao', type=float, required=True, help='Vizyon Birliği (1-10)')
    parser.add_argument('--commander', type=float, required=True, help='Liderlik Gücü (1-10)')
    parser.add_argument('--heaven_earth', type=float, required=True, help='Çevresel Koşullar (1-10)')
    parser.add_argument('--discipline', type=float, required=True, help='Süreç Disiplini (1-10)')
    parser.add_argument('--logistics', type=float, required=True, help='Lojistik Gücü (1-10)')
    parser.add_argument('--training', type=float, required=True, help='Ekip Yetkinliği (1-10)')

    args = parser.parse_args()
    
    scores = vars(args)
    result = calculate_victory_probability(scores)
    
    print(f"\n[SONUÇ] Stratejik Üstünlük Katsayısı: {result:.2f} / 10.00")
    
    if result >= 8.5:
        print(">>> DURUM: Tam Hakimiyet. Saldırı için mükemmel zaman.")
    elif result >= 6.5:
        print(">>> DURUM: Üstünlük sizde. Stratejik manevralar ile güç kazanın.")
    elif result >= 4.5:
        print(">>> DURUM: Denge. Doğrudan savaştan kaçının, dolaylı (Qi) metodlara odaklanın.")
    else:
        print(">>> DURUM: Kritik Zayıflık. Savunmaya çekilin ve 'Büyük Hesaplama'yı yeniden yapın.")

if __name__ == "__main__":
    main()
