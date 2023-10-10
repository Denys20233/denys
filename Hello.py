import streamlit as st
import pandas as pd
import plotly.express as px
# from PIL import Image

st.set_page_config(
    page_title="Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    # theme="dark"
)

st.markdown(
    """
    <style>
        body {
            color: #f8f9fa;
            background-color: #343a40;
        }
        .css-1v3fvcr {
            background-color: #343a40;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


hide_st_style = """
<style>
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)


import folium
from streamlit_folium import folium_static


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
    
        st.subheader("Big Query - 1")
        st.write("")
        st.write("Створив запит для отримання таблиці з інформацією про події, користувачів та сесії в GA4. У результаті виконання запиту ми отримали таблицю, що включатиме в себе такі поля:")

        text_sql42 = "event_timestamp - дата та час події (тип даних timestamp)"
        text_sql43 = "user_pseudo_id - анонімний ідентифікатор користувача в GA4"
        text_sql44 = "session_id - ідентифікатор сесії подій в GA4"
        text_sql45 = "event_name - назва події"
        text_sql46 = "country - країна користувача сайту"
        text_sql47 = "device_category - категорія пристрою користувача сайту"
        text_sql48 = "source - джерело відвідування сайту"
        text_sql49 = "medium - medium відвідування сайту"
        text_sql50 = "campaign - назва кампанії відвідування сайту"
    
        formatted_text13 = f"""
        <div>• {text_sql42}</div>
        <div>• {text_sql43}</div>
        <div>• {text_sql44}</div>
        <div>• {text_sql45}</div>
        <div>• {text_sql46}</div>
        <div>• {text_sql47}</div>
        <div>• {text_sql48}</div>
        <div>• {text_sql49}</div>
        <div>• {text_sql50}</div>
        """
        st.markdown(formatted_text13, unsafe_allow_html=True)

        st.write("")


        st.write("Таблиця  включає лише дані за 2021 рік, та дані з таких подій:")

        text_sql51 = "Початок сесії на сайті"
        text_sql52 = "Перегляд товару"
        text_sql53 = "Додавання товару до корзини"
        text_sql54 = "Початок оформлення замовлення"
        text_sql55 = "Додавання інформації про доставку"
        text_sql56 = "Додавання платіжної інформації"
        text_sql57 = "Покупка"
    
        formatted_text14 = f"""
        <div>• {text_sql51}</div>
        <div>• {text_sql52}</div>
        <div>• {text_sql53}</div>
        <div>• {text_sql54}</div>
        <div>• {text_sql55}</div>
        <div>• {text_sql56}</div>
        <div>• {text_sql57}</div>
        """
        st.markdown(formatted_text14, unsafe_allow_html=True)

        st.write("")

        sql_code6 = """SELECT distinct
  TIMESTAMP_MICROS(event_timestamp) as event_date,
  user_pseudo_id,
  (select value.int_value from unnest(event_params) where key = 'ga_session_id') as session_id,
  event_name,
  geo.country,
  device.category,
  traffic_source.source,
  traffic_source.medium,
  traffic_source.name as campaign
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
where _table_suffix between '20210101' and '20211231'
  and event_name in ('session_start', 'view_item_list', 'add_to_cart', 'begin_checkout', 'add_shipping_info', 'add_payment_info', 'purchase')
LIMIT 1000;

"""
        st.write("")
        st.code(sql_code6, language='sql')

        st.subheader("Big Query - 2")
        st.write("")
        st.write("Розрахунок конверсій в розрізі дат та каналів трафіку. Створив запит для отримання таблиці з інформацією про конверсії від початку сесії до покупки. Результуюча таблиця  включає в себе такі поля:")

        text_sql58 = "event_date - дата старту сесії, що отримана з поля event_timestamp"
        text_sql59 = "source - джерело відвідування сайту"
        text_sql60 = "medium - medium відвідування сайту"
        text_sql61 = "campaign - назва кампанії відвідування сайту"
        text_sql62 = "ser_sessions_count - кількість унікальних сесій в унікальних користувачів у відповідну дату та для відповідного каналу трафіку."
        text_sql63 = "visit_to_cart - конверсія від початку сесії на сайті до додавання товару в корзину (у відповідну дату та для відповідного каналу трафіку)"
        text_sql64 = "visit_to_checkout - конверсія від початку сесії на сайті до спроби оформити замвовлення (у відповідну дату та для відповідного каналу трафіку)"
        text_sql65 = "Visit_to_purchase - конверсія від початку сесії на сайті до покупки (у відповідну дату та для відповідного каналу трафіку)"
    
        formatted_text15 = f"""
        <div>• {text_sql58}</div>
        <div>• {text_sql59}</div>
        <div>• {text_sql60}</div>
        <div>• {text_sql61}</div>
        <div>• {text_sql62}</div>
        <div>• {text_sql63}</div>
        <div>• {text_sql64}</div>
        <div>• {text_sql65}</div>
        """
        st.markdown(formatted_text15, unsafe_allow_html=True)

        st.write("")

        sql_code7 = """with CTE_0 as (
select
  Date(TIMESTAMP_MICROS(event_timestamp)) as event_date,
  traffic_source.source as source_of_site,
  traffic_source.medium as medium,
  traffic_source.name as campaign,
  (select value.int_value from unnest(event_params) where key = 'ga_session_id') as session_id,
  user_pseudo_id
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
where _table_suffix between '20210101' and '20211231'
)
select
  event_date,
  source_of_site,
  medium,
  campaign,
  COUNT(DISTINCT CONCAT(user_pseudo_id, CAST(session_id AS STRING))) AS user_sessions_count,
  ((select count(event_name)
          FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
          where _table_suffix between '20210101' and '20211231'
          and event_name = 'add_to_cart') / count(session_id)) * 100  as visit_to_cart,        
  ((select count(event_name)
          FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
          where _table_suffix between '20210101' and '20211231'
          and event_name = 'begin_checkout') / count(session_id)) * 100  as visit_to_checkout,
  ((select count(event_name)
          FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
          where _table_suffix between '20210101' and '20211231'
          and event_name = 'purchase') / count(session_id)) * 100  as visit_to_purchase,
from CTE_0
group by event_date, source_of_site, campaign, medium
"""
        st.write("")
        st.code(sql_code7, language='sql')

        st.subheader("Big Query - 3")
        st.write("")
        st.write("Порівняння конверсії між різними посадковими сторінками:")
        st.write("Для виконання цієї задачі отримав page path (шлях до сторінки без  адреси домену та без параметрів посилання) з page_location в події початку сесії.")
        st.write("Для кожного унікального page path початку сесії порахував такі метрики на основі даних за 2020 рік:")

        text_sql66 = "Кількість унікальних сесій в унікальних користувачів"
        text_sql67 = "Кількість покупок"
        text_sql68 = "Конверсія від початку сесії в покупку"
    
        formatted_text16 = f"""
        <div>• {text_sql66}</div>
        <div>• {text_sql67}</div>
        <div>• {text_sql68}</div>
        """
        st.markdown(formatted_text16, unsafe_allow_html=True)

        st.write("")

        sql_code8 = """with session_table as (
SELECT
  event_bundle_sequence_id AS session_id,
  user_pseudo_id AS user_id,
  REGEXP_REPLACE((SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location'), r'https?://[^/]+', '') AS page_path
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
where _table_suffix between '20200101' and '20201231'
  and event_name = 'session_start'
LIMIT 1000),
purchase_table as (
select
  event_bundle_sequence_id AS session_id,
  user_pseudo_id AS user_id
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
where _table_suffix between '20200101' and '20201231'
  and event_name = 'purchase'
LIMIT 1000
)
select
  session_table.page_path,
  count(distinct session_table.session_id) as unique_sessions,
  count(distinct purchase_table.session_id) as purchase_count,
  ((count(distinct purchase_table.session_id) / 1.0) / count(distinct session_table.session_id)) * 100
from session_table
join purchase_table on purchase_table.user_id = session_table.user_id
group by session_table.page_path
"""
        st.write("")
        st.code(sql_code8, language='sql')


