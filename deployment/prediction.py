import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# Path to the model file
model_path = "model.pkl"

# Load the model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def run():
    st.title('Prediksi Pengunduran Diri Karyawan')
    # library pillow buat gambar
    st.markdown('---')
    image = Image.open('image_prediction.jpg')
    st.image(image) 


    # Membuat Garis lurus
    st.markdown('---')

    # Formulir untuk pengisian data
    with st.form('form_employee_attrition'):
        # Kolom input sesuai dengan keterangan yang Anda berikan
        business_travel = st.selectbox('Business Travel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
        department = st.selectbox('Department', ['Sales', 'Research & Development', 'Human Resources'])
        education_field = st.selectbox('Education Field', ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])
        job_role = st.selectbox('Job Role', ['Healthcare Representative', 'Research Scientist', 'Sales Executive', 'Human Resources', 'Research Director', 'Laboratory Technician', 'Manufacturing Director', 'Sales Representative', 'Manager'])
        marital_status = st.selectbox('Marital Status', ['Married', 'Single', 'Divorced'])
        training_times_last_year = st.selectbox('Training Times Last Year', [0, 1, 2, 3, 4, 5, 6])
        job_involvement = st.selectbox('Job Involvement', [1, 2, 3, 4], format_func=lambda x: {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'}[x])
        environment_satisfaction = st.selectbox('Environment Satisfaction', [1, 2, 3, 4], format_func=lambda x: {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'}[x])
        job_satisfaction = st.selectbox('Job Satisfaction', [1, 2, 3, 4], format_func=lambda x: {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'}[x])
        work_life_balance = st.selectbox('Work Life Balance', [1, 2, 3, 4], format_func=lambda x: {1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best'}[x])
        age = st.slider('Age', min_value=18, max_value=60)
        percent_salary_hike = st.slider('Percent Salary Hike', min_value=11, max_value=25)
        total_working_years = st.slider('Total Working Years', min_value=0, max_value=40)
        years_at_company = st.slider('Years At Company', min_value=0, max_value=40)
        years_since_last_promotion = st.slider('Years Since Last Promotion', min_value=0, max_value=15)
        years_with_curr_manager = st.slider('Years With Current Manager', min_value=0, max_value=17)

        # Tombol untuk melakukan prediksi
        submitted = st.form_submit_button('Prediksi')

    # Menyusun data input menjadi DataFrame
    data = {
        'BusinessTravel': business_travel,
        'Department': department,
        'EducationField': education_field,
        'JobRole': job_role,
        'MaritalStatus': marital_status,
        'TrainingTimesLastYear': training_times_last_year,
        'JobInvolvement': job_involvement,
        'EnvironmentSatisfaction': environment_satisfaction,
        'JobSatisfaction': job_satisfaction,
        'WorkLifeBalance': work_life_balance,
        'Age': age,
        'PercentSalaryHike': percent_salary_hike,
        'TotalWorkingYears': total_working_years,
        'YearsAtCompany': years_at_company,
        'YearsSinceLastPromotion': years_since_last_promotion,
        'YearsWithCurrManager': years_with_curr_manager
    }
    
    features = pd.DataFrame(data, index=[0])

    # Menampilkan fitur input pengguna
    st.write("## Fitur Input Pengguna")
    st.write(features)

    # Melakukan prediksi jika tombol prediksi ditekan
    if submitted:
        prediction = model.predict(features)
        st.subheader('Hasil Prediksi')
        st.write('Pengunduran Diri Karyawan:', 'Ya' if prediction[0] == 1 else 'Tidak')

if __name__ == '__main__':
    run()
