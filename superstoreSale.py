import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('superstore_dataset2011-2015.csv', encoding='ISO-8859-1')

st.sidebar.title("Hypothesis")
hypothesis = st.sidebar.radio("Select a Hypothesis", [
    "Technology products have the highest profit margin compared to other product categories.",
    "The East region has the highest sales compared to other regions.",
    "Sales are higher during certain months of the year.",
    "Orders with same-day shipping have the lowest rate of returned products.",
    "The company's profit is more on weekdays than on weekends."
])

st.title("Superstore Sales Analytics Dashboard")

if hypothesis == "Technology products have the highest profit margin compared to other product categories.":
    plt.figure(figsize=(8, 5))
    category_wise_profit = data.groupby('Category')['Profit'].sum()
    fig, ax = plt.subplots()
    ax.bar(category_wise_profit.index, category_wise_profit.values)
    ax.set_title('Category wise profit')
    ax.set_xlabel('Category')
    ax.set_ylabel('Total Profit')
    st.pyplot(fig)

    st.write("Result : Technology products have the highest marginal profit compared to other product catagories. Hence True")

elif hypothesis == "The East region has the highest sales compared to other regions." :
    region_wise_sales = data.groupby('Region')['Sales'].sum()
    fig, ax = plt.subplots()
    ax.bar(region_wise_sales.index, region_wise_sales.values)
    ax.set_title('Region wise sales')
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Sales')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    st.write("Result : The hypothesis is not correct. As the Central region carries the highest sales. Hence False")

elif hypothesis == "Sales are higher during certain months of the year." :
    data['Order Month'] = pd.DatetimeIndex(data['Order Date']).month
    monthly_sales = data.groupby('Order Month')['Sales'].sum()
    fig, ax = plt.subplots()
    ax.plot(monthly_sales.index, monthly_sales.values)
    ax.set_title('Monthly sales')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Sales')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig) 

    st.write("Result : Sales are higher during the last two months of the year. Hence True")

elif hypothesis == "Orders with same-day shipping have the lowest rate of returned products." :
    total_orders_by_shipping_mode = data.groupby('Ship Mode').size()
    returned_orders_by_shipping_mode = data[data['Profit']<0].groupby('Ship Mode').size()
    returned_percentage_order_by_shipping_mode = (returned_orders_by_shipping_mode/total_orders_by_shipping_mode)*100
    fig, ax = plt.subplots()
    ax.bar(returned_percentage_order_by_shipping_mode.index, returned_percentage_order_by_shipping_mode.values)
    ax.set_title('Returned Product Percentage by Shipping Mode')
    ax.set_xlabel('Shipping Mode')
    ax.set_ylabel('Return Percentage')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig) 

    st.write("Result : The same day shipping mode has the lowest percentage of return percentage. Hence True")

elif hypothesis == "The company's profit is more on weekdays than on weekends.":
    data['Order Day'] = pd.DatetimeIndex(data['Order Date']).day_name()
    day_wise_profit = data.groupby('Order Day')['Profit'].sum()
    fig, ax = plt.subplots()
    ax.bar(day_wise_profit.index, day_wise_profit.values)
    ax.set_title('Day wise profit')
    ax.set_xlabel('Day of the week')
    ax.set_ylabel('Total Profit')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig) 

    st.write("Result : The company gains less profit on Saturdays and Sundays. Hence False")
