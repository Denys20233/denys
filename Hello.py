import streamlit as st
import pandas as pd

background_color = "#001F3F"  # Ваш колір фону

# Встановлення стилів
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            color: white;
        }}
    </style>
    """,
    unsafe_allow_html=True
)


def postgre_sql(selected_project):
    st.subheader(f"PostgreSQL - {selected_project}")
    if selected_project == 'Проект 1':
        st.write(f"111111111")
        st.markdown("[Посилання на детальну інформацію про проект]("
                    "https://denys-pidhainyi-data-analyst-portfolio.my.canva.site/_link/?link=https%3A%2F%2Fwww.ca"
                    "nva.com"
                    "%2Fdesign%2FDAFtMZOf3T4%2FYM084DeyAzy3Mn2Pv9p75Q%2Fview%3Futm_content%3DDAFtMZOf3T4%26utm_campaign"
                    "%3Ddesignshare%26utm_medium%3Dlink%26utm_source%3Dviewer&target=TOcGtUZ0UKaFA%2FC8u58Y2bBDgFYCS"
                    "2C2%"
                    "2ByIaR8Uw4yqhXkCwNJ%2FPA%2BByMyDO2w%2FJGrK%2BvutBwN6%2FmLoz2tsF9wd8GU%2BmWGFDWhtxphUIxBm8xda"
                    "qY%2B6w"
                    "r%2BVhaEORM6eoL8nZwMPbgI8EYUukoco%2Fn1BrORTa7sYg2XBFizUN5y6JNJ7xGJZp%2BDlvf2YFRWq0Syf%2BkY7Yff"
                    "6H78xKMTKecQIKMRwQ6OU0XwddSTgNxZRcNx0Die%2FpLxlZV7N35Nu4s4gJ8tnW7pHgLE%2BPDSpuBwaGgP%2BsojkQ"
                    "76B9Ea6JxY7V2UyaeomhuN3wfrmd&iv=QQeQa6BTIwixaX5N)")

        st.write(f"111111111")
        st.write(f"111111111")
        st.write(f"111111111")


    elif selected_project == 'Проект 2':
        st.write(f"2222222222")

    elif selected_project == 'Проект 3':
        st.write(f"333333333333")


def bigquery(selected_project):
    st.subheader(f"Big Query - {selected_project}")
    st.write(f"Опис проекту Python {selected_project}")


def python(selected_project):
    st.subheader(f"Python - {selected_project}")



    if selected_project == 'Jupyter notebook 1':
        st.write(f"111111111")

        path = r"C:\Users\Acer\Desktop\University\Курс2 семестр1\Програмування\Visualization\Global YouTube Statistics.csv"

        dataset = pd.read_csv(path, encoding='iso-8859-1')
        st.dataframe(dataset)

        st.write(f"111111111")

        st.image("graph1.jpg", output_format="auto")
        st.image("graph12.jpg", output_format="auto")
        st.image("graph13.jpg", output_format="auto")
        st.image("graph14.jpg", output_format="auto")
        st.image("Знімок екрана 2023-10-02 201020.png", output_format="auto")

    elif selected_project == 'Проект 2':
        st.write(f"2222222222")


    elif selected_project == 'Проект 3':
        st.write(f"333333333333")


def google_sheets(selected_project):
    st.subheader(f"Google Sheets - {selected_project}")
    st.write(f"Опис проекту Google Sheets {selected_project}")


def tableau(selected_project):
    st.subheader(f"Tableau - {selected_project}")
    st.write(f"Опис проекту Google Sheets {selected_project}")


def looker_studio(selected_project):
    st.subheader(f"Looker Studio - {selected_project}")
    st.write(f"Опис проекту Google Sheets {selected_project}")


def power_bi(selected_project):
    st.subheader(f"Power BI - {selected_project}")
    st.write(f"Опис проекту Google Sheets {selected_project}")


def amplitude(selected_project):
    st.subheader(f"Amplitude - {selected_project}")
    st.write(f"Опис проекту Google Sheets {selected_project}")


st.title('Портфоліо')


sections = ['PostgreSQL', 'Bigquery', 'Python', 'Google Sheets', 'Tableau', 'Looker studio', 'Power BI', 'Amplitude']
selected_section = st.sidebar.selectbox("Оберіть розділ:", sections)


# selected_project = None
if selected_section == 'PostgreSQL':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        postgre_sql(selected_project)


elif selected_section == 'Bigquery':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        bigquery(selected_project)


elif selected_section == 'Python':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Jupyter notebook 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        python(selected_project)



elif selected_section == 'Google Sheets':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        google_sheets(selected_project)


elif selected_section == 'Tableau':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        tableau(selected_project)


elif selected_section == 'Looker studio':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        looker_studio(selected_project)


elif selected_section == 'Power BI':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        power_bi(selected_project)


elif selected_section == 'Amplitude':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        amplitude(selected_project)