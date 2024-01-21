#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd 
import seaborn as sns


# In[29]:


df =pd.read_csv("C:/Users/nitis/Downloads/udemy_courses.csv")


# In[30]:


df.head(10)


# In[31]:


df.dtypes


# In[32]:


df.info()


# In[33]:


df.isnull().sum()


# In[34]:


sns.heatmap(df.isnull())


# In[35]:


dup = df.duplicated().any()
print("are dup?",dup)


# In[36]:


df = df.drop_duplicates()
print("are dup?",dup)


# In[37]:


dup = df.duplicated().any()
print("are dup?",dup)


# In[38]:


df.head()


# In[39]:


df['subject'].value_counts()


# In[50]:


import  matplotlib.pyplot as plt
df['subject'] = df['subject'].astype('category')

# Count the occurrences of each unique value in the 'subject' column
subject_counts = df['subject'].value_counts()

# Plotting the countplot using the counts
sns.barplot(x=subject_counts.index, y=subject_counts.values)
plt.xlabel("Sub",fontsize=13)
plt.ylabel('No. of people ')
plt.show()


plt.xticks(rotation = 70)
plt.show()


# In[52]:


#which level udemy provide courses
df['level'].value_counts()


# In[55]:


subject_counts = df['level'].value_counts()

# Plotting the countplot using the counts
sns.barplot(x=subject_counts.index, y=subject_counts.values)
plt.xlabel("Sub",fontsize=13)
plt.ylabel('No. of people ',fontsize=13)
plt.show()


plt.xticks(rotation = 70)
plt.show()


# In[56]:


df.columns


# In[57]:


df['is_paid'].value_counts()


# In[59]:


subject_counts = df['is_paid'].value_counts()

# Plotting the countplot using the counts
sns.barplot(x=subject_counts.index, y=subject_counts.values)
plt.xlabel("Sub",fontsize=13)
plt.ylabel('No. of paid and free course ',fontsize=13)
plt.show()


plt.xticks(rotation = 70)
plt.show()


# In[60]:


df.groupby(['is_paid']).mean()


# In[65]:


sns.barplot( x="is_paid",y="num_subscribers",data=df)


# In[68]:


sns.barplot( x="level",y="num_subscribers",data=df)
plt.xticks(rotation=60)
plt.show()


# In[70]:


df.columns
#most popular course title


# In[72]:


df[df['num_subscribers'].max()==df['num_subscribers']]['course_title']


# In[75]:


#num course_title
top_10 =df.sort_values(by="num_subscribers",ascending=False).head(10)


# In[76]:


sns.barplot(x="num_subscribers",y="course_title",data=top_10)


# In[77]:


df.columns


# In[80]:


plt.figure(figsize=(10,4))
sns.barplot(x="subject",y = "num_reviews",data=df)


# In[83]:


plt.figure(figsize=(15,7))
sns.barplot(x="price",y = "num_reviews",data=df)


# In[ ]:




