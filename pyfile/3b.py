import os
import warnings
import numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model

warnings.filterwarnings('ignore')
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Tentukan mapping kategori ke angka
category_mapping = {'< 5': 0, '5-10': 1, '> 10': 2}

# Path ke file model .keras
model_path = 'model/3b/model.keras'

# Memuat model
model = load_model(model_path)

math_score = get_valid_score("Enter Math Score (0-100): ")
reading_score = get_valid_score("Enter Reading Score (0-100): ")
writing_score = get_valid_score("Enter Writing Score (0-100): ")

user_input = np.array([[math_score, reading_score, writing_score]])

# 5. Melakukan prediksi
prediction = model.predict(user_input)

# 6. Menampilkan hasil prediksi
# Menggunakan np.argmax untuk mendapatkan indeks kelas dengan probabilitas tertinggi
predicted_class = np.argmax(prediction, axis=1)

# Convert kembali ke label asli menggunakan mapping manual
inverse_category_mapping = {v: k for k, v in category_mapping.items()}
predicted_label = [inverse_category_mapping[class_idx] for class_idx in predicted_class]

# print("Predicted class index:", predicted_class)
print("Predicted label:", predicted_label)
