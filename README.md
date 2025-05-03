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

| Home Page                        | Prediction Output                | Azure Deployment Proof           |
|----------------------------------|----------------------------------|----------------------------------|
| ![](screenshots/home-page.png)  | ![](screenshots/prediction.png) | ![](screenshots/azure-portal.png) |

> Make sure you place your actual screenshots in the `/screenshots/` folder of your repository.

---

## 🖥️ How to Use

### 🌐 Web Form Inputs:

From the user interface (`home.html`):

- **Maximum Wind Speed**
- **Maximum Temperature**
- **Minimum Temperature**
- **Average Temperature**
- **Average Wind Speed**

The output will be rendered as:

> `AQI for Jaipur 178.23`

---

### 📡 API Usage

`POST /predict_api`

**Example Request (JSON):**
```json
{
  "feature1": 12.1,
  "feature2": 42.0,
  "feature3": 22.5,
  "feature4": 30.1,
  "feature5": 10.0
}
```

**Example Response:**
```json
178.23
```

---

## ⚙️ Local Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/jaipur-aqi-predictor.git
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

## 🔁 Project Structure

```
.
├── README.md
├── screenshots/
│   ├── home-page.png
│   ├── prediction.png
│   └── azure-portal.png
├── app.py
├── requirements.txt
├── randomForestRegressor.pkl
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── home.html
└── .github/
    └── workflows/
        └── azure-webapp.yml
```

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


