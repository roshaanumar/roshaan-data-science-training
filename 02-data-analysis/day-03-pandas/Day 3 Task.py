import pandas as p
data = p.read_csv("messy_data2.csv")
#Number of original rows
print("Original rows:", len(data))
#Duplicates removed
data.drop_duplicates(subset=["name", "age", "email", "signup_date", "city", "salary"],inplace=True)
#missing values
data.loc[3, "name"] = "Imran Sheikh"
data.loc[5, "signup_date"] = "2022-12-04"
data.loc[7, "email"] = "saad.khan@email.com"
data["age"] = p.to_numeric(data["age"], errors="coerce")
agee = data["age"].mean()
salaryy = data["salary"].mean()

x=int(agee)
y=int(salaryy)
data.fillna({"name" : "Unknown" ,"age" : int(x) , "salary" : int(y) }, inplace= True)
#Invalid rows
data.dropna(inplace= True)
data.reset_index(drop=True, inplace=True)
a = 0
for a in range(len(data)):
    data.loc[a, "name"] = data.loc[a, "name"].strip().title()
    data.loc[a, "city"] = data.loc[a, "city"].strip().title()
    data.loc[a, "email"] = data.loc[a, "email"].strip().lower()
    age = data.loc[a,"age"]
    if age < 25 or age > 50:
       z = data["age"].mode()[0]
       data.loc[a, "age"] = z
    a+=1    
#print("Sorted Data:")
#print(data.sort_values(by = ["age", "salary"], ascending= True))
#Final rows
print(data)
print("Final rows:", len(data))


#My practice:-
#import matplotlib.pyplot as plt
#p.options.display.max_rows = 100
#f = open("messy_data2.csv", "r")
#df_var = p.DataFrame(data)
#s_var = p.Series(data)
#print(data.tail(6))
#print(data.info())
#print(s_var)
#print(df_var.loc[0])
#print(p.options.display.max_rows)
#x = data["age"].mean()
#data.fillna({"age": x}, inplace=True)
#new_data = data.dropna()
#print(new_data.to_string())
#data["signup_date"] = p.to_datetime(data["signup_date"], format="%Y-%m-%d", errors="coerce")
#data["age"] = p.to_numeric(data["age"], errors="coerce")
#data.loc[17, "age"] = 35 
#data.dropna(inplace = True)
#print(data[["id", "age", "salary"]].corr())
#data.sort_values(["age", "salary"])
#print(data[data["age"] > 30])
#print(data.sort_values(by = ["age", "salary"], ascending = [True, True]))
#print(data.describe())
#print(data.groupby("city")["age"].count())
#print(data["email"].value_counts())
#print(data["age"].apply(lambda x: "Adult" if x >= 18 else "Minor"))
#print(data.isnull())
#data.plot()
#plt.show()