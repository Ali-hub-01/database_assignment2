import streamlit as st
import sqlalchemy as sa

conn = sa.create_engine("postgresql+psycopg2://postgres:AliKanafin01@db.oxochhpxmbovxudvultn.supabase.co:5432/postgres")
conn.connect()


def att(choice2):
    if choice2 == "DiseaseType":
        ord = ["Did", "Description"]
    elif choice2 == "Disease":
        ord = ["Disease_code", "Pathogen", "Did"]
    elif choice2 == "Country":
        ord = ["Cname", "Population"]
    elif choice2 == "Discover":
        ord = ["Cname", "Disease_code", "First_enc_date"]
    elif choice2 == "Users":
        ord = ["Email", "Uname", "Surname", "Salary", "Phone", "Cname"]
    elif choice2 == "Doctor":
        ord = ["Email", "Ddegree"]
    elif choice2 == "Specialize":
        ord = ["Did", "Email"]
    elif choice2 == "PublicServant":
        ord = ["Email", "Department"]
    elif choice2 == "Record":
        ord = ["Email", "Cname", "Disease_code", "Total_deaths", "Total_patients"]
    return ord


def katt(choice2):
    if choice2 == "DiseaseType":
        key = ["Did"]
    elif choice2 == "Disease":
        key = ["Disease_code"]
    elif choice2 == "Country":
        key = ["Cname"]
    elif choice2 == "Discover":
        key = ["Cname", "Disease_code"]
    elif choice2 == "Users":
        key = ["Email"]
    elif choice2 == "Doctor":
        key = ["Email"]
    elif choice2 == "Specialize":
        key = ["Did", "Email"]
    elif choice2 == "PublicServant":
        key = ["Email", "Department"]
    elif choice2 == "Record":
        key = ["Email", "Cname", "Disease_code"]
    return key


def view_unique_column(att, choice2):
    data = conn.execute(f"select distinct {att} from {choice2}")
    return data

def view_unique_column_second(att,att_s,att2,choice2):
    data = conn.execute(f"select distinct {att} from {choice2} where {att_s}='{att2}'")
    return data


def view_unique_column_third(att,att_s1,att2,att_s2,att3,choice2):
    data = conn.execute(f"select distinct {att} from {choice2} where {att_s1}='{att2}' and {att_s2}='{att3}'")
    return data


def get_data_int(column, att, choice2):
    data = conn.execute(f"select * from {choice2} where {att} = '{column}'")
    return data


def get_data_int_2(column, column2, att, att2, choice2):
    data = conn.execute(f"select * from {choice2} where {att} = '{column}' and {att2}='{column2}'")
    return data


def get_data_int_3(column, column2, column3, att, att2, att3, choice2):
    data = conn.execute(
        f"select * from {choice2} where {att} = '{column}' and {att2}='{column2}' and {att3}='{column3}'")
    return data


def read(choice2, wh, ord, sc):
    q = sa.text(f"Select * From {choice2}{wh} Order By {ord} {sc}")
    st.table(conn.execute(q))


def find(choice2,att,key_s, key):
    q=sa.text(f"select {att} from {choice2} where {key_s}='{key}'")
    return conn.execute(q)


def find_2(choice2,att,key_s, key,key_s_2,key2):
    q=sa.text(f"select {att} from {choice2} where {key_s}='{key}' and {key_s_2}='{key2}'")
    return conn.execute(q)


def find_3(choice2,att,key_s, key,key_s_2,key2,key_s_3,key3):
    q=sa.text(f"select {att} from {choice2} where {key_s}='{key}' and {key_s_2}='{key2}' and {key_s_3}='{key3}'")
    return conn.execute(q)


def disTypeCreate():
    col1, col2 = st.columns(2)
    with col1:
        id = st.number_input("ID", step=1)
    des = st.text_area("Description", max_chars=140)
    if st.button("Create"):
        q = sa.text(f"Insert Into DiseaseType(did,description) Values({id},'{des}')")
        conn.execute(q)
        st.success(f"Successfully Added Data:{id},'{des}'")