def python(selected_project):

    if selected_project == 'Analysis of YouTube':
        st.subheader(f"Python: Analysis of YouTube")
        st.write("")
        st.write("Я провів аналіз каналів на YouTube з використанням мови програмування Python. У цьому проекті я використовував Jupyter Notebook та бібліотеки, такі як Pandas, Matplotlib.pyplot, FuncFormatter, NumPy та Folium. Мій датасет доступний нижче:")

        dfp1 = pd.read_csv("csv_files/Global YouTube Statistics.csv", encoding='latin-1')
        st.dataframe(dfp1)

        st.write("")
        st.write("")
        st.subheader(f"1. На цьому графіку я вивів топ 10 ютуб каналів за кількістю підписників")
        # st.write("1. На цьому графіку я вивів топ 10 ютуб каналів за кількістю підписників")
        st.image("images/chart1.png", width=900, output_format="auto")
        st.write("У результаті ми бачимо, що найбільше підписників на каналі T-series. Для створення цього графіку я використав такий код:")
        st.write("")
        code_py1 = """
        df_sorted = df.sort_values(by='subscribers', ascending=False)
top_10 = df_sorted.head(10)

plt.figure(figsize=(10, 6))
bars = plt.bar(top_10['Youtuber'], top_10['subscribers'], color='navy')
plt.xlabel('Youtuber')
plt.ylabel('Subscribers')
plt.title(f'Top 10 YouTube channels by subscribers')
plt.xticks(rotation=90, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.0f}M'))

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval / 1e6:.0f}M', ha='center', va='bottom')
    
plt.tight_layout()
        """
        st.code(code_py1, language='python')


        st.write("")
        st.write("")
        st.subheader(f"2. На цьому графіку ми бачимо кількість каналів у яких підписників більше 10 М по кожній країні")
        st.image("images/chart3.png", width=900, output_format="auto")
        st.write("У результаті ми бачимо, що найбільше таких каналів у США та Індії. Для створення цього графіку я використав такий код:")
        st.write("")
        code_py2 = """
        data_10m = df[df['subscribers'] > 1e7]

channels_by_country = data_10m['Country'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.plot(channels_by_country.index, channels_by_country.values, marker='o', linestyle='--', color='navy')

plt.xlabel('Country')
plt.ylabel('Number of Channels')
plt.title('Number of Channels with > 10 M Subscribers by Country')

plt.grid(True)

plt.xticks(rotation=90, ha='right')

plt.tight_layout()
        """
        st.code(code_py2, language='python')


        st.write("")
        st.write("")
        st.subheader(f"3. На цьому графіку ми бачимо топ 10 каналів за кількістю переглядів")
        st.image("images/chart2.png", width=900, output_format="auto")
        st.write("У результаті ми бачимо, що найбільше переглядів у каналі T-series. Для створення цього графіку я використав такий код:")
        st.write("")
        code_py3 = """
        sorted_df1 = df.sort_values(by='video views', ascending=False)
top_10_views = sorted_df1.head(10)

plt.figure(figsize=(10, 6))
bars = plt.bar(top_10_views['Youtuber'], top_10_views['video views'], color='navy')

plt.xlabel('Youtuber')
plt.ylabel('Video Views')
plt.title('Top 10 YouTube Channels by Video Views')

plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e9:.0f}B'))

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval / 1e9:.0f}B', ha='center', va='bottom')

plt.xticks(rotation=90, ha='right')
plt.tight_layout()
        """
        st.code(code_py3, language='python')


        st.write("")
        st.write("")
        st.subheader(f"4. На цьому графіку ми бачимо співвідношення кількості підписників до кількості переглядів")
        st.image("images/chart4.png", width=900, output_format="auto")
        st.write("Якби це не було очевидним, але при меншій кількості переглядів - менша кількість підписників. Для створення цього графіку я використав такий код:")
        st.write("")
        code_py4 = """
        x_column = 'subscribers'
y_column = 'video views'


plt.figure(figsize=(10, 6))
plt.scatter(df[x_column], df[y_column], alpha=0.5, color='blue')

plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e9:.0f}B'))
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.0f}M'))

plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title(f'{x_column} vs {y_column}')
        """
        st.code(code_py4, language='python')


        st.write("")
        st.write("")
        st.subheader(f"5. На цьому графіку ми бачимо кількість каналів по кожній категорії")
        st.image("images/chart5.png", width=900, output_format="auto")
        st.write("Тут ми бачимо, що найбільша кількість каналів у яких багато підписників є в категорії Music та Entertainment. Для створення цього графіку я використав такий код:")
        st.write("")
        code_py5 = """
        x_column = 'subscribers'
y_column = 'video views'


plt.figure(figsize=(10, 6))
plt.scatter(df[x_column], df[y_column], alpha=0.5, color='blue')

plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e9:.0f}B'))
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.0f}M'))

plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title(f'{x_column} vs {y_column}')
        """
        st.code(code_py5, language='python')


        st.write("")
        st.write("")
        st.subheader(f"6. На цій карті ми можемо побачити найбільші каналі по країнам")

        data1 = dfp1[dfp1['subscribers'] > 1e7]
        data1 = data1.dropna(subset=['Latitude', 'Longitude'])

        # Створення мапи Folium
        map = folium.Map(location=[data1['Latitude'].mean(), data1['Longitude'].mean()], zoom_start=2)

        max_subscribers = data1.loc[data1.groupby('Country')['subscribers'].idxmax()]

        for index, row in max_subscribers.iterrows():
            folium.Marker(location=[row['Latitude'], row['Longitude']],
                          popup=f"{row['Youtuber']} - {row['subscribers']} subscribers - {row['Country']}",
                          icon=folium.Icon(color='darkblue')).add_to(map)

        # Вставка мапи у Streamlit
        folium_static(map, width=1100)

        st.write("Наприклад, в Україні найбільший канал це Slivki Show. Для створення цього графіку я використав такий код:")
        st.write("")
        code_py6 = """
        import folium

data1 = df[df['subscribers'] > 1e7]
data1 = data1.dropna(subset=['Latitude', 'Longitude']) # прибираєм nan

map = folium.Map(location=[data1['Latitude'].mean(), data1['Longitude'].mean()], zoom_start=2)

max_subscribers = data1.loc[data1.groupby('Country')['subscribers'].idxmax()]

for index, row in max_subscribers.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']],
                  popup=f"{row['Youtuber']} - {row['subscribers']} subscribers - {row['Country']}",
                  icon=folium.Icon(color='darkblue')).add_to(map)

map
        """
        st.code(code_py6, language='python')

        
    elif selected_project == 'creation and analysis of dataset':
        st.subheader(f"Python: creation and analysis of dataset")
        st.write("")
        st.write("У рамках цього проекту я створив власний датасет, використовуючи інформацію про топ-1000 світових компаній та наповнив його різноманітною інформацією з різних джерел. Після цього я провів аналіз цього датасету, досліджуючи його ключові аспекти.")
        st.write("")
        st.write("Спочатку я взяв основний датасет, прибрав зайві символи та створив 4 стовпчики з показниками:")
        st.write("")
        code_py7 = """
        import pandas as pd
        df = pd.read_csv(r"мій шлях.csv")

        df = df.rename(columns=lambda x: x.strip())

        def convert_to_numeric(value):
    try:
        return pd.to_numeric(value.replace('$', '').replace(',', '').replace('%', '').replace('(', '').replace(')', ''), errors='coerce')
    except ValueError:
        return np.nan

# Застосування функції до відповідних стовпців
df['revenues'] = df['revenues'].apply(convert_to_numeric)
df['profits'] = df['profits'].apply(convert_to_numeric)
df['revenue_percent_change'] = df['revenue_percent_change'].apply(convert_to_numeric)
df['profits_percent_change'] = df['profits_percent_change'].apply(convert_to_numeric)
df['assets'] = df['assets'].apply(convert_to_numeric)
df['market_value'] = df['market_value'].apply(convert_to_numeric)
df['employees'] = df['employees'].apply(convert_to_numeric)

df = df.drop("change_in_rank", axis=1)

df['Average Revenue per Employee'] = df['revenues'] / df['employees'] # Середній дохід на одного працівника
df['Profit Margin'] = df['profits'] / df['revenues']  #  Маржа прибутку
df['Relative Change in Profits'] = df['profits_percent_change'] / 100  #  Відносна зміна прибутку
df['Asset Turnover'] = df['revenues'] / df['assets']  #  Оборот активі
        """
        st.code(code_py7, language='python')

        st.write("")
        st.write("Далі додаємо нові дані та зводимо стовпчики, по яким будемо з'єднувати до спільного регістра:")
        st.write("")
        code_py8 = """
        df1 = pd.read_csv(r"мій шлях")
df2 = pd.read_csv(r"мій шлях.csv")

df1['Name'] = df1['Name'].str.lower()
df2['Name'] = df2['Name'].str.lower()
merged_df1 = pd.merge(df1, df2[['Name', 'marketcap', 'country']], on='Name', how='left')
        """
        st.code(code_py8, language='python')

        st.write("")
        st.write("Додаємо ще декілька стопців з різних джерел та прибираємо рядки для яких не знайшлись спільні значення")
        st.write("")
        code_py9 = """
        df3 = pd.read_csv(r"мій шлях")
        df3['Name'] = df3['Name'].str.lower()
        merged_df2 = pd.merge(merged_df1, df3[['Name', 'cost_to_borrow']], on='Name', how='left')

        df4 = pd.read_csv(r"мій шлях.csv")

        df4['Name'] = df3['Name'].str.lower()
        merged_df3 = pd.merge(merged_df2, df4[['Name', 'total_debt']], on='Name', how='left')

        filtered_df_result = merged_df3[(merged_df3['country'].notna())]
        """

        st.code(code_py9, language='python')


        st.write("")
        st.write("Частина створення датасету була завершина, далі переходимо до аналізу")
        dfp2 = pd.read_csv("csv_files/result.csv", encoding='latin-1')
        st.dataframe(dfp2)
        st.write("")



        st.subheader("1. На цьому графіку ми можемо побачити топ 10 компаній за кількістю співробітників")
        st.write("")

        st.image("images/chart6.png", width=900, output_format="auto")
        st.write("")

        code_py10 = """
        import matplotlib.pyplot as plt
        from matplotlib.ticker import FuncFormatter

        df_sorted1 = filtered_df_result.sort_values(by='employees', ascending=False)
top_10_1 = df_sorted1.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10_1['Name'], top_10_1['employees'], color='navy')
plt.xlabel('Company')
plt.ylabel('Employee')
plt.title(f'Top 10 company of employees')
plt.xticks(rotation=45, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.1f}M'))
plt.tight_layout()
        """

        st.code(code_py10, language='python')

        st.subheader("2. На цьому графіку ми бачимо топ 10 компаній за найбільшим боргом")
        st.write("")

        st.image("images/chart7.png", width=900, output_format="auto")
        st.write("")

        code_py11 = """
        df_sorted2 = filtered_df_result.sort_values(by='total_debt', ascending=False)
top_10_2 = df_sorted2.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10_2['Name'], top_10_2['total_debt'], color='navy')
plt.xlabel('Company')
plt.ylabel('Total debt')
plt.title(f'Top 10 company of total debts')
plt.xticks(rotation=45, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e9:.0f}B'))
plt.tight_layout()
        """

        st.code(code_py11, language='python')


        st.subheader("3. На цьому графіку ми бачимо топ 10 компаній з найбільшими активами ")
        st.write("")

        st.image("images/chart8.png", width=900, output_format="auto")
        st.write("")

        code_py11 = """
        df_sorted3 = filtered_df_result.sort_values(by='assets', ascending=False)
top_10_3 = df_sorted3.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10_3['Name'], top_10_3['assets'], color='navy')
plt.xlabel('Company')
plt.ylabel('Assets')
plt.title(f'Top 10 company of assets')
plt.xticks(rotation=60, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.1f}M'))
plt.tight_layout()
        """

        st.code(code_py11, language='python')

        st.subheader("4. На цьому графіку ми бачимо співвідношення кількості працівників до доходу")
        st.write("")

        st.image("images/chart9.png", width=900, output_format="auto")
        st.write("")

        code_py11 = """
        x_column = 'revenues'
y_column = 'employees'


plt.figure(figsize=(10, 6))
plt.scatter(filtered_df_result[x_column], filtered_df_result[y_column], alpha=0.5, color='blue')

plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.1f}M'))
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e3:.0f}K'))

plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title(f'Scatter Plot: {x_column} vs {y_column}')
        """

        st.code(code_py11, language='python')


        st.subheader("5. На цьому графіку ми бачимо кількість найбільших компаній по країнам")
        st.write("")

        st.image("images/chart10.png", width=900, output_format="auto")
        st.write("")

        code_py12 = """
        companiesby_country = filtered_df_result['country'].value_counts()

plt.figure(figsize=(10, 6))
companiesby_country.plot(kind='line', marker='o')
plt.title('Кількість компаній в кожній країні')
plt.xlabel('Країна')
plt.ylabel('Кількість компаній')
        """

        st.code(code_py12, language='python')


        st.subheader("6. На цьому графіку ми бачимо найдорожчі компанії на ринку")
        st.write("")

        st.image("images/chart11.png", width=900, output_format="auto")
        st.write("")

        code_py13 = """
        plt.figure(figsize=(10, 6))
plt.bar(top_10_4['Name'], top_10_4['market_value'], color='navy')
plt.xlabel('Company')
plt.ylabel('market_value')
plt.title(f'Top 10 company of market_value')
plt.xticks(rotation=60, ha='right')
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x / 1e6:.1f}M'))
plt.tight_layout()
        """

        st.code(code_py13, language='python')


    elif selected_project == 'Проект 3':
        st.write("У цьому проекті я використав такий датасет, на основі якого створив інтерактивні графіки, які можна налаштовувати зліва")
        from dateutil.relativedelta import relativedelta


        df = pd.read_csv("csv_files/games_activity_combined.csv")
        st.dataframe(df)
        df['activity_date'] = pd.to_datetime(df['activity_date'])

        # Створюємо фільтри
        game_filter = st.sidebar.selectbox("Виберіть гру", df["game_activity_name"].unique())
        device_filter = st.sidebar.selectbox("Виберіть тип девайсу", ["Старий", "Новий"])
        date_range = st.sidebar.date_input("Виберіть діапазон дат", [df["activity_date"].min(), df["activity_date"].max()])
        date_range = [pd.to_datetime(date) for date in date_range]
        age_range = st.sidebar.slider("Виберіть діапазон віку", int(df["age"].min()), int(df["age"].max()), (20, 60))

        # Фільтруємо дані за вибраними фільтрами
        filtered_df = df[(df["game_activity_name"] == game_filter) &
                        (df["has_older_device_model"] == (device_filter == "Старий")) &
                        (df["activity_date"].between(date_range[0], date_range[1])) &
                        (df["age"].between(age_range[0], age_range[1]))]

        

        # Побудова лінійного графіка за активністю по днях
        fig_line = px.line(filtered_df.groupby("activity_date").size().reset_index(name="Кількість користувачів"),
                          x="activity_date", y="Кількість користувачів",
                          title="Кількість активних користувачів по днях",
                          labels={"activity_date": "Дата", "Кількість користувачів": "Кількість користувачів"})
        st.plotly_chart(fig_line)


        # 1
        fig_line_age_activity = px.line(filtered_df.groupby(["age", "game_activity_name"]).size().reset_index(name="Кількість користувачів"),
                                x="age", y="Кількість користувачів",
                                color="game_activity_name",
                                title="Кількість користувачів за віком та грою",
                                labels={"age": "Вік", "Кількість користувачів": "Кількість користувачів"})
        st.plotly_chart(fig_line_age_activity)

        # Побудова стовпчикового графіка за кількістю користувачів за мовою
        fig_bar = px.bar(filtered_df.groupby("language").size().reset_index(name="Кількість користувачів"),
                        x="language", y="Кількість користувачів",
                        title="Кількість користувачів за мовою",
                        labels={"language": "Мова", "Кількість користувачів": "Кількість користувачів"})
        st.plotly_chart(fig_bar)

        fig_bar_age_game = px.bar(filtered_df.groupby(["age", "game_activity_name"]).size().reset_index(name="Кількість користувачів"),
                    x="age", y="Кількість користувачів",
                    color="game_activity_name",
                    title="Кількість користувачів за віком та грою",
                    labels={"age": "Вік", "Кількість користувачів": "Кількість користувачів"})
        st.plotly_chart(fig_bar_age_game)

        # 3
        fig_pie_age = px.pie(filtered_df.groupby("age").size().reset_index(name="Кількість користувачів"),
                            names="age", values="Кількість користувачів",
                            title="Розподіл користувачів за віком",
                            labels={"age": "Вік", "Кількість користувачів": "Кількість користувачів"})
        st.plotly_chart(fig_pie_age)

        
        fig_scatter = px.scatter(filtered_df, x="age", y=filtered_df["total_seconds"] / 3600, color="game_activity_name",
                                title="Взаємозв'язок віку та часу гри (в годинах)",
                                labels={"age": "Вік", "total_seconds": "Час гри (в годинах)", "game_activity_name": "Гра"})
        st.plotly_chart(fig_scatter)


    elif selected_project == 'regular expressions':
        import re

        st.subheader("regular expressions")
        
        
        def count_words(text):
            word_count = len(re.findall(r'\b[a-zA-ZА-Яа-я]{2,}\b', text))
            return word_count

        def main():
            st.subheader("Word Count App")

            text0 = st.text_area("Введіть текст:", "")

            if st.button("Підрахувати кількість слів"):
  
                word_count = count_words(text0)
                st.success(f"Кількість слів у вашому тексті: {word_count}")

        # Запуск веб-додатку
        if __name__ == "__main__":
            main()

        st.write("Код цієї програми:")
        code = """
import re

def count_words(text):
    word_count = len(re.findall(r'\b[a-zA-ZА-Яа-я]{2,}\b', text))
    return word_count

def main():
    st.title("Word Count App")

    # Введення тексту користувачем
    text0 = st.text_area("Введіть текст:", "")

    # Кнопка для виклику функції підрахунку слів
    if st.button("Підрахувати кількість слів"):
        # Виклик функції та виведення результату
        word_count = count_words(text0)
        st.success(f"Кількість слів у вашому тексті: {word_count}")

if __name__ == "__main__":
    main()
"""

        # Відображення коду
        st.code(code, language="python")

        st.subheader("Пошук всіх електронних адрес в тексті")
        code = """
       
pattern = r'[A-Za-z0-9._%-+]+@[A-Za-z-.]+\.[A-Za-z]+\b'

list_email = (re.findall(pattern, my_text))

for email in list_email:
    print(email)
"""

        # Відображення коду
        st.code(code, language="python")

        st.subheader("Перевірка паролю не зважаючи на зайві символи та регістр")
        code = """
import re

password_system = 'teST34-45'

pattern = r'[^A-Za-z0-9-]+'


while True:
    password_user = re.sub(pattern, '', input('Введіть пароль з 9-ти символів:'))

    if password_user.lower() == password_system.lower():
        print("Пароль вірний")
        break
    else:
        print("Пароль не вірний, спробуйте ще раз\n")
"""

        # Відображення коду
        st.code(code, language="python")

        st.subheader("Цей скрипт створює абревіатуру з перших букв кожного слова")
        code = """
import re
pattern = r'\b[^0-9\W]'

user_text = input('Введіть речення: ')

word_list = ''.join(re.findall(pattern, user_text))
print(word_list.upper())
"""

        # Відображення коду
        st.code(code, language="python")

        st.subheader("Видалення повторів")
        code = """
import re
my_text = 'Дуже поширена помилка помилка - це лише повторення повторення слова слова.' \
          ' Смішно, чи чи не так? Це - книга книгарні.'

pattern = r'\b(\w+)\s+\1\b'

new_text = re.sub(pattern, r'\1', my_text)
print(my_text)
print()
print(new_text)
"""

        # Відображення коду
        st.code(code, language="python")

        st.subheader("Видалення зайвих пробілів та розміщення рядків з нового рядка")
        code = """
text = ""
pattern = '([.;!?]+)'

text_without_lines = re.sub(r'\s+', ' ', text)
print(text_without_lines)

print()

result_text = re.sub(r'([.;!?]+\s)', r'\1\n', text_without_lines)
print(result_text)
"""

        # Відображення коду
        st.code(code, language="python")

        st.subheader("Пошук всіх військових бригад з тексту")
        code = """
import re
text = ""
print(re.findall(r'[0-9]+(?:th|ed)\s\b[A-Z][A-Za-z]+\b', text))
"""

        # Відображення коду
        st.code(code, language="python")

        st.subheader("Пошук всіх дат з тексту")
        code = """
import re

path = r"мій шлях.txt"


with open(path, 'r') as file:
    text = file.read()


pattern = r'\d{4}'
dates = re.findall(pattern, text)

print('Результат:', dates)
+
pattern = r'[A-Z][a-z]+\s\d{4}'
dates = re.findall(pattern, text)

print('Результат:', dates)

pattern = r'\d{2}\s[A-Z][a-z]+\s\d{4}'
dates = re.findall(pattern, text)

print('Результат:', dates)
"""

        # Відображення коду
        st.code(code, language="python")


        st.subheader("Скрипт який шукає всі версії Python  у тексті")
        code = """
import re

path = r"мій шлях.txt"


with open(path, 'r') as file:
    text = file.read()


pattern = r'\bPython\s+(\d+\.\d+)\b'
result = re.findall(pattern, text)

print('Результат:', result)

pattern = r'\bPython\s+(\d+\.\d+\.\d+)\b'
result1 = re.findall(pattern, text)

print('Результат:', result1)
"""

        # Відображення коду
        st.code(code, language="python")

        
    elif selected_project == 'Проект 5':
        
      st.subheader("Проект 5")
      st.write("У цьому проекті я використав такий датасет, на основі якого створив інтерактивні графіки, які можна налаштовувати зліва")
        
      df = pd.read_csv("csv_files/Adidas Vs Nike.csv")
      st.dataframe(df)

      with st.sidebar:
          # Додаємо фільтри
          price_range = st.slider('Діапазон цін', min_value=df['Sale Price'].min(), max_value=df['Sale Price'].max(), value=(df['Sale Price'].min(), df['Sale Price'].max()))
          rating_range = st.slider('Діапазон рейтингу', min_value=0.0, max_value=5.0, value=(0.0, 5.0), step=0.1)
          selected_models = st.multiselect('Оберіть моделі кросівок', df['Brand'].unique(), default=df['Brand'].unique())

      # Фільтруємо дані
      filtered_data = df[(df['Sale Price'].between(price_range[0], price_range[1])) & 
                        (df['Rating'].between(rating_range[0], rating_range[1])) &
                        (df['Brand'].isin(selected_models))]

      # Тепер можна перейти до створення графіків
      # Графік розсіювання
      scatter_fig = px.scatter(filtered_data, x='Rating', y='Sale Price', color='Brand', title='Scatter Plot of Rating vs Sale Price')
      st.plotly_chart(scatter_fig)

      # Графік стовпчиковий
      bar_fig = px.bar(filtered_data, x='Brand', y='Reviews', title='Bar Chart of Reviews by Brand')
      st.plotly_chart(bar_fig)

      # Графік кругової діаграми
      pie_fig = px.pie(filtered_data, names='Brand', title='Brand Distribution')
      st.plotly_chart(pie_fig)

      # Графік стовпчиків продажів за моделями
      sales_by_model = filtered_data.groupby('Brand')['Sale Price'].sum().reset_index()
      bar_sales_fig = px.bar(sales_by_model, x='Brand', y='Sale Price', title='Total Sales by Brand')
      bar_sales_fig.update_layout(xaxis_title='Brand', yaxis_title='Total Sales')
      st.plotly_chart(bar_sales_fig)

      bar_brand_sales_fig = px.bar(filtered_data.groupby('Brand')['Sale Price'].count().reset_index(), x='Brand', y='Sale Price', title='Number of Shoes Sold by Brand')
      bar_brand_sales_fig.update_layout(xaxis_title='Brand', yaxis_title='Number of Shoes Sold')
      st.plotly_chart(bar_brand_sales_fig)


      line_fig = px.line(filtered_data.groupby('Product Name')['Sale Price'].mean().reset_index(), x='Product Name', y='Sale Price', title='Average Sale Price by Shoe Model')
      line_fig.update_layout(xaxis_title='Shoe Model', yaxis_title='Average Sale Price')

      # Налаштовуємо шрифт для назв моделей
      line_fig.update_layout(
          xaxis=dict(tickfont=dict(size=8)),
          yaxis=dict(tickfont=dict(size=12))
      )

      # Збільшуємо графік у ширину
      line_fig.update_layout(width=1000)

      st.plotly_chart(line_fig)


      # Створюємо другий графік
      discount_fig = px.line(filtered_data.groupby('Product Name')['Discount'].mean().reset_index(), x='Product Name', y='Discount', title='Average Discount by Shoe Model')
      discount_fig.update_layout(xaxis_title='Shoe Model', yaxis_title='Average Discount')

      # Налаштовуємо шрифт для назв моделей
      discount_fig.update_layout(
          xaxis=dict(tickfont=dict(size=8)),
          yaxis=dict(tickfont=dict(size=12))
      )

      # Збільшуємо графік у ширину
      discount_fig.update_layout(width=1000)

      st.plotly_chart(discount_fig)






      
        

        





       







       

        


