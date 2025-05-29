
# 🩺 MediPredict+

**MediPredict+** is a unified, Streamlit-based web application that uses multiple machine learning models to predict the likelihood of various diseases including:

- Diabetes
- Heart Disease
- Breast Cancer
- Parkinson’s Disease
- Lung Cancer

This tool is designed to assist users and medical professionals with early-stage risk assessment using structured input parameters.

---

## 📸 Demo

![MediPredict+ Logo](logopng.png)

---

## 🚀 Features

✅ User-friendly web interface via **Streamlit**  
✅ 5 disease predictions in one unified platform  
✅ Model-driven predictions with input validation  
✅ Interactive sidebar navigation  
✅ Responsive design with organized input sections

---

## 🧠 Machine Learning Models Used

Each disease module is powered by pre-trained machine learning models:

| Disease               | Model File                          |
|----------------------|-------------------------------------|
| Diabetes             | `Diabetes_trained_model.sav`        |
| Heart Disease        | `trained_model.sav`                 |
| Breast Cancer        | `breast_cancer_model.sav`           |
| Parkinson's Disease  | `Parkinsons_trained_model.sav`      |
| Lung Cancer          | `lung_trained_model.sav`            |

---

## 🧾 Requirements

- Python 3.8+
- Streamlit
- Pillow
- streamlit-option-menu
- scikit-learn
- Pickle (standard library)

Install dependencies:

```bash
pip install streamlit pillow streamlit-option-menu scikit-learn
```

---

## 📂 Project Structure

```
├── Medipredict.py                  # Main Streamlit app
├── logopng.png                     # Logo image
├── Saved Models/
│   ├── Diabetes_trained_model.sav
│   ├── trained_model.sav
│   ├── breast_cancer_model.sav
│   ├── Parkinsons_trained_model.sav
│   └── lung_trained_model.sav
└── README.md
```

---

## ▶️ Run the App

Make sure all `.sav` model files and the logo image are placed correctly. Then launch the app using:

```bash
streamlit run Medipredict.py
```

---

## 📌 Notes

- Ensure all input fields are filled with valid numerical values where required.
- Lung cancer and Parkinson’s prediction includes categorical inputs that are internally encoded.
- For best results, use trained models with up-to-date datasets.

---

## 🙋‍♂️ Author

**Vinay Patel**  
B.Tech Final Year Project | Feroze Gandhi Institute of Engineering & Technology  
Email: [vinaypatel0039@gmail.com]  
LinkedIn: [(https://www.linkedin.com/in/iamvinay1/)]  

---

## 📄 License

This project is licensed for academic and educational purposes only.