def disCreate():
    list_of_data = [i[0] for i in view_unique_column("did", "diseasetype")]
    disCode = st.text_input("Disease Code", max_chars=50)
    col1, col2 = st.columns(2)
    with col1:
        patho = st.text_input("Pathogen", max_chars=20)
    with col2:
        id = st.selectbox("ID", list_of_data)
    des = st.text_area("Description", max_chars=140)
    if st.button("Create"):
        q = sa.text(
            f"Insert Into Disease(disease_code,pathogen,description,did) Values('{disCode}','{patho}','{des}',{id})")
        conn.execute(q)
        st.success(f"Successfully Added Data:'{disCode}','{patho}','{des}',{id}")


def counCreate():
    col1, col2 = st.columns(2)
    with col1:
        cname = st.text_input("Country Name", max_chars=50)
    with col2:
        popul = st.number_input("Population", step=1)
    if st.button("Create"):
        q = sa.text(f"Insert Into Country(cname,population) Values('{cname}',{popul})")
        conn.execute(q)
        st.success(f"Successfully Added Data:'{cname}',{popul}")


def discCreate():
    list_of_data1 = [i[0] for i in view_unique_column("disease_code", "disease")]
    list_of_data2 = [i[0] for i in view_unique_column("cname", "country")]
    col1, col2 = st.columns(2)
    with col1:
        cname = st.selectbox("Country", list_of_data2)
    with col2:
        dis_c = st.selectbox("Disease Code", list_of_data1)
    fed = st.date_input("First Entrance Date")
    if st.button("Create"):
        q = sa.text(f"Insert Into Discover(cname,disease_code,first_enc_date) Values('{cname}','{dis_c}','{fed}')")
        conn.execute(q)
        st.success(f"Successfully Added Data:'{cname}','{dis_c}','{fed}'")


def userCreate():
    list_of_data = [i[0] for i in view_unique_column("cname", "country")]
    col1, col2 = st.columns(2)
    with col1:
        uname = st.text_input("User Name", max_chars=30)
        surname = st.text_input("User Surname", max_chars=40)
        cname = st.selectbox("Country", list_of_data)
    with col2:
        phone = st.text_input("Phone Number", max_chars=20)
        email = st.text_input("Email", max_chars=60)
        salary = st.number_input("Salary", step=1)
    if st.button("Create"):
        q = sa.text(
            f"Insert Into Users(email,uname,surname,salary,phone,cname) Values('{email}','{uname}','{surname}',{salary},'{phone}','{cname}')")
        conn.execute(q)
        st.success(f"Successfully Added Data:'{email}','{uname}','{surname}',{salary},'{phone}','{cname}'")


def pServantCreate():
    list_of_data = [i[0] for i in view_unique_column("email", "users")]
    email = st.selectbox("Email", list_of_data)
    depart = st.text_input("Department", max_chars=50)
    if st.button("Create"):
        q = sa.text(f"Insert Into PublicServant(email,department) Values('{email}','{depart}')")
        conn.execute(q)
        st.success(f"Successfully Added Data:'{email}','{depart}'")


def doctorCreate():
    list_of_data = [i[0] for i in view_unique_column("email", "users")]
    email = st.selectbox("Email", list_of_data)
    degree = st.text_input("Degree", max_chars=20)
    if st.button("Create"):
        q = sa.text(f"Insert Into Doctor(email,ddegree) Values('{email}','{degree}')")
        conn.execute(q)
        st.success(f"Successfully Added Data:'{email}','{degree}'")


def specCreate():
    list_of_data1 = [i[0] for i in view_unique_column("email", "users")]
    email = st.selectbox("Email", list_of_data1)
    list_of_data2 = [i[0] for i in view_unique_column("did", "diseasetype")]
    id = st.selectbox("ID", list_of_data2)
    if st.button("Create"):
        q = sa.text(f"Insert Into Specialize(did,email) Values({id},'{email}')")
        conn.execute(q)
        st.success(f"Successfully Added Data:{id},'{email}'")


def recCreate():
    list_of_data1 = [i[0] for i in view_unique_column("email", "users")]
    email = st.selectbox("Email", list_of_data1)
    list_of_data2 = [i[0] for i in view_unique_column("cname", "country")]
    cname = st.selectbox("Country", list_of_data2)
    list_of_data2 = [i[0] for i in view_unique_column("disease_code", "disease")]
    discode = st.selectbox("Country", list_of_data2)
    tot_death = st.number_input("Total Deaths", step=1)
    tot_patient = st.number_input("Total Patients", step=1)
    if st.button("Create"):
        q = sa.text(f"Insert Into Record(email,cname,disease_code,total_deaths,total_patients) "
                    f"Values('{email}','{cname}','{discode}',{tot_death},{tot_patient})")
        conn.execute(q)
        st.success(f"Successfully Added Data:'{email}','{cname}','{discode}',{tot_death},{tot_patient}")


def disTypeUpdate(choice2):
    list_of_data = [i[0] for i in view_unique_column("did", choice2)]
    select_data = st.selectbox("Data to Update", list_of_data)
    select_result = get_data_int(select_data, "did", choice2)
    st.table(select_result)
    if select_result:
        col1, col2 = st.columns(2)
        with col1:
            id = st.number_input("ID", step=1,value=[i[0] for i in find(choice2,"did","did",select_data)][0])
        des = st.text_area("Description", max_chars=140,value=[i[0] for i in find(choice2,"description","did",select_data)][0])
    if st.button("Update"):
        q = sa.text(f"update {choice2} set did={id}, description ='{des}' where did ={select_data}")
        conn.execute(q)


def disUpdate(choice2):
    list_of_data = [i[0] for i in view_unique_column("disease_code", choice2)]
    select_data = st.selectbox("Data to Update", list_of_data)
    select_result = get_data_int(select_data, "disease_code", choice2)
    st.table(select_result)
    if select_result:
        disCode = st.text_input("Disease Code", max_chars=50,value=[i[0] for i in find(choice2,"disease_code","disease_code",select_data)][0])
        col1, col2 = st.columns(2)
        with col1:
            patho = st.text_input("Pathogen", max_chars=20,value=[i[0] for i in find(choice2,"pathogen","disease_code",select_data)][0])
        with col2:
            id = st.number_input("ID", step=1,value=[i[0] for i in find(choice2,"did","disease_code",select_data)][0])
        des = st.text_area("Description", max_chars=140,value=[i[0] for i in find(choice2,"description","disease_code",select_data)][0])
    if st.button("Update"):
        q = sa.text(f"update {choice2} set disease_code='{disCode}',pathogen='{patho}', description ='{des}',did={id} "
                    f"where disease_code ='{select_data}'")
        conn.execute(q)


def counUpdate(choice2):
    list_of_data = [i[0] for i in view_unique_column("cname", choice2)]
    select_data = st.selectbox("Data to Update", list_of_data)
    select_result = get_data_int(select_data, "cname", choice2)
    st.table(select_result)
    if select_result:
        col1, col2 = st.columns(2)
        with col1:
            cname = st.text_input("Country Name", max_chars=50,value=[i[0] for i in find(choice2,"cname","cname",select_data)][0])
        with col2:
            popul = st.number_input("Population", step=1,value=[i[0] for i in find(choice2,"population","cname",select_data)][0])
    if st.button("Update"):
        q = sa.text(f"update {choice2} set cname='{cname}', population ={popul} where cname ='{select_data}'")
        conn.execute(q)


def discUpdate(choice2):
    list_of_data1 = [i[0] for i in view_unique_column("cname", choice2)]
    select_data1 = st.selectbox("Data to Update", list_of_data1)
    list_of_data2 = [i[0] for i in view_unique_column_second("disease_code","cname",select_data1, choice2)]
    select_data2 = st.selectbox("Data to Update", list_of_data2)
    select_result = get_data_int_2(select_data1, select_data2, "cname", "disease_code", choice2)
    st.table(select_result)
    if select_result:
        col1, col2 = st.columns(2)
        with col1:
            cname = st.text_input("Country Name", max_chars=50,value=[i[0] for i in find_2(choice2,"cname","cname",select_data1,"disease_code",select_data2)][0])
        with col2:
            dis_c = st.text_input("Disease Code", max_chars=50,value=[i[0] for i in find_2(choice2,"disease_code","cname",select_data1,"disease_code",select_data2)][0])
        fed = st.date_input("First Entrance Date",value=[i[0] for i in find_2(choice2,"first_enc_date","cname",select_data1,"disease_code",select_data2)][0])
    if st.button("Update"):
        q = sa.text(f"update {choice2} set cname='{cname}', disease_code ='{dis_c}',first_enc_date='{fed}' "
                    f"where cname ={select_data1} and disease_code={select_data2}")
        conn.execute(q)


def userUpdate(choice2):
    list_of_data = [i[0] for i in view_unique_column("email", choice2)]
    select_data = st.selectbox("Data to Update", list_of_data)
    select_result = get_data_int(select_data, "email", choice2)
    st.table(select_result)
    if select_result:
        col1, col2 = st.columns(2)
        with col1:
            uname = st.text_input("User Name", max_chars=30,value=[i[0] for i in find(choice2,"uname","email",select_data)][0])
            surname = st.text_input("User Surname", max_chars=40,value=[i[0] for i in find(choice2,"surname","emeil",select_data)][0])
            cname = st.text_input("Country Name", max_chars=50,value=[i[0] for i in find(choice2,"cname","email",select_data)][0])
        with col2:
            phone = st.text_input("Phone Number", max_chars=20,value=[i[0] for i in find(choice2,"phone","email",select_data)][0])
            email = st.text_input("Email", max_chars=60,value=[i[0] for i in find(choice2,"email","email",select_data)][0])
            salary = st.number_input("Salary", step=1,value=[i[0] for i in find(choice2,"salary","email",select_data)][0])
    if st.button("Update"):
        q = sa.text(
            f"update {choice2} set uname='{uname}', surname ='{surname}',cname='{cname}',phone='{phone}',email='{email}',"
            f"salary={salary} where email ={select_data}")
        conn.execute(q)


def pServantUpdate(choice2):
    list_of_data = [i[0] for i in view_unique_column("email", choice2)]
    select_data = st.selectbox("Data to Update", list_of_data)
    select_result = get_data_int(select_data, "email", choice2)
    st.table(select_result)
    if select_result:
        email = st.text_input("Email", max_chars=60,value=[i[0] for i in find(choice2,"email","email",select_data)][0])
        depart = st.text_input("Department", max_chars=50,value=[i[0] for i in find(choice2,"department","email",select_data)][0])
    if st.button("Update"):
        q = sa.text(
            f"update {choice2} set email='{email}',department='{depart}' where email ={select_data}")
        conn.execute(q)


def doctorUpdate(choice2):
    list_of_data = [i[0] for i in view_unique_column("email", choice2)]
    select_data = st.selectbox("Data to Update", list_of_data)
    select_result = get_data_int(select_data, "email", choice2)
    st.table(select_result)
    if select_result:
        email = st.text_input("Email", max_chars=60,value=[i[0] for i in find(choice2,"email","email",select_data)][0])
        degree = st.text_input("Degree", max_chars=20,value=[i[0] for i in find(choice2,"ddegree","email",select_data)][0])
    if st.button("Update"):
        q = sa.text(
            f"update {choice2} set email='{email}',ddegree='{degree}' where email ={select_data}")
        conn.execute(q)


def specUpdate(choice2):
    list_of_data1 = [i[0] for i in view_unique_column("did", choice2)]
    select_data1 = st.selectbox("Data to Update", list_of_data1)
    list_of_data2 = [i[0] for i in view_unique_column_second("email","did",select_data1, choice2)]
    select_data2 = st.selectbox("Data to Update", list_of_data2)
    select_result = get_data_int_2(select_data1, select_data2, "did", "email", choice2)
    st.table(select_result)
    if select_result:
        email = st.text_input("Email", max_chars=60,value=[i[0] for i in find_2(choice2,"email","did",select_data1,"email",select_data2)][0])
        id = st.number_input("ID", step=1, value=[i[0] for i in find_2(choice2,"ID","did",select_data1,"email",select_data2)][0])
    if st.button("Update"):
        q = sa.text(
            f"update {choice2} set email='{email}', did ={id} where cname ={select_data1} and disease_code={select_data2}")
        conn.execute(q)


def recUpdate(choice2):
    list_of_data1 = [i[0] for i in view_unique_column("email", choice2)]
    select_data1 = st.selectbox("Data to Update", list_of_data1)
    list_of_data2 = [i[0] for i in view_unique_column_second("cname","email",select_data1, choice2)]
    select_data2 = st.selectbox("Data to Update", list_of_data2)
    list_of_data3 = [i[0] for i in view_unique_column_third("disease_code","email",select_data1,"cname",select_data2, choice2)]
    select_data3 = st.selectbox("Data to Update", list_of_data3)
    select_result = get_data_int_3(select_data1, select_data2, select_data3, "email", "cname", "disease_code", choice2)
    st.table(select_result)
    if select_result:
        email = st.text_input("Email", max_chars=60, value=[i[0] for i in find_3(choice2,"email","email",select_data1,"cname",select_data2,"disease_code",select_data3)][0])
        cname = st.text_input("Country Name", max_chars=50, value=[i[0] for i in find_3(choice2,"cname","email",select_data1,"cname",select_data2,"disease_code",select_data3)][0])
        discode = st.text_input("Disease Code", max_chars=50, value=[i[0] for i in find_3(choice2,"disease_code","email",select_data1,"cname",select_data2,"disease_code",select_data3)][0])
        tot_death = st.number_input("Total Deaths", step=1, value=[i[0] for i in find_3(choice2,"total_deaths","email",select_data1,"cname",select_data2,"disease_code",select_data3)][0])
        tot_patient = st.number_input("Total Patients", step=1, value=[i[0] for i in find_3(choice2,"total_patients","email",select_data1,"cname",select_data2,"disease_code",select_data3)][0])
    if st.button("Update"):
        q = sa.text(
            f"update {choice2} set email='{email}', cname ='{cname}',disease_code='{discode}',"
            f"total_deaths={tot_death},total_patients={tot_patient} where email ='{select_data1}' "
            f"and cname='{select_data2}' and disease_code={select_data3}")
        conn.execute(q)

def delete(choice2,att):
    list_of_data = [i[0] for i in view_unique_column(att, choice2)]
    select_data = st.selectbox("Data to Update", list_of_data)
    select_result = get_data_int(select_data, att, choice2)
    st.table(select_result)
    if st.button("Delete"):
        q = sa.text(f"delete from {choice2} where {att}='{select_data}'")
        conn.execute(q)


def delete_2(choice2,att,att2):
    list_of_data1 = [i[0] for i in view_unique_column(att, choice2)]
    select_data1 = st.selectbox("Data to Update", list_of_data1)
    list_of_data2 = [i[0] for i in view_unique_column_second(att2,att,select_data1, choice2)]
    select_data2 = st.selectbox("Data to Update", list_of_data2)
    select_result = get_data_int_2(select_data1, select_data2, att, att2, choice2)
    st.table(select_result)
    if st.button("Delete"):
        q = sa.text(f"delete from {choice2} where {att}='{select_data1}' and {att2}='{select_data2}'")
        conn.execute(q)


