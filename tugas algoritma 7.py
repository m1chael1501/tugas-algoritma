def contains_lowercase(sentence):

  for char in sentence:
    if char.islower():
      return True # Langsung kembalikan True jika menemukan huruf kecil
  return False # Jika loop selesai tanpa menemukan huruf kecil

# Meminta input dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Memanggil fungsi dan mencetak hasilnya
if contains_lowercase(kalimat):
  print("Kalimat ini mengandung huruf kecil.")
else:
  print("Kalimat ini tidak mengandung huruf kecil.")