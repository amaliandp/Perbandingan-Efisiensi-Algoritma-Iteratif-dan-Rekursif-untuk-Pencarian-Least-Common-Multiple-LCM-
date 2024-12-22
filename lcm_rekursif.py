def find_lcm_recursive(x, y, candidate=None):
    if candidate is None:
        candidate = max(x, y)
    if candidate % x == 0 and candidate % y == 0:
        return candidate
    return find_lcm_recursive(x, y, candidate + 1)

if __name__ == "__main__":
    import time
    import sys

    sys.setrecursionlimit(1000000)  

    x = int(input("Masukkan bilangan pertama (3-5 digit): "))
    y = int(input("Masukkan bilangan kedua (3-5 digit): "))

    start = time.perf_counter()  # Menggunakan perf_counter untuk waktu lebih presisi
    try:
        lcm = find_lcm_recursive(x, y)
        end = time.perf_counter()  # Menggunakan perf_counter untuk waktu lebih presisi
        print(f"KPK (Rekursif) dari {x} dan {y} adalah: {lcm}")
        print(f"Waktu eksekusi rekursif: {end - start:.6f} detik")
    except RecursionError:
        print("RecursionError: Maksimum kedalaman rekursi terlampaui.")
