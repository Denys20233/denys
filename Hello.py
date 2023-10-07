import streamlit as st
import pandas as pd
from PIL import Image


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
    st.subheader(f"Python - {selected_project}")



    if selected_project == 'Jupyter notebook 1':
        st.write(f"111111111")
        st.write(f"111111111")
        st.write(f"111111111")
        st.write(f"2")
        st.image("images/graph11.png", output_format="auto")
        st.image("images/graph11.png", output_format="auto")
       

    elif selected_project == 'Проект 2':
        st.write(f"2222222222")


    elif selected_project == 'Проект 3':
        st.write(f"333333333333")


def visualization(selected_project):

    if selected_project == 'Tableau':
        st.subheader(f"Tableau 1")
        st.write(f"1")
        

    elif selected_project == 'Power BI':
        st.subheader(f"Power BI")
        st.write(f"2")


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
        
        # st.image("images/Looker 2.png", output_format="auto")
        # image1 = Image.open("images/Looker 2.png")
        # image1.show()

        st.write("12")

        # try:
        #   image1 = Image.open("images/Looker 2.png")
        #   image1.show()
        # except FileNotFoundError as e:
        #     print("File not found. Details:", e)

        image_path = "images/Looker 2.png"

        try:
            image1 = Image.open(image_path)
            st.image(image1, caption="Looker 2 Image", use_column_width=True)
        except FileNotFoundError as e:
            st.error("File not found. Details: {}".format(e))
        
        


    elif selected_project == 'Amplitude':
        st.subheader(f"Amplitude")
        st.write(f"4")




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

st.title('Портфоліо')


sections = ['SQL', 'Python', 'Visualization', 'Google Sheets']
selected_section = st.sidebar.selectbox("Оберіть розділ:", sections)


# selected_project = None
if selected_section == 'SQL':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['PostgreSQL', 'Big Query'])
    if selected_project:
        sql(selected_project)


elif selected_section == 'Python':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Jupyter notebook 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        python(selected_project)


elif selected_section == 'Visualization':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Tableau', 'Power BI', 'Looker studio', 'Amplitude'])
    if selected_project:
        visualization(selected_project)


elif selected_section == 'Google Sheets':
    selected_project = st.sidebar.selectbox("Оберіть проект:", ['Проект 1', 'Проект 2', 'Проект 3'])
    if selected_project:
        google_sheets(selected_project)
