

import pandas as pd
import json
import os
import mysql.connector
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import PIL
from PIL import Image
import git

def git_connect():
    try:
        git.Repo.clone_from( 'https://github.com/PhonePe/pulse.git', 'pulse')
    except:
        pass

git_connect()



Path_1 = "C:/Users/susmi/pulse/data/aggregated/transaction/country/india/state/"
Agg_tran_state_list = os.listdir(Path_1)

Agg_tra = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in Agg_tran_state_list:
    p_i = Path_1 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            A = json.load(Data)
            
            for l in A['data']['transactionData']:
                Name = l['name']
                count = l['paymentInstruments'][0]['count']
                amount = l['paymentInstruments'][0]['amount']
                Agg_tra['State'].append(i)
                Agg_tra['Year'].append(j)
                Agg_tra['Quarter'].append(int(k.strip('.json')))
                Agg_tra['Transaction_type'].append(Name)
                Agg_tra['Transaction_count'].append(count)
                Agg_tra['Transaction_amount'].append(amount)
                
df_agg_trans= pd.DataFrame(Agg_tra)
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

df_agg_trans['State'] = df_agg_trans['State'].replace(dict(zip(Agg_tran_state_list, custom_state_list)))



Path_2 = "C:/Users/susmi/pulse/data/aggregated/user/country/india/state/"
Agg_user_state_list = os.listdir(Path_2)

Agg_user = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'User_Count': [], 'User_Percentage': []}

for i in Agg_user_state_list:
    p_i = Path_2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            B = json.load(Data)
            
            try:
                for l in B["data"]["usersByDevice"]:
                    brand_name = l["brand"]
                    count_ = l["count"]
                    ALL_percentage = l["percentage"]
                    Agg_user["State"].append(i)
                    Agg_user["Year"].append(j)
                    Agg_user["Quarter"].append(int(k.strip('.json')))
                    Agg_user["Brands"].append(brand_name)
                    Agg_user["User_Count"].append(count_)
                    Agg_user["User_Percentage"].append(ALL_percentage*100)
            except:
                pass

df_agg_user = pd.DataFrame(Agg_user)
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

df_agg_user['State'] = df_agg_user['State'].replace(dict(zip(Agg_user_state_list, custom_state_list)))



Path_3 = "C:/Users/susmi/pulse/data/map/transaction/hover/country/india/state/"
map_tra_state_list = os.listdir(Path_3)

Map_tra = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in map_tra_state_list:
    p_i = Path_3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            C = json.load(Data)
            
            for z in C["data"]["hoverDataList"]:
                District = z["name"]
                count = z["metric"][0]["count"]
                amount = z["metric"][0]["amount"]
                Map_tra['State'].append(i)
                Map_tra['Year'].append(j)
                Map_tra['Quarter'].append(int(k.strip('.json')))
                Map_tra["District"].append(District)
                Map_tra["Transaction_count"].append(count)
                Map_tra["Transaction_amount"].append(amount)
                
df_map_trans = pd.DataFrame(Map_tra)
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

df_map_trans['State'] = df_map_trans['State'].replace(dict(zip(map_tra_state_list, custom_state_list)))



Path_4 = "C:/Users/susmi/pulse/data/map/user/hover/country/india/state/"
map_user_state_list = os.listdir(Path_4)

Map_user = {"State": [], "Year": [], "Quarter": [], "District": [], "Registered_User": [],"App_opens":[]}

for i in map_user_state_list:
    p_i = Path_4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            for z_key, z_value in D['data']['hoverData'].items():
                            district = z_key.split(' district')[0]
                            reg_user = z_value['registeredUsers']
                            app_opens = z_value['appOpens']
                            Map_user['State'].append(i)
                            Map_user['Year'].append(j)
                            Map_user['Quarter'].append(k[0])
                            Map_user['District'].append(district)
                            Map_user['Registered_User'].append(reg_user)
                            Map_user['App_opens'].append(app_opens)
                
df_map_user = pd.DataFrame(Map_user)
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

df_map_user['State'] = df_map_user['State'].replace(dict(zip(map_user_state_list, custom_state_list)))



Path_5 = "C:/Users/susmi/pulse/data/top/transaction/country/india/state/"
top_tra_state_list = os.listdir(Path_5)

Top_tra = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Transaction_count': [], 'Transaction_amount': []}

for i in top_tra_state_list:
    p_i = Path_5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            E = json.load(Data)
            
            for l in E['data']['pincodes']:
                Name = l['entityName']
                count = l['metric']['count']
                amount = l['metric']['amount']
                Top_tra['State'].append(i)
                Top_tra['Year'].append(j)
                Top_tra['Quarter'].append(int(k.strip('.json')))
                Top_tra['District_Pincode'].append(Name)
                Top_tra['Transaction_count'].append(count)
                Top_tra['Transaction_amount'].append(amount)

df_top_trans = pd.DataFrame(Top_tra)
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

df_top_trans['State'] = df_top_trans['State'].replace(dict(zip(top_tra_state_list, custom_state_list)))




Path_6 = "C:/Users/susmi/pulse/data/top/user/country/india/state/"
top_user_state_list = os.listdir(Path_6)

Top_user = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Registered_User': []}

for i in top_user_state_list:
    p_i = Path_6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            F = json.load(Data)
            
            for l in F['data']['pincodes']:
                Name = l['name']
                registeredUser = l['registeredUsers']
                Top_user['State'].append(i)
                Top_user['Year'].append(j)
                Top_user['Quarter'].append(int(k.strip('.json')))
                Top_user['District_Pincode'].append(Name)
                Top_user['Registered_User'].append(registeredUser)
                
df_top_user = pd.DataFrame(Top_user)
custom_state_list = ['Andaman & Nicobar',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']

df_top_user['State'] = df_top_user['State'].replace(dict(zip(top_user_state_list, custom_state_list)))



mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "Phone_pe")
mycursor = mydb.cursor()



def Agg_trans_tab():
    drop_query = '''drop table if exists Agg_trans'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists Agg_trans(State VARCHAR(100),
                                                              Year INT,
                                                              Quarter INT,
                                                              Transaction_type VARCHAR(100),
                                                              Transaction_count BIGINT,
                                                              Transaction_amount FLOAT)''')

   
    for index,row in df_agg_trans.iterrows():
            insert_query='''insert into Agg_trans(State,
                                                   Year,
                                                   Quarter,
                                                   Transaction_type,
                                                   Transaction_count,
                                                   Transaction_amount
                                                   )values(%s,%s,%s,%s,%s,%s)'''
            values=(row['State'],
                    row['Year'],
                    row['Quarter'],
                    row['Transaction_type'],
                    row['Transaction_count'],
                    row['Transaction_amount'])
            mycursor.execute(insert_query,values)
    mydb.commit()


def Agg_user_tab():
    drop_query = '''drop table if exists Agg_user'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists Agg_user(State VARCHAR(100),
                                                              Year INT,
                                                              Quarter INT,
                                                              Brands VARCHAR(100),
                                                              User_Count BIGINT,
                                                              User_Percentage FLOAT)''')

    
    for index,row in df_agg_user.iterrows():
            insert_query='''insert into Agg_user(State,
                                                   Year,
                                                   Quarter,
                                                   Brands,
                                                   User_Count,
                                                   User_Percentage
                                                   )values(%s,%s,%s,%s,%s,%s)'''
            values=(row['State'],
                    row['Year'],
                    row['Quarter'],
                    row['Brands'],
                    row['User_Count'],
                    row['User_Percentage'])
            mycursor.execute(insert_query,values)
    mydb.commit()




