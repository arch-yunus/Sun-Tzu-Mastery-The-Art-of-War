import time
import random

class MasteryEngine:
    """
    Sun-Tzu Mastery: Taktiksel Simülasyon Motoru (v2.0)
    Modern Mühendislik ve Strateji Senaryolarını Analiz Eder.
    """
    
    def __init__(self, team_name):
        self.team_name = team_name
        self.stats = {
            "tao": 50,      # Vizyon Birliği
            "shi": 50,      # Momentum
            "resource": 100, # Lojistik/Kaynak
            "xu": 0         # Düşman Zayıflığı
        }
        self.turn = 1

    def log(self, msg, type="INFO"):
        prefix = "[🏮 MASTER]" if type == "INFO" else "[⚠️ KRİTİK]"
        print(f"{prefix} {msg}")

    def simulate_scenario(self, choice):
        print(f"\n--- Tur {self.turn} ---")
        if choice == 1: # Agresif İnovasyon (Qi)
            self.log("Asimetrik saldırı başlatılıyor (Doktrin V)...")
            self.stats["shi"] += 20
            self.stats["resource"] -= 30
            self.stats["xu"] += 10
        elif choice == 2: # Sistemsel Güçlendirme (Via Negativa)
            self.log("Sistem sertleştirme yapılıyor (Doktrin IV)...")
            self.stats["tao"] += 15
            self.stats["resource"] -= 10
            self.stats["shi"] -= 5
        elif choice == 3: # İstihbarat ve OSINT
            self.log("İstihbarat toplanıyor (Doktrin XIII)...")
            self.stats["xu"] += 30
            self.stats["tao"] -= 5

        self.turn += 1
        self.report()

    def report(self):
        print("-" * 30)
        for stat, val in self.stats.items():
            print(f"{stat.upper():<10}: {'█' * (val // 10)} ({val})")
        print("-" * 30)

        if self.stats["resource"] <= 0:
            self.log("Lojistik tükendi! Geri çekilme emri (Doktrin II).", "ALERT")
            return False
        if self.stats["shi"] >= 90 and self.stats["xu"] >= 50:
            self.log("ZAFER: Savaşmadan fethedildi! (Doktrin III).", "INFO")
            return False
        return True

def main():
    print("🐉 SUN-TZU MASTERY SIMULATOR v2.0")
    name = input("Ekip/Proje Adı: ")
    engine = MasteryEngine(name)
    
    active = True
    while active:
        print("\nSTRATEJİK SEÇENEKLER:")
        print("1. Asimetrik İnovasyon (Qi - Enerji Artırır)")
        print("2. Sistem Sertleştirme (Savunma - Tao Artırır)")
        print("3. İstihbarat Toplama (Casusluk - Rakip Zayıflığı Bulur)")
        print("4. Çıkış")
        
        try:
            cmd = int(input("> "))
            if cmd == 4: break
            active = engine.simulate_scenario(cmd)
        except ValueError:
            print("Geçersiz komut.")

if __name__ == "__main__":
    main()
