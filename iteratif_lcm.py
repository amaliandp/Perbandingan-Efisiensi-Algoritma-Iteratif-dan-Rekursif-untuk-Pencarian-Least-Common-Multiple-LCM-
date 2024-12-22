def find_lcm_iterative(x, y):
    lcm = max(x, y)
    while True:
        if lcm % x == 0 and lcm % y == 0:
            return lcm
        lcm += 1

if __name__ == "__main__":
    import time
    x = int(input("Masukkan bilangan pertama: "))
    y = int(input("Masukkan bilangan kedua: "))

    start = time.perf_counter()  # Menggunakan perf_counter untuk waktu lebih presisi
    lcm = find_lcm_iterative(x, y)
    end = time.perf_counter()  

    print(f"KPK (Iteratif) dari {x} dan {y} adalah: {lcm}")
    print(f"Waktu eksekusi iteratif: {end - start:.6f} detik")
