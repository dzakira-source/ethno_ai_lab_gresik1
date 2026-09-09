import tkinter as tk
from tkinter import ttk, messagebox
import math
import time

# Ethno-AI Inclusive Lab - Wilayah Gresik
# Aplikasi Lab Sains Virtual untuk ABK (Hambatan Intelektual Class 4 SD)

class EthnoAIGresikApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ETHNO-AI INCLUSIVE LAB - KEARIFAN LOKAL GRESIK")
        self.root.geometry("900x650")
        self.root.configure(bg="#F0F9FF")

        # Data Tanaman Obat Keluarga (TOGA) Khas Gresik
        self.toga_gresik = {
            "sirih": {
                "nama": "Daun Sirih Gresik",
                "ikon": "🍃",
                "warna": "#22C55E",
                "khasiat": "Obat pembersih alami & penyembuh luka.",
                "kearifan_lokal": "Masyarakat pesisir Gresik menggunakannya untuk tradisi nginang dan obat gusi.",
                "suara": "Halo Cah Gresik! Ini Daun Sirih. Aromanya wangi, rasanya hangat, cocok untuk obat alami!"
            },
            "pandan": {
                "nama": "Daun Pandan Sidayu",
                "ikon": "🌿",
                "warna": "#16A34A",
                "khasiat": "Pewangi makanan & penenang alami.",
                "kearifan_lokal": "Sering dipakai dalam jajanan tradisional khas Gresik seperti Pudak dan Pudak Pandan.",
                "suara": "Wah, harum sekali! Ini Daun Pandan Sidayu Gresik. Harumnya buat kue Pudak jadi lezat!"
            },
            "mengkudu": {
                "nama": "Daun Mengkudu / Pace",
                "ikon": "🌱",
                "warna": "#15803D",
                "khasiat": "Menurunkan tekanan darah & meredakan batuk.",
                "kearifan_lokal": "Di pedesaan Gresik, daun mudanya biasa diolah jadi botok mengkudu sehat.",
                "suara": "Iki Daun Pace/Mengkudu Gresik! Banyak manfaatnya untuk kesehatan tubuh kita."
            }
        }

        self.selected_plant = None
        self.setup_ui()

    def setup_ui(self):
        # Header / Banner
        header = tk.Frame(self.root, bg="#0284C7", height=80)
        header.pack(fill="x")
        
        lbl_title = tk.Label(header, text="🌟 ETHNO-AI LAB GRESIK 🌟", font=("Helvetica", 22, "bold"), fg="white", bg="#0284C7")
        lbl_title.pack(pady=5)
        
        lbl_subtitle = tk.Label(header, text="Lab Sains Inklusif ABK - Pindai Tanaman Obat & Koding Gambar", font=("Helvetica", 12), fg="#E0F2FE", bg="#0284C7")
        lbl_subtitle.pack()

        # Main Layout (Left: Scan AI, Right: Output & Koding)
        main_frame = tk.Frame(self.root, bg="#F0F9FF")
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Left Panel (Scan AI Tangible)
        left_panel = tk.LabelFrame(main_frame, text=" 📸 1. PINDAI TANAMAN OBA (TANGIBLE AI) ", font=("Helvetica", 12, "bold"), fg="#0369A1", bg="#FFFFFF", bd=3, relief="groove")
        left_panel.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        lbl_instruct = tk.Label(left_panel, text="Tunjukkan Daun Asli di Depan Kamera:", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#334155")
        lbl_instruct.pack(pady=10)

        # Tombol Pilihan Daun Besar (Ramah Motorik ABK)
        btn_frame = tk.Frame(left_panel, bg="#FFFFFF")
        btn_frame.pack(pady=10)

        btn_sirih = tk.Button(btn_frame, text="🍃 DAUN SIRIH", font=("Helvetica", 13, "bold"), bg="#DCFCE7", fg="#15803D", activebackground="#86EFAC", height=2, width=18, command=lambda: self.scan_plant("sirih"))
        btn_sirih.pack(pady=8)

        btn_pandan = tk.Button(btn_frame, text="🌿 DAUN PANDAN", font=("Helvetica", 13, "bold"), bg="#DCFCE7", fg="#15803D", activebackground="#86EFAC", height=2, width=18, command=lambda: self.scan_plant("pandan"))
        btn_pandan.pack(pady=8)

        btn_mengkudu = tk.Button(btn_frame, text="🌱 DAUN MENGKUDU", font=("Helvetica", 13, "bold"), bg="#DCFCE7", fg="#15803D", activebackground="#86EFAC", height=2, width=18, command=lambda: self.scan_plant("mengkudu"))
        btn_mengkudu.pack(pady=8)

        # Simulasi Kamera Frame
        self.cam_frame = tk.Frame(left_panel, bg="#E2E8F0", width=250, height=150, bd=2, relief="sunken")
        self.cam_frame.pack(pady=15)
        self.cam_frame.pack_propagate(False)

        self.lbl_cam = tk.Label(self.cam_frame, text="[ Kamera Siap Scan... ]", font=("Helvetica", 10, "italic"), bg="#E2E8F0", fg="#64748B")
        self.lbl_cam.pack(expand=True)

        # Right Panel (Respon Maskot & Koding Simbolis)
        right_panel = tk.LabelFrame(main_frame, text=" 🎭 2. RESPO MASKOT GRESIK & KODING GAMBAR ", font=("Helvetica", 12, "bold"), fg="#0369A1", bg="#FFFFFF", bd=3, relief="groove")
        right_panel.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        # Display Respon
        self.display_frame = tk.Frame(right_panel, bg="#FEF9C3", bd=2, relief="solid")
        self.display_frame.pack(fill="x", padx=10, pady=10)

        self.lbl_maskot = tk.Label(self.display_frame, text="🐥 Maskot Damar Kurung Cilik", font=("Helvetica", 14, "bold"), bg="#FEF9C3", fg="#854D0E")
        self.lbl_maskot.pack(pady=5)

        self.lbl_info = tk.Label(self.display_frame, text="Pilih/pindai daun di sebelah kiri untuk memulai eksperimen!", font=("Helvetica", 11), bg="#FEF9C3", fg="#1E293B", wraplength=350, justify="center")
        self.lbl_info.pack(pady=10)

        # Koding Simbolis (Picture Coding)
        lbl_koding = tk.Label(right_panel, text="🧩 Blok Koding Simbolis Sederhana:", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#334155")
        lbl_koding.pack(pady=(10, 5))

        coding_box = tk.Frame(right_panel, bg="#F1F5F9", bd=1, relief="solid")
        coding_box.pack(fill="x", padx=10, pady=5)

        lbl_block1 = tk.Label(coding_box, text="[ 📷 KAMERA SCAN ] ➔ [ 🌿 AI TEGUR DAUN ] ➔ [ 📢 MASKOT BERSUARA ]", font=("Helvetica", 10, "bold"), bg="#3B82F6", fg="white", padx=10, pady=8)
        lbl_block1.pack(pady=10)

        # Tombol Aksi Koding
        self.btn_play_sound = tk.Button(right_panel, text="🔊 DENGARKAN SUARA MASKOT", font=("Helvetica", 12, "bold"), bg="#FDE047", fg="#713F12", activebackground="#FEF08A", height=2, command=self.play_sound)
        self.btn_play_sound.pack(fill="x", padx=10, pady=8)

        # Footer Status
        footer = tk.Frame(self.root, bg="#0284C7", height=30)
        footer.pack(fill="x", side="bottom")
        lbl_foot = tk.Label(footer, text="Modul Eksperimen IPAS SD Inklusif - Kembangkan Karakter Bernalar Kritis & Cinta Budaya Gresik", font=("Helvetica", 9), fg="white", bg="#0284C7")
        lbl_foot.pack(pady=3)

    def scan_plant(self, key):
        self.selected_plant = self.toga_gresik[key]
        plant = self.selected_plant
        
        # Update Kamera Frame Simulation
        self.cam_frame.configure(bg=plant["warna"])
        self.lbl_cam.configure(text=f"BERHASIL DIPINDAI!\n{plant['ikon']} {plant['nama']}", font=("Helvetica", 12, "bold"), fg="white", bg=plant["warna"])

        # Update Display Info
        info_text = f"✨ TANAMAN TERDETEKSI! ✨\n\n📌 Nama: {plant['nama']}\n💡 Khasiat: {plant['khasiat']}\n🏛️ Kearifan Gresik: {plant['kearifan_lokal']}"
        self.lbl_info.configure(text=info_text, fg="#0F172A", font=("Helvetica", 11, "bold"))
        self.display_frame.configure(bg="#DCFCE7")
        self.lbl_maskot.configure(bg="#DCFCE7", fg="#14532D", text=f"🐥 Maskot Gresik: 'Hebat, Cah Gresik!'")

    def play_sound(self):
        if not self.selected_plant:
            messagebox.showinfo("Petunjuk Guru", "Silakan minta siswa memindai/menekan salah satu daun terlebih dahulu, ya!")
        else:
            plant = self.selected_plant
            messagebox.showinfo("Suara Maskot Ethno-AI", f"📢 MASKOT BERSUARA:\n\n\"{plant['suara']}\"")

if __name__ == "__main__":
    root = tk.Tk()
    app = EthnoAIGresikApp(root)
    root.mainloop()
