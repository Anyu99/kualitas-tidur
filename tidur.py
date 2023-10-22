import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# membaca model
model = pickle.load(open('tidur.sav', 'rb'))

#judul web
st.title('Prediksi Tidur Sehat')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Age = st.number_input('Umur Pasien')
    Sleep_Duration = st.number_input('Berapa jam pasien tidur setiap harinya?')
    Quality_of_Sleep = st.number_input('Dari 1 - 10, Berapa kualitas tidur pasien?')
    Physical_Activity_Level = st.number_input('Total berapa menit pasien melakukan aktivitas fisik perharinya?')
    Stress_Level = st.number_input('Dari 1 - 10, Berapa peringkat subjektif dari tingkat stres yang dialami oleh pasien?')
    Heart_Rate = st.number_input('Denyut jantung istirahat pasien per menit')
    Daily_Steps = st.number_input('Jumlah langkah yang dilakukan pasien per hari.')
with col2:
    Occ = st.selectbox('Pekerjaan pasien', ['Nurse','Doctor', 'Engineer','Lawyer', 'Teacher', 
                                            'Accountant', 'Salesperson', 'Software Engineer', 
                                            'Scientist', 'Sales Representative', 'Manager'])
    BMI = st.selectbox('Kategori BMI pasien', ['Normal','Overweight','Normal Weight','Obese'])
    gender = st.selectbox('Jenis Kelamin Penumpang', ['Laki-Laki', 'Perempuan'])
    BPU = st.number_input('Tekanan Darah Sistolik Pasien')
    BPD = st.number_input('Tekanan Darah Diastolik Pasien')

label_encoder_occ = LabelEncoder()
label_encoder_occ.fit(['Nurse','Doctor', 'Engineer','Lawyer', 'Teacher', 
                    'Accountant', 'Salesperson', 'Software Engineer', 
                    'Scientist', 'Sales Representative', 'Manager'])
encoded = label_encoder_occ.transform([Occ])[0]

label_encoder_bmi = LabelEncoder()
label_encoder_bmi.fit(['Normal','Overweight','Normal Weight','Obese'])
bmi_encoded = label_encoder_bmi.transform([BMI])[0]

label_encoder_gender = LabelEncoder()
label_encoder_gender.fit(['Laki-Laki', 'Perempuan'])
gender_encoded = label_encoder_gender.transform([gender])[0]

tidur = ''

if st.button('Proses'):
    predict = model.predict(
        [[Age, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, 
          Stress_Level, Heart_Rate, Daily_Steps, encoded, bmi_encoded, gender_encoded, BPU, BPD]]
    )
    if predict == 0:
        tidur = 'Kualitas tidur pasie termasuk kedalam kategori Insomnia'
    elif predict == 1:
        tidur = 'Kualitas tidur pasie termasuk kedalam kategori Normal'
    else:
        tidur = 'Kualitas tidur pasie termasuk kedalam kategori Sleep Apnea'
    st.write(tidur)