def Map_trans_tab():
    drop_query = '''drop table if exists Map_trans'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists Map_trans(State VARCHAR(100),
                                                              Year INT,
                                                              Quarter INT,
                                                              District VARCHAR(100),
                                                              Transaction_count BIGINT,
                                                              Transaction_amount FLOAT)''')

    
    for index,row in df_map_trans.iterrows():
            insert_query='''insert into Map_trans(State,
                                                   Year,
                                                   Quarter,
                                                   District,
                                                   Transaction_count,
                                                   Transaction_amount
                                                   )values(%s,%s,%s,%s,%s,%s)'''
            values=(row['State'],
                    row['Year'],
                    row['Quarter'],
                    row['District'],
                    row['Transaction_count'],
                    row['Transaction_amount'])
            mycursor.execute(insert_query,values)
    mydb.commit()



def Map_user_tab():
    drop_query = '''drop table if exists Map_user'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists  Map_user(State VARCHAR(100),
                                                              Year INT,
                                                              Quarter INT,
                                                              District VARCHAR(100),
                                                              Registered_User INT,
                                                              App_opens BIGINT)''')


    for index,row in df_map_user.iterrows():
            insert_query='''insert into  Map_user(State,
                                                   Year,
                                                   Quarter,
                                                   District,
                                                   Registered_User,
                                                   App_opens)values(%s,%s,%s,%s,%s,%s)'''
            values=(row['State'],
                    row['Year'],
                    row['Quarter'],
                    row['District'],
                    row['Registered_User'],
                    row['App_opens'])
            mycursor.execute(insert_query,values)
    mydb.commit()



def Top_trans_tab():
    drop_query = '''drop table if exists Top_trans'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists Top_trans(State VARCHAR(100),
                                                              Year INT,
                                                              Quarter INT,
                                                              District_Pincode VARCHAR(100),
                                                              Transaction_count BIGINT,
                                                              Transaction_amount FLOAT)''')

    
    for index,row in df_top_trans.iterrows():
            insert_query='''insert into Top_trans(State,
                                                   Year,
                                                   Quarter,
                                                   District_Pincode,
                                                   Transaction_count,
                                                   Transaction_amount
                                                   )values(%s,%s,%s,%s,%s,%s)'''
            values=(row['State'],
                    row['Year'],
                    row['Quarter'],
                    row['District_Pincode'],
                    row['Transaction_count'],
                    row['Transaction_amount'])
            mycursor.execute(insert_query,values)
    mydb.commit()




def Top_user_tab():
    drop_query = '''drop table if exists Top_user'''
    mycursor.execute(drop_query)
    mycursor.execute('''CREATE TABLE if not exists  Top_user(State VARCHAR(100),
                                                              Year INT,
                                                              Quarter INT,
                                                              District_Pincode VARCHAR(100),
                                                              Registered_User INT)''')

    
    for index,row in df_top_user.iterrows():
            insert_query='''insert into  Top_user(State,
                                                   Year,
                                                   Quarter,
                                                   District_Pincode,
                                                   Registered_User)values(%s,%s,%s,%s,%s)'''
            values=(row['State'],
                    row['Year'],
                    row['Quarter'],
                    row['District_Pincode'],
                    row['Registered_User'])
            mycursor.execute(insert_query,values)
    mydb.commit()


def state_list():
    mycursor.execute(f"""select distinct state 
                        from agg_trans
                        order by state asc;""")
    data = mycursor.fetchall()
    original_state = [i[0] for i in data]
    return original_state


def year_list():
    mycursor.execute("SELECT distinct year FROM phone_pe.agg_trans order by year asc;")
    data = mycursor.fetchall()
    data = [i[0] for i in data]
    return data


def quarter_list():
    mycursor.execute("SELECT distinct quarter FROM phone_pe.agg_trans order by quarter asc;")
    data = mycursor.fetchall()
    data = [i[0] for i in data]
    return data


def get_transaction_type():
    mycursor.execute("SELECT distinct transaction_type FROM phone_pe.agg_trans;")
    data = mycursor.fetchall()
    data = [i[0] for i in data]
    return data

def get_agg_users():
    mycursor.execute("SELECT * FROM phone_pe.agg_user;")
    data = mycursor.fetchall()
    d = pd.DataFrame(data, columns=mycursor.column_names)
    return d

def agg_trans_avg(agg_trans):
    data = []
    for i in range(0, len(agg_trans)):
        avg = agg_trans.iloc[i]["Transaction_amount"] / agg_trans.iloc[i]["Transaction_count"]
        data.append(avg)
    return data

def new_frame(v):
    i = [i for i in range(1, len(v)+1)]
    data = pd.DataFrame(v.values, columns=v.columns, index=i)
    return data

def get_map_transaction():
    mycursor.execute("SELECT * FROM phone_pe.map_trans;")
    data = mycursor.fetchall()
    d = pd.DataFrame(data, columns=mycursor.column_names)
    return d

def get_map_users():
    mycursor.execute("SELECT * FROM phone_pe.map_user;")
    data = mycursor.fetchall()
    d = pd.DataFrame(data, columns=mycursor.column_names)
    return d



def users_trans_avg(agg_trans):
    data = []
    for i in range(0, len(agg_trans)):
        avg = agg_trans.iloc[i]["App_opens"] / agg_trans.iloc[i]["Registered_User"]
        data.append(avg)
    return data

#streamlit

