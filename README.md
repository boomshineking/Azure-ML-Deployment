# AzureDeployment
[![Build & Deploy CI/CD](https://img.shields.io/badge/build%20&%20deploy%20ci%2Fcd-pass-brightgreen)](https://github.com/boomshineking/Azure-ML-Deployment/actions/runs/14585266147)


# 🌫️ Jaipur AQI Predictor (Air Quality Index)

A Flask-based machine learning web application that predicts the **Air Quality Index (AQI)** for Jaipur, India, using weather-related inputs such as temperature and wind speed. The model is built with `RandomForestRegressor` and prepared for deployment on **Azure App Services** with a fully integrated **GitHub Actions** CI/CD workflow.

---

## 🧠 Features

- ✅ User-friendly web interface for AQI prediction
- 🔁 API endpoint for programmatic predictions
- 📦 ML model serialized using `pickle`
- 🚀 CI/CD pipeline configured with GitHub Actions
- 🛠️ Azure-ready deployment configuration
- 📸 Deployment proof included via screenshots

---

## 📸 Screenshots

| Home Page     
![jaipur](https://github.com/user-attachments/assets/28571218-5cc5-4e9c-a189-70bb5c42a2fd)
|--------------------------------------------------------------------------------------------------------------------------|
| Prediction Output      
![Jaipur result](https://github.com/user-attachments/assets/2fe3e34f-46b0-4126-80fd-fef3e5ee9135)
|--------------------------------------------------------------------------------------------------------------------------|
| Azure Deployment Proof 
1.![Screenshot 2025-04-22 030044](https://github.com/user-attachments/assets/f8425b28-a1c4-4ee1-8591-60d26bfbcbc3)
2.![Screenshot 2025-04-22 030244](https://github.com/user-attachments/assets/fb8c736f-61f0-4146-bd09-5682ca102a59)
3.![Screenshot 2025-04-22 030944](https://github.com/user-attachments/assets/c54802cd-37f9-4972-a733-2dab8d02ad87)
4.![Screenshot 2025-04-22 031818](https://github.com/user-attachments/assets/7b5561b7-c7c7-4263-b42f-072a6d199eb7)
5.![Screenshot 2025-04-22 034702](https://github.com/user-attachments/assets/408792d8-b0d6-40a4-8143-b03b17c1f879)
|--------------------------------------------------------------------------------------------------------------------------|
---

## 🖥️ How to Use

### 🌐 Web Form Inputs:

From the user interface (`home.html`):

- **Maximum Wind Speed**
- **Maximum Temperature**
- **Minimum Temperature**
- **Average Temperature**
- **Average Wind Speed**
## ⚙️ Local Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/jaipur-aqi-predictor.git](https://github.com/boomshineking/Azure-ML-Deployment)
   cd jaipur-aqi-predictor
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   python app.py
   ```

   Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🤖 GitHub Actions CI/CD

- Trigger: Push to `main` branch
- Builds and zips project
- Uploads artifact
- Deploys to Azure (when configured)
  
> ⚠️ **Note:** App is not currently deployed live due to Azure costs. CI/CD is configured and proven via screenshots.

---

## 📜 Requirements

Here are the key packages used:

```
certifi
Click
Flask
gunicorn
itsdangerous
Jinja2
MarkupSafe
Werkzeug
numpy
scipy
matplotlib
pandas
tpot
seaborn
cloudpickle
scikit-learn
joblib
```

These were generated via `pip freeze` after setting up the project.

---

## 🔒 GitHub Secrets (for Deployment)

To enable Azure deployment, store your Azure publish profile as a GitHub secret:

| Secret Name | Description |
|-------------|-------------|
| `AZUREAPPSERVICE_PUBLISHPROFILE_...` | Your Azure App Service publish profile content |

---

## 📄 License

MIT License © 2025 Richard Stephenraj

---


