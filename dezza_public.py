import hashlib
import time
import sys

# KONFIGURASI PUBLIK
# Alamat ini adalah identitas tujuan pengamanan (Aman disebar)
ALAMAT_TUJUAN = "DZ_3235a5af047d3fe0711a"
VERSI_NODE = "1.0.0-Public"

def mulai_validasi():
    print(f"==========================================")
    print(f"🛡️  DEZZA LAYER - PUBLIC NODE VALIDATOR")
    print(f"Version: {VERSI_NODE}")
    print(f"Membantu Jaringan: {ALAMAT_TUJUAN}")
    print(f"==========================================")
    print("Status: Menghubungkan ke Algoritma Master...")
    time.sleep(2)
    print("✅ Terhubung! Mulai mempertebal lapisan keamanan...\n")

    lapis_terhitung = 0
    start_time = time.time()

    try:
        while True:
            # Mengambil data timestamp terbaru untuk keunikan blok
            timestamp = str(time.time())
            # Data yang dihitung menggabungkan alamat kamu dan usaha (nonce)
            data_mentah = ALAMAT_TUJUAN + timestamp + str(lapis_terhitung)
            
            # Proses Hashing SHA-256 (Jantung Kriptografi)
            hash_result = hashlib.sha256(data_mentah.encode()).hexdigest()

            # Syarat Lapis Keamanan (mencari hash yang diawali '000')
            if hash_result.startswith("000"):
                lapis_terhitung += 1
                current_time = time.strftime("%H:%M:%S")
                
                print(f"[{current_time}] ✨ LAPIS BERHASIL DIKUNCI!")
                print(f" -> Hash: {hash_result[:32]}...")
                print(f" -> Total Kontribusi: {lapis_terhitung} Lapis")
                print(f"------------------------------------------")
                
                # Jeda tipis agar CPU perangkat pembantu tidak overheat
                time.sleep(0.5) 

    except KeyboardInterrupt:
        durasi = round((time.time() - start_time) / 60, 2)
        print(f"\n[!] Node Berhenti.")
        print(f"📊 Total kontribusi kamu: {lapis_terhitung} lapis dalam {durasi} menit.")
        sys.exit()

if __name__ == "__main__":
    mulai_validasi()