def visualization(selected_project):

    if selected_project == 'Tableau':
        st.markdown("## [Tableau - 1](https://public.tableau.com/app/profile/.12596403/viz/Homework_6-2/Homework22)")
        st.write("")
        st.write("У цьому проекті я використав такий датасет:")
        
        df1 = pd.read_csv("csv_files/saas_revenue.csv")
        st.dataframe(df1)

        st.write("")
        st.write("У воркбуці Tableau створив обчислювані поля для таких метрик:")

        sentences_t1 = [
        "Total Revenue",
        "Paid Users count",
        "Average Revenue Per Paid Users"
        ]

        form_text_t1 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t1]) + "</div>"
        st.markdown(form_text_t1, unsafe_allow_html=True)

        st.write("")

        st.write("Після цього створив наступні діаграми:")

        sentences_t2 = [
        "Діаграма, що дозволяє візуально порівняти загальне Revenue для кожної з комбінацій локація + продукт.",
        "Діаграма, що дозволяє порівняти загальне Revenue по кожній з локацій.",
        "Діаграма, на якій вказано загальне Revenue по місяцях з розбивкою за продуктом.",
        "Діаграма, що показує ARPPU та Paid Users Сount помісячно.",
        "Box plot для порівняння сум транзакцій.",
        "діаграму, що показує як змінюється частка кожної локації в Revenue з часом."
        ]

        form_text_t2 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t2]) + "</div>"
        st.markdown(form_text_t2, unsafe_allow_html=True)

        st.write("")
        st.write("Створив дашборд з головними графіками, на мою думку. Додав фільтри з локацією, продуктом та датою.")

        st.write("")
        st.image("images/tableau1.jpg", output_format="auto")
        st.write("")


        st.markdown("## [Tableau - 2](https://public.tableau.com/app/profile/.12596403/viz/Homework_6-3/Dashboard12)")
        st.write("")
        st.write("У цьому проекті я використав такий датасет:")
        
        df2 = pd.read_csv("csv_files/games_activity_combined.csv")
        st.dataframe(df2)

        st.write("")
        st.write("В новому воркбуці створив три аркуші:")
        st.write("Аркуш 1. З розбивкою помісячно вивів дві метрики:")

        sentences_t3 = [
        "Загальна кількість користувачів ігор.",
        "Відсоток від загальної кількості користувачів, що проводили будь-яку кількість часу в активностях, повїязаних з “Battle pass”."
        ]

        form_text_t3 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t3]) + "</div>"
        st.markdown(form_text_t3, unsafe_allow_html=True)

        st.write("")

        st.write("Аркуш 2. З розбивкою помісячно вивів середній на гравця час, проведений у грі.")

        sentences_t4 = [
        "До аркуша додав Label з середньою на гравця кількістю годин та хвилин, проведених у грі.",
        "Зробив Label текстовим полем і відобразив час у форматі “кількість годин: кількість хвилин”“HH:MM”"
        ]

        form_text_t4 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t4]) + "</div>"
        st.markdown(form_text_t4, unsafe_allow_html=True)

        st.write("Аркуш 3. Створив теплову карту з даними про середню кількість часу проведеного в грі за вимірами:")

        sentences_t5 = [
        "Вікова групою гравців з кроком в 5 років. ",
        "Квартал дати активності"
        ]

        form_text_t5 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t5]) + "</div>"
        st.markdown(form_text_t5, unsafe_allow_html=True)

        st.write("Зібрав всі три аркуша в одному дашборді та додав фільтри:")

        sentences_t6 = [
        "Дата активності",
        "Вікова група",
        "Назва гри",
        "Мова девайсу користувача"
        ]

        form_text_t6 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t6]) + "</div>"
        st.markdown(form_text_t6, unsafe_allow_html=True)

        st.write("")
        st.image("images/tableau2.jpg", output_format="auto")
        st.write("")

        st.markdown("## [Tableau - 3](https://public.tableau.com/app/profile/.12596403/viz/Homework3bonus_16947992656080/Dashboard1)")
        st.write("")
        st.write("У цьому проекті я використав інший датасет")

        st.write("")
        st.write("В новому воркбуці створив три аркуші:")
        st.write("")
        st.write("Аркуш 1. Середня кількість днів, що йдуть на доставку замовлення для кожного типу доставки (Ship mode)")
        st.write("Аркуш 2. Кількість замовлень в розбивці за кількістю днів на доставку. Наприклад, доставлено за 0 днів - X замовлень, доставлено за 1 день - Y замовлень")
        st.write("Аркуш 3. Середня кількість днів, що йдуть на доставку замовлення в кожному штаті в США, з візуалізацією на мапі і використанням градієнту.")
        st.write("")
        st.write("Зібрав три аркуша в одному дашборді та додав фільтри:")

        sentences_t7 = [
        "Дата замовлення",
        "Сегмент",
        "Тип доставки"
        ]

        form_text_t7 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t7]) + "</div>"
        st.markdown(form_text_t7, unsafe_allow_html=True)

        st.write("")
        st.image("images/tableau3.jpg", output_format="auto")
        st.write("")


        st.markdown("## [Tableau - 4](https://public.tableau.com/app/profile/.12596403/viz/Homework4_16948736309800/Cohortanalysis)")
        st.write("")
        st.write("У цьому проекті я використав минулий датасет з Tableau - 1")

        st.write("")
        st.write("Аркуш 1. New MRR - сума revenue, що була отримана від нових користувачів протягом того календарного місяця, коли вони стали платними.")
        st.write("Аркуш 2. Total Revenue на одній вертикальній осі та зміна Total Revenue у відсотках відносно попереднього місяця на другій осі.")
        st.write("Аркуш 3. Таблиця для когортного аналізу Revenue від користувачів:")
        sentences_t8 = [
        "В рядках перший місяць, коли користувач став платним.",
        "В стовпчиках - кількість місяців, що пройшла від першого місяця оплати (тобто від місяця у відповідному рядку).",
        "В таблиці виводяться значення Total Revenue у відповідний період для відповідної когорти.",
        "Таблиця залита градієнтом за показником співвідношення суми Revenue у відповідній клітині до суми Revenue в перший місяць когорти."
        ]

        form_text_t8 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t8]) + "</div>"
        st.markdown(form_text_t8, unsafe_allow_html=True)

        st.write("")
        st.write("Зібрав три аркуша в одному дашборді та додав до дашборду фільтри за локацією та датою.")

        st.write("")
        st.image("images/tableau4.jpg", output_format="auto")
        st.write("")

        st.markdown("## [Tableau - 5](https://public.tableau.com/app/profile/.12596403/viz/Homework5_16953255791190/Dashboard1_1)")
        st.write("")
        st.write("У цьому проекті я використав такий датасет")

        df3 = pd.read_csv("csv_files/onboarding_funnel_product.csv")
        st.dataframe(df3)
        st.write("")
        st.write("Використовуючи дані з файлу, створив дашборд з такими складовими:")
        st.write("1. Три окремих блока з числами:")

        sentences_t9 = [
        "Кількість зареєстрованих користувачів",
        "кількість користувачів, що почали trial перiод",
        "кількість користувачів, що оплатили."
        ]

        form_text_t9 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_t9]) + "</div>"
        st.markdown(form_text_t9, unsafe_allow_html=True)

        st.write("")
        st.write("2. Графік з кількістю реєстрацій та конверсією з реєстрації в trial в кожному місяці реєстрації.")
        st.write("3. Графік з середньою кількістю днів від реєстрації до оплати в кожному місяці реєстрації.")
        st.write("4. Діаграму у вигляді воронки, що відображає проходження користувачами кроків з файла.")
        st.write("5. Додав інтерактив до дашборду за допомогою Actions та Parameters. Коли користувач дашборда клікає по певному блоку з цифрами - графік перебудовується")

        st.write("")
        st.image("images/tableau5.jpg", output_format="auto")
        st.write("")
        





    elif selected_project == 'Power BI':
        st.subheader(f"Power BI")
        st.write("In progress...")


    elif selected_project == 'Looker studio':
        st.markdown("## [Looker studio](https://lookerstudio.google.com/reporting/cb4dd091-e015-499f-8cb3-03bed143b0ea)")
        st.write("")
        st.write("В Google Looker Studio створив новий звіт та налаштував джерело даних:")
        st.write("В звіті створив нові поля:")

        text_looker1 = "Сума Ad Spend"
        text_looker2 = "CPC"
        text_looker3 = "CPM"
        text_looker4 = "CTR"
        text_looker5 = "ROMI"
    
        form_text_looker1 = f"""
        <div>• {text_looker1}</div>
        <div>• {text_looker2}</div>
        <div>• {text_looker3}</div>
        <div>• {text_looker4}</div>
        <div>• {text_looker5}</div>
        """
        st.markdown(form_text_looker1, unsafe_allow_html=True)

        st.write("")

        st.write("В дашборд додав три чарти:")

        text_looker6 = "Комбіновану діаграму з датою показу реклами на горизонтальній осі, та з сумою Ad Spend та ROMI за кожен місяць на двох вертикальних осях"
        text_looker7 = "Лінійний графік з кількістю активних кампаній в кожен місяць показу реклами."
        text_looker8 = "Таблицю зі стовпчиками та тепловими картами, де у якості dimension виставлена назва кампанії, а у якості метрик - сумарний Ad Spend, CPC, CPM, CTR, ROMI."
    
        form_text_looker2 = f"""
        <div>• {text_looker6}</div>
        <div>• {text_looker7}</div>
        <div>• {text_looker8}</div>
        """
        st.markdown(form_text_looker2, unsafe_allow_html=True)

        st.write("")

        st.write("Додав до звіта фільтри за назвою кампаній та за датою показу реклами.")

        st.write("")
        st.image("images/Looker1.png", output_format="auto")


    elif selected_project == 'Amplitude':
        st.subheader(f"Amplitude")
        st.write("")
        st.write("У Demo Amplitude обрав проєкт Media Streaming - Analytics та створив когорту, що задана наступними параметрами:")

        sentences_a1 = [
        "Країна: США",
        "Платформа: iOS або Android",
        "Користувачі, що вперше виконали дію Welcome протягом червня 2023"
        ]

        form_text_a1 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences_a1]) + "</div>"
        st.markdown(form_text_a1, unsafe_allow_html=True)

        st.write("")
        st.image("images/amp0.jpg", output_format="auto")
        st.write("")
        
        st.write("На основі цієї когорти створив наступні візуалізації:")
        st.write("1. Воронка онбордингу користувача у послідовності Welcome - User Sign Up - Main Landing Screen - Search Song or Video - Play Song or Video, розбита за платформою")

        st.write("")
        st.image("images/Amp1.jpg", output_format="auto")
        st.write("")

        st.write("2. Конверсія у проходження воронки онбордингу поденно, розбита за платформою")

        st.write("")
        st.image("images/Amp2.jpg", output_format="auto")
        st.write("")

        st.write("3. Час, за який користувач проходить онбординг поденно, розбитий за платформою")

        st.write("")
        st.image("images/Amp3.jpg", output_format="auto")
        st.write("")

        st.write("4. Динаміка кількості користувачів, що виконують Play Song or Video та користувачів, що виконують будь-який активний івент поденно")

        st.write("")
        st.image("images/Amp4.jpg", output_format="auto")
        st.write("")

        st.write("5. Середня кількість івентів на користувача поденно: будь-який активний івент та Play Song or Video")

        st.write("")
        st.image("images/Amp5.jpg", output_format="auto")
        st.write("")

        st.write("6. Графік Retention користувачів з івенту Welcome в будь-який активний івент та Play Song or Video у вигляді стовпчикової діаграми")

        st.write("")
        st.image("images/Amp6.jpg", output_format="auto")
        st.write("")

        st.write("7. Створив Journey Map користувача від старту сесії до Play Song or Video.")

        st.write("")
        st.image("images/Amplitude_+.jpg", output_format="auto")
        st.write("")

