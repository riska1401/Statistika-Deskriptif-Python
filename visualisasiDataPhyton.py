import pandas as pd
import matplotlib.pyplot as plt

# 1. Membaca file excel
path = "riska.xlsx"
dataraw = pd.read_excel(path)

print("--- DATA AWAL ---")
print(dataraw)

# 2. Tabel Frekuensi
datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")
print("\n--- TABEL FREKUENSI ---")
print(datafrq)

# 3. VISUALISASI DATA (TAMPILAN MODERN & KONTINU)

# a. LINE CHART
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_facecolor('#f8fafc')
ax.plot(
    datafrq.index, 
    datafrq["Frekuensi"], 
    color="#4f46e5", 
    marker="o", 
    markersize=9, 
    markerfacecolor="#06b6d4", 
    markeredgecolor="#ffffff", 
    markeredgewidth=2, 
    linewidth=3, 
    linestyle="-",
    label="Tren Mahasiswa"
)
ax.fill_between(range(len(datafrq)), datafrq["Frekuensi"], color="#4f46e5", alpha=0.12)
ax.set_title("DISTRIBUSI FREKUENSI PEROLEHAN GRADE", fontsize=13, fontweight="bold", pad=15, color="#1e293b")
ax.set_xlabel("Kategori Grade", fontweight="bold", labelpad=10, color="#334155")
ax.set_ylabel("Jumlah Mahasiswa", fontweight="bold", labelpad=10, color="#334155")
ax.grid(True, linestyle="--", alpha=0.5, color="#cbd5e1")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()

# b. BAR CHART
neon_colors = ["#10b981", "#06b6d4", "#3b82f6", "#f59e0b", "#f97316", "#ef4444"]
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_facecolor('#f8fafc')
bars = ax.bar(
    datafrq.index, 
    datafrq["Frekuensi"], 
    color=neon_colors[:len(datafrq)], 
    edgecolor="#0f172a", 
    linewidth=1.2, 
    width=0.55
)

for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2, 
        yval + 0.25, 
        f"{int(yval)} Mhs", 
        ha='center', 
        va='bottom', 
        fontweight='bold', 
        fontsize=10, 
        color="#0f172a"
    )

ax.set_title("SEBARAN JUMLAH MAHASISWA PER GRADE", fontsize=13, fontweight="bold", pad=15, color="#1e293b")
ax.set_xlabel("Grade", fontweight="bold", labelpad=10, color="#334155")
ax.set_ylabel("Frekuensi", fontweight="bold", labelpad=10, color="#334155")
ax.set_ylim(0, max(datafrq["Frekuensi"]) + 2)
ax.grid(axis="y", linestyle=":", alpha=0.6, color="#94a3b8")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(rotation=0, fontweight="bold")
plt.tight_layout()
plt.show()

# c. PIE CHART
donut_colors = ["#10b981", "#06b6d4", "#3b82f6", "#f59e0b", "#f97316", "#ef4444"]
explode = [0.05] * len(datafrq)

fig, ax = plt.subplots(figsize=(7, 6))
wedges, texts, autotexts = ax.pie(
    datafrq["Frekuensi"],
    labels=datafrq.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=donut_colors[:len(datafrq)],
    explode=explode,
    pctdistance=0.75,
    wedgeprops=dict(width=0.45, edgecolor='#ffffff', linewidth=2),
    shadow=True
)

for t in texts:
    t.set_fontsize(11)
    t.set_fontweight('bold')
    t.set_color('#1e293b')

for at in autotexts:
    at.set_fontsize(10)
    at.set_fontweight('bold')
    at.set_color('#ffffff')

ax.set_title("PROPORSI KELULUSAN MAHASISWA (DONUT CHART)", fontsize=13, fontweight="bold", pad=20, color="#1e293b")
plt.tight_layout()
plt.show()

# 4. STATISTIKA DESKRIPTIF
dataraw["Nilai"] = pd.to_numeric(dataraw["Nilai"], errors="coerce")
dt = dataraw["Nilai"]

stats = dt.describe()
stats["Standard Error"] = dt.sem()
stats["Median"] = dt.median()
stats["Mode"] = dt.mode().iloc[0]
stats["variance"] = dt.var()
stats["range"] = dt.max() - dt.min()
stats["skewness"] = dt.skew()
stats["kurtosis"] = dt.kurtosis()

print("\n--- HASIL STATISTIKA DESKRIPTIF ---")
print(stats)