class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

class Mahasiswa(Orang):
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"
    
    def __init__(self, nama_depan, nama_belakang, nomer_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")

class Karyawan(Orang):
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.status_karyawan = status_karyawan

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_id, status_karyawan)
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)
rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
rizki.mengajar("Statistik")

class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        Orang.__init__(self, nama_depan, nama_belakang, nomer_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

print("Data Mahasiswa:")
print("Nama:", bowo.nama_depan, bowo.nama_belakang)
print("Nomor ID:", bowo.nomer_id)
print("Jenjang:", bowo.jenjang)
print("Mata Kuliah yang Diambil:", bowo.matkul)

print("\nData Dosen:")
print("Nama:", rizki.nama_depan, rizki.nama_belakang)
print("Nomor ID:", rizki.nomer_id)
print("Status Karyawan:", rizki.status_karyawan)
print("Mata Kuliah yang Diajar:", rizki.matkul_diajar)

print("\nData Asdos:")
print("Nama:", uswatun.nama_depan, uswatun.nama_belakang)
print("Nomor ID:", uswatun.nomer_id)
print("Mata Kuliah yang Diambil:", uswatun.matkul)
print("Mata Kuliah yang Diajar:", uswatun.matkul_diajar)