def google_sheets(selected_project):
    
    if selected_project == 'Проект 1':
        st.markdown("## [Проект 1](https://docs.google.com/spreadsheets/d/1WI4--LgLHITuZwYX_EVYSmZLmvElRT41s8-btiXiGL4/edit?usp=sharing)")
        
        st.write("")
        st.write("У цьому проекті я рахував продуктові метрики за допомогою Google Sheets та оцінював ефективність витрат на залучення користувачів. А саме:")

        text_google1 = "Total revenue - загальний revenue гри."
        text_google2 = "Paid users count - загальна кількість користувачів, що платять."
        text_google3 = "CR to Paid - конверсія з користувачів в платних користувачів у відсотках."
        text_google4 = "ARPPU - середній revenue на користувача, який платить."
        text_google5 = "Average Age (paid users) - середній вік користувачів, які платять."
        text_google6 = "Median age (paid users) - медіанний вік користувачів, які платять."
        text_google7 = "Minimum age (paid users) - мінімальний вік користувачів, які платять."
        text_google8 = "Maximum age (paid users) - максимальний вік користувачів, які платять."
    
        form_text_google1 = f"""
        <div>• {text_google1}</div>
        <div>• {text_google2}</div>
        <div>• {text_google3}</div>
        <div>• {text_google4}</div>
        <div>• {text_google5}</div>
        <div>• {text_google6}</div>
        <div>• {text_google7}</div>
        <div>• {text_google8}</div>
        """
        st.markdown(form_text_google1, unsafe_allow_html=True)

        st.write("")
        st.write("Додав строку “Total” з загальними значеннями кожної метрики по всім продуктам одночасно")
        st.write("")
        st.image("images/google sheets.jpg", output_format="auto")
        st.write("")

        st.write("У цьому завданні використовував такі функції:")

        sentences = [
        "SUM",
        "SUMIF",
        "COUNTIF",
        "AVERAGEIF",
        "AVERAGE",
        "MEDIAN",
        "MIN",
        "MINIFS",
        "MAX",
        "MAXIFS"
        ]

        form_text_google2 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences]) + "</div>"
        st.markdown(form_text_google2, unsafe_allow_html=True)

        st.write("")

        st.write("Також,  знизу під таблицею написав висновки на такі запитання:")

        sentences1 = [
        "Чому ігри під номером 1 і 2 можуть мати нижчу CR to Paid конверсію в оплату?",
        "У чому може полягати причина різниці ARPPU між іграми?",
        "Як би ти перевірив свої гіпотези?",
        "Які рекомендації ти мiг би дати менеджерам гри номер 2?"
        ]

        form_text_google3 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences1]) + "</div>"
        st.markdown(form_text_google3, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets1.jpg", output_format="auto")

    elif selected_project == 'Проект 2':
        st.markdown("## [Проект 2](https://docs.google.com/spreadsheets/d/1wG7KmAhwDI026dpEWBgSbs3239hBSvbWDSrsfDkr7K4/edit?usp=sharing)")
        st.write("")
        st.write("У файлі на листі “active users” для віку користувачів визначив:")

        sentences2 = [
        "Середній вік",
        "Standard deviation (стандартне вiдхилення)",
        "Медіану",
        "Іnterquartile range (iнтерквартильний розмах)",
        "10 перцентиль віку",
        "90 перцентиль віку"
        ]

        form_text_google4 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences2]) + "</div>"
        st.markdown(form_text_google4, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets2.jpg", output_format="auto")
        st.write("")

        st.write("Розрахував DAU, WAU та stickiness користувачів. Для цього:")

        sentences3 = [
        "На листі “activity” додав  колонку week_start_date. Використовув формули для виведення дати початку тижня для кожної дати у колонці activity_date.",
        "Створив лист “DAU” з колонкою activity_date. У цій колонці вивів унікальні дати активності (activity_date) з листа “activity.",
        "Створив на листі “DAU” колонку DAU і вивів у ній унікальну кількість користувачів, які проводили час на продукті у відповідну дату.",
        "Створив на листі “DAU” колонку week_start_date та порахував його значення так само, як  це робив на листі “activity.",
        "Створив лист “WAU” з колонкою week_start_date.",
        "Створив на листі “WAU” колонку WAU і в ній вивів  унікальну кількість користувачів, які проводили час на продукті у відповідний тиждень.",
        "Створив на листі “WAU” колонку Average DAU і в ній вивів середній DAU за відповідний тиждень. Для цього використовував дані з листа “DAU” та функції SUMIF та COUNTIF.",
        "Створив на листі “WAU” колонку DAU/WAU та в ній вивів співвідношення Average DAU до WAU у відповідний тиждень."
        ]

        form_text_google5 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences3]) + "</div>"
        st.markdown(form_text_google5, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets 3.jpg", output_format="auto")
        st.write("")
        st.image("images/google sheets 4.jpg", output_format="auto")
        st.write("")
        st.write("У цьому завданні використовував такі функції:")
        
        sentences4 = [
        "AVERAGE",
        "STDEV",
        "MEDIAN",
        "PERCENTILE",
        "B2-WEEKDAY(B2;2)+1",
        "UNIQUE",
        "COUNTUNIQUEIFS",
        "SUMIF",
        "COUNTIF"
        ]

        form_text_google6 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences4]) + "</div>"
        st.markdown(form_text_google6, unsafe_allow_html=True)

        st.write("")
        st.subheader(f"Проект 2.1")
        st.write("")
        st.write("Спрогнозував DAU та WAU:")
        st.write("")

        sentences5 = [
        "На листі “WAU” додав 20 нових рядків із датами старту тижнів",
        "За допомогою функцій ROUND та FORECAST спрозгнозував значення WAU та DAU для нових тижнів.",
        "Заповнив колонку DAU/WAU для нових тижнів."
        ]

        form_text_google7 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences5]) + "</div>"
        st.markdown(form_text_google7, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets 5.jpg", output_format="auto")
        st.write("")

        st.subheader(f"Проект 2.2")
        st.write("")
        st.write("Побудував 4 чарти:")
        st.write("1. Чарт із даними зі сторінки “active users”. Це  горизонтальний bar chart, який відображає кількість користувачів за кожним language.")
        st.write("")
        st.image("images/google sheets 6.jpg", output_format="auto")
        st.write("")

        st.write("2. Чарт із даними зі сторінки “active users”. Це pie chart, який показує розбивку користувачів за ознакою has_older_device_model.")
        st.write("")
        st.image("images/google sheets 7.jpg", output_format="auto")
        st.write("")

        st.write("3. Чарт із даними зі сторінки “WAU”, що містить на горизонтальній осі тижні, а також дві вертикальні осі: WAU та DAU/WAU.")
        st.write("")
        st.image("images/google sheets 8.jpg", output_format="auto")
        st.write("")

        st.write("4. Чарт із даними зі сторінки “WAU”, що містить на горизонтальній осі тижні, а на вертикальній осі - значення WAU.")
        st.write("")
        st.image("images/google sheets 9.jpg", output_format="auto")
        st.write("")

        st.subheader(f"Проект 2.3")
        st.write("")
        st.write("Робота з текстовими функціями та датами в Google Sheets:")
        st.write("")

        sentences6 = [
        "На листі “activity” розбив колонку game_activity_name на дві частини: назва гри та назву активаності.",
        "8 назв активностей обʼєднав в 5 типів активності та вивів тип активності в листі “activity” окремою колонкою",
        "На листі “activity” створив колонку з мовою користувача та заповни її, використовуючи дані з листа “active users",
        "На листі “activity” створив три колонки, що є похідними від колонки activity_date: a. Activity month — місяць активності, тобто місяць, до якого входить activity_date. b. First activity month — перший місяць активності для кожного користувача. c. Activity month number — номер місяця активності. Тобто, скільки місяців пройшло від First activity month до Activity month."
        ]

        form_text_google8 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences6]) + "</div>"
        st.markdown(form_text_google8, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets 10.jpg", output_format="auto")
        st.write("")

        st.write("У цьому завданні використовував такі функції:")

        sentences8 = [
        "LEFT",
        "FIND",
        "RIGHT",
        "VLOOKUP",
        "DATE",
        "YEAR",
        "MONTH",
        "MINIFS",
        "DATEDIF"
        ]

        form_text_google10 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences8]) + "</div>"
        st.markdown(form_text_google10, unsafe_allow_html=True)
        st.write("")
        st.subheader(f"Проект 2.4")
        st.write("")
        st.write("Когортний аналіз")
        st.write("")

        sentences7 = [
        "Створив новий лист “Cohort analysis” із pivot table, що використовує дані з листа “activity",
        "У pivot table вивів у рядках Activity month number та як values — кількість унікальних юзерів.",
        "Візуалізував кількість користувачів у кожен місяць активності. Створив line chart із горизонтальною віссю — Activity month number та вертикальною — кількістю користувачів, які мають відповідний month number."
        ]

        form_text_google9 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences7]) + "</div>"
        st.markdown(form_text_google9, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets 11.jpg", output_format="auto")
        st.write("")

        st.write("")
        st.image("images/google sheets 12.jpg", output_format="auto")
        

        st.subheader(f"Проект 2.5")
        st.write("")
        st.write(" Побудував таблиці для когортного аналізу:")
        st.write("")

        sentences9 = [
        "На окремому листі створив pivot table, що використовує дані з листа “activity”",
        "У pivot table вивів у рядках First activity month, у колонках — Activity month number та як values — кількість унікальних юзерів."
        ]

        form_text_google11 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences9]) + "</div>"
        st.markdown(form_text_google11, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets 13.jpg", output_format="auto")
        st.write("")

        sentences10 = [
        "Знизу під pivot table створив таблицю, яка відображатиме ті ж дані, що й pivot table, але замість values (кількість унікальних юзерів) вивів retention rate у відповідній клітині.",
        "Зробив так, щоб друга таблиця зменшувалася чи збільшувалася одночасно з pivot table.",
        "Застосував до обох таблиць conditional formatting, щоб підсвітити найбільші та найменші значення."
        ]

        form_text_google12 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences10]) + "</div>"
        st.markdown(form_text_google12, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets 14.jpg", output_format="auto")

        st.write("")

        sentences11 = [
        "Поряд із таблицею додав три зрізи: назва гри, тип активності та мова користувача."
        ]

        form_text_google13 = "<div>" + "</div><div>".join([f"• {sentence}" for sentence in sentences11]) + "</div>"
        st.markdown(form_text_google13, unsafe_allow_html=True)

        st.write("")
        st.image("images/google sheets 15.jpg", output_format="auto")

def about_me(selected_project):
    
    if selected_project == 'Resume':
        st.subheader("About me")
        st.image("images/Знімок екрана 2023-10-10 162023.png", output_format="auto")

        contact_info = """
        **Connect with me:**
        - 067 689 32 68 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp; - [Telegram](https://t.me/your_telegram_link)
        - dnpidgainiy2005@gmail.com &emsp;&emsp;&emsp;&emsp;&emsp; - [LinkedIn](https://www.linkedin.com/in/your_linkedin_profile)
        """


        st.markdown(contact_info, unsafe_allow_html=True)
        

        

        



st.title('Портфоліо')


sections = ['About me', 'SQL', 'Python', 'Visualization', 'Google Sheets']
selected_section = st.sidebar.selectbox("Оберіть розділ:", sections)


# selected_project = None

if selected_section == 'About me':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Resume'])
    if selected_project:
        about_me(selected_project)


elif selected_section == 'SQL':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['PostgreSQL', 'Big Query'])
    if selected_project:
        sql(selected_project)


elif selected_section == 'Python':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Analysis of YouTube', 'creation and analysis of dataset', 'Проект 3', 'regular expressions', 'Проект 5'])
    if selected_project:
        python(selected_project)


elif selected_section == 'Visualization':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Tableau', 'Power BI', 'Looker studio', 'Amplitude'])
    if selected_project:
        visualization(selected_project)


elif selected_section == 'Google Sheets':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2'])
    if selected_project:
        google_sheets(selected_project)
