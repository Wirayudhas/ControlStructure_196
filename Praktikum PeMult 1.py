# Tugas 1: Penilaian
def penilaian(percentage):
    # Fungsi ini mengevaluasi kinerja berdasarkan persentase yang diberikan
    if percentage >= 90:
        return "Excellent performance" 
    elif percentage >= 80:
        return "Very Good performance" 
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Poor performance"

# Mengambil input dari pengguna
percentage = float(input("Enter the student's percentage: "))
# Mencetak hasil penilaian
print(penilaian(percentage))

# Tugas 2: Mencari Angka Terbesar
# Mengambil tiga angka dari pengguna
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Memeriksa angka terbesar
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")  
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")  
else:
    print(f"The largest number is: {num3}")  

# Tugas 3: Deret Fibonacci
# Mengambil nilai maksimum dari deret Fibonacci
n = int(input("Enter the maximum value of Fibonacci series: "))
a, b = 0, 1  # Inisialisasi dua angka pertama dari deret

# Mencetak deret Fibonacci hingga nilai maksimum yang diberikan
print("Fibonacci series up to", n, ":")
while a <= n:
    print(a, end=" ")  # Mencetak angka Fibonacci
    a, b = b, a + b   # Mengupdate nilai a dan b

# Tugas 4: Angka Ganjil
# Mengambil nilai n dari pengguna
n = int(input("Enter the value of n: "))
print("Odd numbers up to n:")
# Mengiterasi dari 1 hingga n
for i in range(1, n + 1):
    if i % 2 != 0:  # Memeriksa apakah angka tersebut ganjil
        print(i, end=" ")  # Mencetak angka ganjil

# Tugas 5: Segitiga Angka
# Mengambil nilai n dari pengguna
n = int(input("Enter the value of n: "))
# Menghasilkan pola segitiga angka
for i in range(1, n + 1):
    print((str(i) + " ") * i)  # Mencetak angka i sebanyak i kali
