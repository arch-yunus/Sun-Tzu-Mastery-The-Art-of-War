import sys

def calculate_opex_impact(velocity, cloud_cost, team_burn_rate, months=12):
    """
    Doktrin II (Zuo Zhan) temel alınarak; projenin sürat (velocity) ile 
    maliyet (burn rate) arasındaki sürdürülebilirlik analizi.
    """
    total_cost = (cloud_cost + team_burn_rate) * months
    efficiency = velocity / (total_cost / 1000) # Değer başına maliyet indeksi
    
    return total_cost, efficiency

def main():
    print("Sun-Tzu Mastery: Kaynak Optimizasyonu (v1.0)")
    print("-" * 50)
    
    try:
        velocity = float(input("Proje Yayılım Hızı (Deployment/Hafta): "))
        cloud_cost = float(input("Aylık Bulut Maliyeti ($): "))
        team_burn_rate = float(input("Aylık Ekip Maliyeti ($): "))
    except ValueError:
        print("Geçersiz değer. Lütfen sayısal veriler girin.")
        sys.exit(1)
        
    total, eff = calculate_opex_impact(velocity, cloud_cost, team_burn_rate)
    
    print(f"\n[ANALİZ]")
    print(f"- 12 Aylık Tahmini Harcama: ${total:,.2f}")
    print(f"- Verimlilik Katsayısı: {eff:.4f}")
    
    print("\n[DOKTRİN YORUMU]")
    if eff > 0.5:
        print(">>> Sürat, maliyeti domine ediyor. 'Becerikli Hız' prensibi devrede.")
    elif eff > 0.2:
        print(">>> Denge durumu. Uzun süren savaş (proje) kaynakları tüketebilir.")
    else:
        print(">>> KRİTİK: Kaynak tüketimi hızı aşıyor. Lojistik (maliyet) operasyonu bitirebilir.")

if __name__ == "__main__":
    main()
