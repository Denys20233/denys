import streamlit as st
import pandas as pd



def sql(selected_project):
    # st.subheader(f"{selected_project}")
    if selected_project == 'PostgreSQL':
        st.subheader("PostgreSQL - 1")
        st.write("")
        st.write("Написав SQL запит, що вибере з таблиці наступні дані:")

        text_sql1 = "ad_date - дата показу реклами"
        formatted_text1 = f"<div>• {text_sql1}</div>"
        st.markdown(formatted_text1, unsafe_allow_html=True)

        text_sql2 = "campaign_id - унікальний ідентифікатор кампанії"
        formatted_text2 = f"<div>• {text_sql2}</div>"
        st.markdown(formatted_text2, unsafe_allow_html=True)

        text_sql3 = "агреговані за датою та id кампанії значення для наступних показників:"
        formatted_text3 = f"<div>• {text_sql3}</div>"
        st.markdown(formatted_text3, unsafe_allow_html=True)


        text_sql4 = "- кількість показів"
        text_sql5 = "- кількість кліків"
        text_sql6 = "- загальна сума витрат"
        text_sql7 = "- загальний Value конверсій"

        formatted_text4 = f"""
        <div style='<div style='font-size: 0.5em;'>{text_sql4}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql5}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql6}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql7}</div>
        """
        st.markdown(formatted_text4, unsafe_allow_html=True)

        st.write("")

        text_sql8 = "Використовуючи агреговані показники витрат та конверсій, розрахував для кожної дати та id кампанії такі метрики:"
        formatted_text8 = f"<div>• {text_sql8}</div>"
        st.markdown(formatted_text8, unsafe_allow_html=True)

        text_sql9 = "- CPC"
        text_sql10 = "- CPM"
        text_sql11 = "- CTR"
        text_sql12 = "- ROMI"

        formatted_text5 = f"""
        <div style='<div style='font-size: 0.5em;'>{text_sql9}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql10}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql11}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql12}</div>
        """
        st.markdown(formatted_text5, unsafe_allow_html=True)

        st.write("")

        text_sql13 = "Окремим запитом серед кампаній з загальною сумою витрат більше 500 000 знайди кампанію з найвищим ROMI."
        formatted_text13 = f"<div>• {text_sql13}</div>"
        st.markdown(formatted_text13, unsafe_allow_html=True)

        sql_code1 = """
select
	campaign_id,
	ad_date,
	sum(spend) as spend_suma,
	sum(impressions) as impressions_suma,
	sum(clicks) as clicks_suma,
	sum(value) as value_suma,
	round(Cast(sum(spend) as decimal(10,4)) / sum(clicks), 4) as CPC,
	round((Cast(sum(spend) as decimal(10,4)) / sum(impressions)) * 1000, 4) as CPM,
	round((Cast(sum(clicks) as decimal(10,4)) / sum(impressions)) * 100, 4) as CTR_percentage,
	round((((cast(sum(value) as decimal(10,1)) - sum(spend)) / sum(spend)) * 100), 1) as ROMI_percentage
from facebook_ads_basic_daily
where spend > 0 and clicks > 0 and impressions > 0
group by
	campaign_id,
	ad_date;



select
	campaign_id,
	sum(value) as value_suma,
	sum(spend) as spend_suma,
	round((((cast(sum(value) as decimal(10,1)) - sum(spend)) / sum(spend)) * 100), 1) as ROMI_percentage
from facebook_ads_basic_daily
where spend > 0
group by
	campaign_id 
having sum(spend) > 500000
limit 1;
"""
        st.write("")
        st.code(sql_code1, language='sql')
        st.write("")
        st.subheader("PostgreSQL - 2.1")
        st.write("")
        st.write("У цьому завданні я використав дані з чотирьох таблиць в БД:")
        st.write("")
        text_sql14 = "Використовуючи агреговані показники витрат та конверсій, розрахував для кожної дати та id кампанії такі метрики:"
        formatted_text14 = f"<div>• {text_sql14}</div>"
        st.markdown(formatted_text14, unsafe_allow_html=True)

        text_sql15 = "- ad_date - дата показу реклами в Google та Facebook"
        text_sql16 = "- campaign_name - назва кампанії в Google та Facebook"
        text_sql17 = "- spend, impressions, reach, clicks, leads, value - метрики кампаній та наборів оголошень у відповідні дні"

        formatted_text6 = f"""
        <div style='<div style='font-size: 0.5em;'>{text_sql15}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql16}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql17}</div>
        """
        st.markdown(formatted_text6, unsafe_allow_html=True)

        st.write("")

        text_sql18 = "З отриманої обʼєднаної таблиці (CTE) зробив вибірку:"
        formatted_text18 = f"<div>• {text_sql18}</div>"
        st.markdown(formatted_text18, unsafe_allow_html=True)

        text_sql19 = "- ad_date - дата показу реклами"
        text_sql20 = "- campaign_name - назва кампанії"
        text_sql21 = "- агреговані за датою та campaign_name значення для показників: (загальна сума витрат, кількість показів, кількість кліків, загальний Value конверсій)"

        formatted_text7 = f"""
        <div style='<div style='font-size: 0.5em;'>{text_sql19}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql20}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql21}</div>
        """
        st.markdown(formatted_text7, unsafe_allow_html=True)
        st.write("")
        sql_code2 = """
with test_table as (select ad_date, campaign_name, spend, impressions, reach, clicks, leads, value from facebook_ads_basic_daily
join facebook_adset on facebook_adset.adset_id = facebook_ads_basic_daily.adset_id
join facebook_campaign on facebook_campaign.campaign_id = facebook_ads_basic_daily.campaign_id
union all 
select ad_date, campaign_name, spend, impressions, reach, clicks, leads, value from Google_ads_basic_daily
)
select 
	ad_date,
	campaign_name,
	sum(spend) as spend_suma,
	sum(impressions) as impressions_suma,
	sum(clicks) as clicks_suma,
	sum(value) as value_suma
from test_table
group by ad_date, campaign_name;
"""
        st.write("")
        st.code(sql_code2, language='sql')

        st.write("")
        st.subheader("PostgreSQL - 2.2")
        st.write("")
        st.write("""Обʼєднавши дані з чотирьох таблиць, визначив кампанію з найвищим ROMI серед усіх кампаній з загальною сумою витрат більше 500 000 та
в цій кампанії визначив групу оголошень (adset_name) з найвищим ROMI.""")
        st.write("")

        sql_code3 = """
with test_table as (select ad_date, campaign_name, adset_name, spend, value from facebook_ads_basic_daily
join facebook_adset on facebook_adset.adset_id = facebook_ads_basic_daily.adset_id
join facebook_campaign on facebook_campaign.campaign_id = facebook_ads_basic_daily.campaign_id
union all 
select ad_date, campaign_name, adset_name, spend, value from Google_ads_basic_daily
)
select 
  campaign_name,
  sum(spend) as spend_suma,
  sum(value) as value_suma,
  round((((cast(sum(value) as decimal(10,1)) - sum(spend)) / sum(spend)) * 100), 1) as ROMI_percentage,
  adset_name
from test_table
where spend > 0 
group by campaign_name, adset_name
having sum(spend) > 500000
order by round((((cast(sum(value) as decimal(10,1)) - sum(spend)) / sum(spend)) * 100), 1) desc
limit 1
"""
        st.write("")
        st.code(sql_code3, language='sql')

        st.write("")
        st.subheader("PostgreSQL - 3")
        st.write("")
        st.write("У цьому завданні я використав дані з чотирьох таблиць в БД:")
        st.write("")

        text_sql21 = "У CTE запиті обʼєднав дані з наведених вище таблиць, щоб отримати:"
        formatted_text21 = f"<div>• {text_sql21}</div>"
        st.markdown(formatted_text21, unsafe_allow_html=True)

        text_sql22 = "- ad_date - дата показу реклами в Google та Facebook;"
        text_sql23 = "- url_parameters - частина URL з посилання кампаній, що включає в себе UTM параметри;"
        text_sql24 = "- spend, impressions, reach, clicks, leads, value - метрики кампаній та наборів оголошень у відповідні дні;"

        formatted_text8 = f"""
        <div style='<div style='font-size: 1.2em;'>{text_sql22}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql23}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql24}</div>
        """
        st.markdown(formatted_text8, unsafe_allow_html=True)

        st.write("")

        text_sql25 = "З отриманого CTE зробив вибірку:"
        formatted_text25 = f"<div>• {text_sql25}</div>"
        st.markdown(formatted_text25, unsafe_allow_html=True)

        text_sql26 = "- ad_date - дата показу реклами"
        text_sql27 = "- utm_campaign - значення параметра utm_campaign з поля utm_parameters, що задовольняє наступним умовам (зведене до нижнього регістра та якщо значення utm_campaign в utm_parameters дорівнює ‘nan’,  воно має бути пустим (тобто null) в результуючій таблиці"
        text_sql28 = "- Загальна сума витрат, кількість показів, кількість кліків, а також загальний Value конверсій у відповідну дату по відповідній кампанії;"
        text_sql29 = "- CTR, CPC, CPM, ROMI у відповідну дату по відповідній кампанії."

        formatted_text9 = f"""
        <div style='<div style='font-size: 0.5em;'>{text_sql26}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql27}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql28}</div>
        <div style='<div style='font-size: 1.2em;'>{text_sql29}</div>
        """
        st.markdown(formatted_text9, unsafe_allow_html=True)
        st.write("")

        sql_code4 = """
with test_table as (
select 
  campaign_name, ad_date, url_parameters, spend, impressions,
  reach, clicks, leads, value,
  coalesce(leads, 0) as leads_1
from facebook_ads_basic_daily
join facebook_adset on facebook_adset.adset_id = facebook_ads_basic_daily.adset_id
join facebook_campaign on facebook_campaign.campaign_id = facebook_ads_basic_daily.campaign_id
union all 
select 
  campaign_name, ad_date, url_parameters, spend, impressions,
  reach, clicks, leads, value,
  coalesce(leads, 0) as leads_1 
from Google_ads_basic_daily
)
select 
  ad_date,
  case
    when lower(substring(url_parameters, 'utm_campaign=([^&#$]+)')) = 'nan' then null
    else lower(substring(url_parameters, 'utm_campaign=([^&#$]+)')) 
  end as utm_campaign,
  sum(spend) as spend_suma,
  sum(impressions) as impressions_suma,
  sum(clicks) as clicks_suma,
  sum(value) as value_suma,
  case
    when impressions > 0 then (cast(sum(clicks) as float) / sum(impressions)) * 100
    else 0
  end as CTR,
  case
    when clicks > 0 then sum(spend) / sum(clicks)
    else 0
  end as CPC,
  case
    when impressions > 0 then (cast(sum(spend) as float) / sum(impressions)) * 1000
    else 0
  end as CPM,
  case
    when spend > 0 then ((cast(sum(value) as float) - sum(spend)) / sum(spend)) * 100
    else 0
  end as ROMI
from test_table
group by utm_campaign, ad_date, clicks, impressions, spend
"""
        st.write("")
        st.code(sql_code4, language='sql')

        st.write("")
        st.subheader("PostgreSQL - 4")
        st.write("")
        st.write("У цьому завданні я використав CTE з попереднього завдання. Це будуть дані з Facebook і Google з полями:")

        text_sql30 = "ad_date"
        text_sql31 = "url_parameters"
        text_sql32 = "spend"
        text_sql33 = "impressions"
        text_sql34 = "reach"
        text_sql35 = "licks"
        text_sql36 = "leads"
        text_sql37 = "value"

        formatted_text10 = f"""
        <div>• {text_sql30}</div>
        <div>• {text_sql31}</div>
        <div>• {text_sql32}</div>
        <div>• {text_sql33}</div>
        <div>• {text_sql34}</div>
        <div>• {text_sql35}</div>
        <div>• {text_sql36}</div>
        <div>• {text_sql37}</div>
        """
        st.markdown(formatted_text10, unsafe_allow_html=True)

        st.write("")
        st.write("Використав CTE з попереднього завдання в новому (другому) CTE для створення вибірки з такими даними:")

        text_sql38 = "ad_month - перше число місяця дати показу реклами (отримане з ad_date);"
        text_sql39 = "utm_campaign, загальна сума витрат, кількість показів, кількість кліків, value конверсій, CTR, CPC, CPM, ROMI"

        formatted_text11 = f"""
        <div>• {text_sql38}</div>
        <div>• {text_sql39}</div>
        """
        st.markdown(formatted_text11, unsafe_allow_html=True)

        st.write("")
        st.write("Зробив результуючу вибірку з наступними полями:")

        text_sql40 = "Ad_month;"
        text_sql41 = "utm_campaign, загальна сума витрат, кількість показів, кількість кліків, value конверсій, CTR, CPC, CPM, ROMI;"

        formatted_text12 = f"""
        <div>• {text_sql40}</div>
        <div>• {text_sql41}</div>
        """
        st.markdown(formatted_text12, unsafe_allow_html=True)

        st.write("")
        st.write("Для кожної utm_campaign в кожен місяць додав нове поле: ‘різниця CPM, CTR та ROMI’ в поточному місяці відносно попереднього у відсотках.")

        st.write("")
        sql_code5 = """
with test_table_1 as (
select 
  ad_date, url_parameters, spend, impressions,
  reach, clicks, leads, value
from facebook_ads_basic_daily
join facebook_adset on facebook_adset.adset_id = facebook_ads_basic_daily.adset_id
join facebook_campaign on facebook_campaign.campaign_id = facebook_ads_basic_daily.campaign_id
union all 
select 
  ad_date, url_parameters, spend, impressions,
  reach, clicks, leads, value
from Google_ads_basic_daily
),
test_table_2 as (
select 
  date_trunc('month', ad_date) as ad_month,
    case
      when lower(substring(url_parameters, 'utm_campaign=([^&#$]+)')) = 'nan' then null
        else lower(substring(url_parameters, 'utm_campaign=([^&#$]+)')) 
        end as utm_campaign,
  sum(spend) as spend_suma,
    sum(impressions) as impressions_suma,
    sum(clicks) as clicks_suma,
    sum(value) as value_suma,
    case
      when impressions > 0 then (cast(sum(clicks) as float) / sum(impressions)) * 100
        else 0
        end as CTR,
    case
        when clicks > 0 then sum(spend) / sum(clicks)
        else 0
        end as CPC,
    case
        when impressions > 0 then (cast(sum(spend) as float) / sum(impressions)) * 1000
        else 0
        end as CPM,
    case
        when spend > 0 then ((cast(sum(value) as float) - sum(spend)) / sum(spend)) * 100
        else 0
        end as ROMI
from test_table_1
group by ad_date, url_parameters, clicks, impressions, spend
),
finish_table as(
select 
	utm_campaign as utm,
	ad_month as current_ad_month,
	((AVG(CPM) - lag(AVG(CPM), 1) over(PARTITION by utm_campaign order by ad_month))
			/ lag(AVG(CPM), 1) over(PARTITION by utm_campaign order by ad_month)) * 100 as CPM_difference,
	((AVG(CTR) - lag(AVG(CTR), 1) over(PARTITION by utm_campaign order by ad_month)) 
			/ lag(AVG(CTR), 1) over(PARTITION by utm_campaign order by ad_month)) * 100 as CTR_difference,
	((AVG(ROMI) - lag(AVG(ROMI), 1) over(PARTITION by utm_campaign order by ad_month)) 
			/ lag(AVG(ROMI), 1) over(PARTITION by utm_campaign order by ad_month)) * 100 as ROMI_difference,
--	AVG(CPM) as current_CPM,
--	AVG(CTR)as current_CTR,
--	AVG(ROMI)as current_ROMI,
	ad_month - interval '1 month' as month_ahead
--	lag(AVG(CPM), 1) over(PARTITION by utm_campaign order by ad_month) as CPM_ahead,
--	lag(AVG(CTR), 1) over(PARTITION by utm_campaign order by ad_month) as CTR_ahead,
--	lag(AVG(ROMI), 1) over(PARTITION by utm_campaign order by ad_month) as ROMI_ahead
from test_table_2
group by ad_month, month_ahead, utm
)
--select * from finish_table;
select 
	current_ad_month,
	utm_campaign,
	Round(CPM_difference) as CPM_difference,
	Round(CTR_difference) as CTR_difference,
	Round(ROMI_difference) as ROMI_difference,
	test_table_2.value_suma,
	test_table_2.spend_suma,
	test_table_2.clicks_suma,
	test_table_2.impressions_suma,
	CPM, CTR, CPC, ROMI
from finish_table
join test_table_2 on test_table_2.utm_campaign = finish_table.utm
"""
        st.write("")
        st.code(sql_code5, language='sql')
















    elif selected_project == 'Big Query':
        st.write(f"2222222222")

   


def bigquery(selected_project):
    st.subheader(f"Big Query - {selected_project}")
    st.write(f"Опис проекту Python {selected_project}")


def python(selected_project):
    st.subheader(f"Python - {selected_project}")



    if selected_project == 'Jupyter notebook 1':
        st.write(f"111111111")
        st.write(f"111111111")
        st.write(f"111111111")
        st.write(f"2")
        st.image("images/graph11.png", output_format="auto")
        st.image("images/graph11.png", output_format="auto")
        st.image("/workspaces/denys/images/graph11.png", output_format="auto")

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


sections = ['SQL', 'Python', 'Google Sheets', 'Tableau', 'Looker studio', 'Power BI', 'Amplitude']
selected_section = st.sidebar.selectbox("Оберіть розділ:", sections)


# selected_project = None
if selected_section == 'SQL':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['PostgreSQL', 'Big Query'])
    if selected_project:
        sql(selected_project)


# elif selected_section == 'Bigquery':
#     selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
#     if selected_project:
#         bigquery(selected_project)


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