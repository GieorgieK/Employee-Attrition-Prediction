import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


#melebarkan
st.set_page_config(
    page_title='Employee Attrition Prediction',
    layout='wide',
    initial_sidebar_state='expanded'

)

st.markdown("""<style>.reportview-container {background: "5160549.jpg"}.sidebar .sidebar-content {background: "5160549.jpg"}</style>""",unsafe_allow_html=True)



def run():

    # membuat judul
    st.title('Employee Attrition Prediction')

    #membuat sub header
    st.subheader('Employee Attrition Prediction EDA')

    #menambahkan deskripsi
    st.write('Created by: Gieorgie Kosasih')

    # library pillow buat gambar
    image = Image.open('employee.jpg')
    st.markdown('---')
    st.image(image) 


    # Membuat Garis lurus
    st.markdown('---')


    # Nampilin dataframe
    st.write('### Employee Attrition Data')

    df = pd.read_csv('Main_Data.csv')
    st.dataframe(df.head(5))

    st.markdown('***')
    

    
    ###########################################
    
    st.write('### Attrition Distribution')
    
    # Menghitung jumlah setiap value
    target_counts = df['Attrition'].value_counts()

    # Membuat label untuk legenda dengan jumlah setiap value
    labels = [f'Attrition {i} - {count}' for i, count in target_counts.items()]

    # Membuat pie chart
    fig = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 2)
    target_counts.plot(kind='pie', autopct='%1.1f%%',  shadow=True, labels=None, colors =['#0072C6', '#BFBFBF'])
    plt.title('Employee Attrition')

    # Menambahkan legenda
    plt.legend(labels, loc='upper right', bbox_to_anchor=(1.3, 1))
    
    
    st.pyplot(fig)
    
    st.markdown('---')


    ###########################################
    st.write('### Data Demografi Karyawan')
    pilihan = st.selectbox('Pilih Kolom : ', ('Gender','Education','MaritalStatus','Department'))

    # Melakukan pengelompokan langsung pada indeks DataFrame
    attrition_data = df.groupby([df[pilihan], 'Attrition']).size().unstack(fill_value=0)

    fig = plt.figure(figsize=(15, 5))
    colors =['#0072C6', '#BFBFBF']
    # Plot: Distribusi Attrition berdasarkan kolom yang dipilih
    ax = plt.gca()

    # Menyesuaikan jenis plot berdasarkan jumlah indeks attrition_data
    if len(attrition_data.index) > 3:
        attrition_data.plot(kind='barh', stacked=True, color=colors, ax=ax)
        ax.set_xlabel('Jumlah Karyawan')
        ax.set_ylabel(pilihan)  # Menggunakan nama kolom yang dipilih langsung
    else:
        attrition_data.plot(kind='bar', stacked=True, color=colors, ax=ax)
        ax.set_ylabel('Jumlah Karyawan')
        ax.set_xlabel(pilihan)  # Menggunakan nama kolom yang dipilih langsung
        ax.set_xticklabels(attrition_data.index, rotation=0)

    ax.set_title(f'Distribusi Attrition Berdasarkan {pilihan}')  # Menggunakan nama kolom yang dipilih langsung
    ax.legend(title='Attrition', labels=['Tidak', 'Ya'])

    # Menambahkan anotasi pada plot
    for container in ax.containers:
        if len(attrition_data.index) > 3:
            labels = [f'{int(v.get_width())}' for v in container]
        else:
            labels = [f'{int(v.get_height())}' for v in container]
        ax.bar_label(container, labels=labels, label_type='center', padding=2)
    st.pyplot(fig)

    st.markdown('---')

    ####################################################

    st.write('### Data Survey Karyawan')
    pilihan = st.selectbox('Pilih Kolom : ', ('EnvironmentSatisfaction','JobSatisfaction', 'WorkLifeBalance'))

    # Melakukan pengelompokan langsung pada indeks DataFrame
    attrition_data = df.groupby([df[pilihan], 'Attrition']).size().unstack(fill_value=0)

    fig = plt.figure(figsize=(15, 5))
    colors =['#0072C6', '#BFBFBF']
    # Plot: Distribusi Attrition berdasarkan kolom yang dipilih
    ax = plt.gca()

    # Menyesuaikan jenis plot berdasarkan jumlah indeks attrition_data
    if len(attrition_data.index) > 3:
        attrition_data.plot(kind='barh', stacked=True, color=colors, ax=ax)
        ax.set_xlabel('Jumlah Karyawan')
        ax.set_ylabel(pilihan)  # Menggunakan nama kolom yang dipilih langsung
    else:
        attrition_data.plot(kind='bar', stacked=True, color=colors, ax=ax)
        ax.set_ylabel('Jumlah Karyawan')
        ax.set_xlabel(pilihan)  # Menggunakan nama kolom yang dipilih langsung
        ax.set_xticklabels(attrition_data.index, rotation=0)

    ax.set_title(f'Distribusi Attrition Berdasarkan {pilihan}')  # Menggunakan nama kolom yang dipilih langsung
    ax.legend(title='Attrition', labels=['Tidak', 'Ya'])

    # Menambahkan anotasi pada plot
    for container in ax.containers:
        if len(attrition_data.index) > 3:
            labels = [f'{int(v.get_width())}' for v in container]
        else:
            labels = [f'{int(v.get_height())}' for v in container]
        ax.bar_label(container, labels=labels, label_type='center', padding=2)
    st.pyplot(fig)

    st.markdown('---')

    ####################################################

    st.write('### Data Performa Karyawan')
    pilihan = st.selectbox('Pilih Kolom : ', ('JobInvolvement', 'PerformanceRating','BusinessTravel','JobLevel', 'JobRole'))

    # Melakukan pengelompokan langsung pada indeks DataFrame
    attrition_data = df.groupby([df[pilihan], 'Attrition']).size().unstack(fill_value=0)

    fig = plt.figure(figsize=(15, 5))
    colors =['#0072C6', '#BFBFBF']
    # Plot: Distribusi Attrition berdasarkan kolom yang dipilih
    ax = plt.gca()

    # Menyesuaikan jenis plot berdasarkan jumlah indeks attrition_data
    if len(attrition_data.index) > 3:
        attrition_data.plot(kind='barh', stacked=True, color=colors, ax=ax)
        ax.set_xlabel('Jumlah Karyawan')
        ax.set_ylabel(pilihan)  # Menggunakan nama kolom yang dipilih langsung
    else:
        attrition_data.plot(kind='bar', stacked=True, color=colors, ax=ax)
        ax.set_ylabel('Jumlah Karyawan')
        ax.set_xlabel(pilihan)  # Menggunakan nama kolom yang dipilih langsung
        ax.set_xticklabels(attrition_data.index, rotation=0)

    ax.set_title(f'Distribusi Attrition Berdasarkan {pilihan}')  # Menggunakan nama kolom yang dipilih langsung
    ax.legend(title='Attrition', labels=['Tidak', 'Ya'])

    # Menambahkan anotasi pada plot
    for container in ax.containers:
        if len(attrition_data.index) > 3:
            labels = [f'{int(v.get_width())}' for v in container]
        else:
            labels = [f'{int(v.get_height())}' for v in container]
        ax.bar_label(container, labels=labels, label_type='center', padding=2)
    st.pyplot(fig)

    st.markdown('---')

    ####################################################

    st.write('### Data Numerical')
    pilihan = st.selectbox('Pilih Kolom : ', ('Age','DistanceFromHome','MonthlyIncome', 'NumCompaniesWorked','PercentSalaryHike','TotalWorkingYears',
               'YearsAtCompany','YearsSinceLastPromotion','YearsWithCurrManager'))
    
    
    fig = plt.figure(figsize=(15, 5))
    
    attrition_no = df[df['Attrition'] == 'No'][pilihan]
    attrition_yes = df[df['Attrition'] == 'Yes'][pilihan]
    
    sns.histplot(attrition_no, color=colors[0], label='No', kde=False, bins=30)
    sns.histplot(attrition_yes, color=colors[1], label='Yes', kde=False, bins=30)
    
    plt.title(f'Histogram Distribusi {pilihan} Berdasarkan Attrition')
    plt.xlabel(pilihan)
    plt.ylabel('Jumlah Karyawan')
    plt.legend(title='Attrition')
    
    plt.tight_layout()
    
    st.pyplot(fig)


if __name__ == '__main__':
    run()