def delete_3(choice2,att,att2,att3):
    list_of_data1 = [i[0] for i in view_unique_column(att, choice2)]
    select_data1 = st.selectbox("Data to Update", list_of_data1)
    list_of_data2 = [i[0] for i in view_unique_column_second(att2,att,select_data1, choice2)]
    select_data2 = st.selectbox("Data to Update", list_of_data2)
    list_of_data3 = [i[0] for i in view_unique_column_second(att3,att,select_data1,att2,select_data2, choice2)]
    select_data3 = st.selectbox("Data to Update", list_of_data3)
    select_result = get_data_int_3(select_data1, select_data2, select_data3, "email", "cname", "disease_code", choice2)
    st.table(select_result)
    if st.button("Delete"):
        q = sa.text(f"delete from {choice2} where {att}='{select_data1}' and {att2}='{select_data2}' and {att3}='{select_data3}'")
        conn.execute(q)

def main():
    st.title("CRUD APP")

    crud = ["Create", "Read", "Update", "Delete"]
    choice1 = st.sidebar.selectbox("CRUD", crud)
    table = ["DiseaseType", "Disease", "Country", "Discover", "Users", "Doctor", "Specialize", "PublicServant",
             "Record"]
    choice2 = st.sidebar.selectbox("Table", table)

    if choice1 == "Read":
        st.subheader("View Items")
        col1, col2 = st.columns(2)
        sc = ["Asc", "Desc"]
        with col1:
            ord = st.selectbox("Order By", att(choice2))
        with col2:
            ord2 = st.selectbox("In", sc)

        search = st.text_input(f"Search by {ord}", placeholder=f"{ord}")
        wh = ""
        if search:
            wh = f" where Lower({ord}) = '{search}'"
        read(choice2, wh, ord, ord2)

    elif choice1 == "Create":
        st.subheader(f"Create New Data to {choice2}")
        if choice2 == "DiseaseType":
            disTypeCreate()
        elif choice2 == "Disease":
            disCreate()
        elif choice2 == "Country":
            counCreate()
        elif choice2 == "Discover":
            discCreate()
        elif choice2 == "Users":
            userCreate()
        elif choice2 == "PublicServant":
            pServantCreate()
        elif choice2 == "Doctor":
            doctorCreate()
        elif choice2 == "Specialize":
            specCreate()
        elif choice2 == "Record":
            recCreate()

    elif choice1 == "Update":
        st.subheader(f"Edit/Update Data from {choice2}")
        if choice2 == "DiseaseType":
            disTypeUpdate(choice2)
        elif choice2 == "Disease":
            disUpdate(choice2)
        elif choice2 == "Country":
            counUpdate(choice2)
        elif choice2 == "Discover":
            discUpdate(choice2)
        elif choice2 == "Users":
            userUpdate(choice2)
        elif choice2 == "PublicServant":
            pServantUpdate(choice2)
        elif choice2 == "Doctor":
            doctorUpdate(choice2)
        elif choice2 == "Specialize":
            specUpdate(choice2)
        elif choice2 == "Record":
            recUpdate(choice2)

    elif choice1 == "Delete":
        st.subheader("Delete Items")
        if choice2 == "DiseaseType":
            delete(choice2,"did")
        elif choice2 == "Disease":
            delete(choice2,"disease_code")
        elif choice2 == "Country":
            delete(choice2, "cname")
        elif choice2 == "Discover":
            delete_2(choice2,"cname","disease_code")
        elif choice2 == "Users":
            delete(choice2,"email")
        elif choice2 == "PublicServant":
            delete(choice2,"email")
        elif choice2 == "Doctor":
            delete(choice2,"email")
        elif choice2 == "Specialize":
            delete_2(choice2,"did","email")
        elif choice2 == "Record":
            recUpdate(choice2)


if __name__ == '__main__':
    main()