# Setting up page configuration
icon = Image.open("ICN.png")
st.set_page_config(page_title= "Phonepe Pulse Data Visualization",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded")

st.title(":violet[Phonepe Pulse Data Visualization]")

with st.sidebar:
    st.header(":wave: :violet[**Hello! Welcome to the dashboard**]")
    india=Image.open("india.png")
    selected = option_menu(None,
                            options=["Home","INDIA","Transactions-Insights","Users-Insights"],
                            icons=["house","india", "cash-coin", "bi-people"],
                            default_index=0,
                            orientation="horizontal",
                            styles={"container": {"width": "90%"},
                                    "options": {"margin": "10px"},
                                    "icon": {"color": "black", "font-size": "24px"},
                                    "nav-link": {"font-size": "20px", "text-align": "center", "margin": "15px", "--hover-color": "#6F36AD"},
                                    "nav-link-selected": {"background-color": "#6F36AD"}})
    
    
if selected == "Home":
    im1 = Image.open("cover1.jpeg")
    st.image(im1, width=1000)
    st.header(":violet[📱PHONEPE]  _INDIA'S Most Trusted Payment Gateway_")
    st.subheader("DOMAIN: :green[Fintech]")
    st.subheader(":green[TECHNOLOGIES-USED]")
    st.markdown("Github Cloning, Python, Pandas, MYSQL, Streamlit, and Plotly")
    st.subheader("OVERVIEW")
    st.markdown("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")

    st.write("****FEATURES****")
    st.write("****✳Credit & Debit card linking****")
    st.write("****✳Bank Balance check****")
    st.write("****✳Money Storage****")
    st.write("****✳PIN Authorization****")
    st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    
    
    
    
if selected == "INDIA":
    MAP= st.selectbox("select your MAP",("Click to select","Total_transactions","Registered Users","App_opens"))
    def get_aggregated_user():
            mycursor.execute( "SELECT * FROM phone_pe.agg_trans;")
            data = mycursor.fetchall()
            df = pd.DataFrame(data, columns=mycursor.column_names)
            return df
        
    
    
    if MAP=='Total_transactions':
        total_trans=get_aggregated_user()
        total_trans=total_trans.groupby(["State"])[["Transaction_count"]].sum().reset_index()
        fig = px.choropleth(total_trans,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_count',
                            color_continuous_scale="Viridis",
                            title="Transactions state wise",
                                    height=1000, width=1200)
        fig.update_geos(fitbounds='locations', visible=False)
        st.write(fig)        
    
    if MAP =="Registered Users":
        tot_user = get_map_users()
        tot_user = tot_user.groupby(["State"])[["Registered_User", "App_opens"]].sum().reset_index()
        data =state_list()
        fig = px.choropleth(tot_user,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Registered_User',
                            color_continuous_scale="Reds",
                            title="Registered Users state wise",
                                    height=1000, width=1200)
        fig.update_geos(fitbounds='locations', visible=False)
        st.write(fig)
    if MAP=='App_opens':
        tot_user = get_map_users()
        tot_user = tot_user.groupby(["State"])[["Registered_User", "App_opens"]].sum().reset_index()
        fig = px.choropleth(tot_user,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='App_opens',
                            color_continuous_scale="Greens",
                            title="App opens state wise",
                                    height=1000, width=1200)
        fig.update_geos(fitbounds='locations', visible=False)
        st.write(fig)        
        

if selected == "Transactions-Insights":
    with st.container():       
        st.markdown(":black[TRANSACTIONS INSIGHTS]")
        col1, col2, col3 = st.columns(3)
        # select box
        with col1:
            state = st.selectbox(label="Select the state",
                                 options=state_list(), index=0)
        with col2:
            year = st.selectbox(label="Select the year",
                                options=year_list(), index=0)
        with col3:
            quarter = st.selectbox(label="Select the Quarter", 
                                   options=quarter_list(), index=0)
   
        def get_aggregated_user():
            mycursor.execute( "SELECT * FROM phone_pe.agg_trans;")
            data = mycursor.fetchall()
            df = pd.DataFrame(data, columns=mycursor.column_names)
            return df
        
        
        df_agg_tran = get_aggregated_user()
        avg_value = agg_trans_avg(df_agg_tran)
        avg_value = pd.DataFrame(avg_value, columns=["avg_value"])
        df_av = pd.concat([df_agg_tran, avg_value], axis=1)
        v = df_av[(df_av["Year"] == year) & (df_av["Quarter"] == quarter)& (df_av["State"] == state)]
        total_transactions = v["Transaction_count"].sum()
        total_transaction_amount =v["Transaction_amount"].sum()
        total_avg=v["avg_value"].sum()
        
        col1,col2,col3=st.columns(3)
        with col1:
            st.markdown(":black[All PhonePe transactions (UPI + Cards + Wallets)]")
            st.write(total_transactions)
        with col2:
            st.markdown(":black[Total payment value]")
            st.write( total_transaction_amount)
        with col3:
            st.markdown(":black[Avg. transaction value]")
            st.write(total_avg)
                     
        plt.figure(figsize=(12, 5))
        fig = px.pie(v, values='Transaction_amount', names='Transaction_type', title='Pie Chart for Transaction Types',
            hover_data=['Transaction_count', 'avg_value'])

        fig.update_traces(textinfo='percent+label', pull=[0.1] * len(v['Transaction_type']))
        st.write(fig)
        st.markdown("")
        new_v = new_frame(v)
        st.table(new_v)

        col1, col2 = st.columns(2)
    
        with col1:
            year_df = st.selectbox(label="Select year", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)

        with col2:
            transaction_type = st.selectbox(label="Select the transaction type", options=get_transaction_type(), index=0)
        
        df_agg_total = get_aggregated_user()
        df_agg_total = df_agg_total.groupby(["State", "Year", "Transaction_type"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()
        q = df_agg_total[(df_agg_total["Year"] == year_df) & (df_agg_total["Transaction_type"] == transaction_type)]

        fig = px.bar(q, x='State', y='Transaction_count',hover_data=['State', 'Transaction_count'], height=500, title="Transaction count state wise")
        st.write(fig)
                
        df_agg_total = get_aggregated_user()
        df_agg_total = df_agg_total.groupby(["State", "Year", "Transaction_type"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()
        q = df_agg_total[(df_agg_total["Year"] == year_df) & (df_agg_total["Transaction_type"] == transaction_type)]

        fig = px.bar(q, x='State', y='Transaction_amount',hover_data=['State', 'Transaction_amount'], height=500, title="Transaction Amount state wise")
        st.write(fig)

        st.markdown("")
        new_v = new_frame(q)
        st.table(new_v)   
        
        st.markdown("#### Top 10 distircts")
        year_df_d = st.selectbox(label="Select year for the district wise data", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)
         
        st.markdown("#### Top 10 distircts for Transaction Count wise")
        df = get_map_transaction()
        df = df.groupby(["Year", "District"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()
        k = df[df["Year"] == year_df_d]
        c = k.sort_values(by=["Transaction_count"],ascending=False).head(10)
        c = c[["Year", "District", "Transaction_count"]]
        c_df = new_frame(c)
        st.table(c_df)
        
     
        st.markdown("#### Top 10 States")
        year_df_State = st.selectbox(label="Select year for the state wise data", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)

        st.markdown("#### Top 10 States for Transaction Count wise")
        df = get_aggregated_user()
        df = df.groupby(["Year", "State"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()
        k1 = df[df["Year"] == year_df_State]
        c1 = k1.sort_values(by=["Transaction_count"],ascending=False).head(10)
        c1 = c1[["Year","State","Transaction_count"]]
        c1_df = new_frame(c1)
        st.table(c1_df)
         
        
       

if selected == "Users-Insights":
    
    st.markdown("#### :black[USERS INSIGHTS]")
    col1, col2, col3 = st.columns(3)
    with col1:
        user_state = st.selectbox(label="Select the state users", options=state_list(), index=0)
        
    with col2:
        user_year = st.selectbox(label="Select the year users",options=year_list(), index=0)
         
    with col3:
        user_quarter = st.selectbox(label="Select the Quarter users", options=quarter_list(), index=0)
           
    
    user_df = get_agg_users()
    user = user_df[(user_df["State"] == user_state) & (user_df["Year"] == user_year) & (user_df["Quarter"] == user_quarter)]
    User_Count=user["User_Count"].sum()
    User_Percentage=user["User_Percentage"].sum()
    
    col1,col2=st.columns(2)
    with col1:
        st.markdown("User Count")
        st.write(User_Count)
    with col2:
        st.markdown("User Percentage")
        st.write(User_Percentage)
    
    pie_fig = px.pie(user, names="Brands", values="User_Count",title="Pie Chart for Users Brands")
    st.write(pie_fig)
    6g    
    c_df = new_frame(user)
    st.table(c_df)
   
    tot_state = st.selectbox(label="Select a state",options=state_list(), index=10)
    tot_user = get_map_users()
    tot_user = tot_user.groupby(["State", "Year",])[ ["Registered_User", "App_opens"]].sum().reset_index()
    to = tot_user[tot_user["State"] == tot_state][1:]
    
    col1, col2 = st.columns(2)

    with col1:    
        fig = px.bar(to, x='Year', y='Registered_User', width=500, color="Year",title="Year wise Registered Users")
        st.write(fig)

    with col2:

        fig = px.bar(to, x='Year', y='App_opens', width=500, color="Year", title="Year wise App opens")
        st.write(fig)

    st.markdown("")
    st.markdown("")
    to_df = new_frame(to)
    st.table(to_df)

    st.markdown("#### Top 10 distircts")
    year_df_d = st.selectbox(label="Select year for the district wise data", options=(2018, 2019, 2020, 2021, 2022, 2023), index=0)
        
    st.markdown("#### Top 10 distircts for Registered_User")
    df = get_map_users()
    df = df.groupby(["Year", "District"])[["Registered_User", "App_opens"]].sum().reset_index()
    k = df[df["Year"] == year_df_d]
    c = k.sort_values(by=["Registered_User"],ascending=False).head(10)
    c = c[["Year", "District", "Registered_User"]]
    c_df = new_frame(c)
    st.table(c_df)
    
    
    
    
    
   
    
    
    
    
    
    
    