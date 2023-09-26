#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# # Add 12 Records. Take input from user.

# In[1]:


def add_records():
    records = []
    for i in range(12):
        prod_no = input("Enter Product No: ")
        prod_name = input("Enter Product Name: ")
        jan = int(input("Enter January Sell: "))
        feb = int(input("Enter February Sell: "))
        mar = int(input("Enter March Sell: "))
        apr = int(input("Enter April Sell: "))
        may = int(input("Enter May Sell: "))
        jun = int(input("Enter June Sell: "))
        records.append([prod_no, prod_name, jan, feb, mar, apr, may, jun])
    return records


# In[ ]:


data= add_records()


# # 2. Create dataframe.

# In[ ]:


columns = ["Prod_No", "Prod_Name", "January", "February", "March", "April", "May", "June"]
df = pd.DataFrame(data, columns=columns)


# # 3. Change Column Name

# In[ ]:


df = df.rename(columns={"Prod_No": "Product No", "Prod_Name": "Product Name"})


# # 4.Add column "Total Sell" to count total of all month and "Average Sell"

# In[ ]:


df["Total Sell"] = df.iloc[:, 2:].sum(axis=1)
df["Average Sell"] = df.iloc[:, 2:8].mean(axis=1)


# # 5. Add 2 row at the end.

# In[ ]:


df=pd.concat([df,pd.DataFrame([["13","pear",500,200,600,900,700,100],
                              ["14","cherry",900,800,700,600,500,400]],columns=columns)],ignore_index=True)


# # 6. Add 2 row after 3rd row.

# In[ ]:


insert_row1 = {"Product No": "P8", "Product Name": "Product 8", "January": 8000, "February": 9000, "March": 10000, "April": 11000, "May": 12000, "June": 13000}
insert_row2 = {"Product No": "P9", "Product Name": "Product 9", "January": 9000, "February": 10000, "March": 11000, "April": 12000, "May": 13000, "June": 14000}
df = pd.concat([df.iloc[:3], pd.DataFrame([insert_row1, insert_row2]), df.iloc[3:]]).reset_index(drop=True)


# # 7. Print first 5 row.

# In[ ]:


print("First 5 rows:")
print(df.head(5))


# # 8. Print Last 5 row.

# In[ ]:


print("\nLast 5 rows:")
print(df.tail(5))


# # 9. Print row 6 to 10.

# In[ ]:


print("\nRows 6 to 10:")
print(df.iloc[5:10])


# # 10. Print only product name.

# In[ ]:


print("\nProduct Names:")
print(df["Product Name"])


# # 11. Print sell of January month with product id and product name.

# In[ ]:


print("\nJanuary Sell with Product ID and Product Name:")
print(df[["Product No", "Product Name", "January"]])


# # 12. Print only those product id , product name where january sell is > 5000 and February sell is >8000

# In[ ]:


print("\nRecords where January sell > 5000 and February sell > 8000:")
print(df[(df["January"] > 5000) & (df["February"] > 8000)])


# # 13. Print record in sorting order of Product name.

# In[ ]:




