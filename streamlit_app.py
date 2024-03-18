import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# Function to solve job sequencing problem
def job_sequencing(df):
    # Sort jobs based on profit in descending order
    df = df.sort_values(by='profit', ascending=False)
    
    # Initialize variables
    max_deadline = max(df['deadlines'])
    sequence = [''] * max_deadline
    total_profit = 0
    
    # Iterate through each job
    for index, row in df.iterrows():
        deadline = row['deadlines']
        # Find a slot before the deadline
        while deadline > 0:
            if sequence[deadline - 1] == '':
                sequence[deadline - 1] = row['jobID']
                total_profit += row['profit']
                break
            deadline -= 1
    
    return sequence, total_profit

# Load dataset
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Main function
def main():
    st.title('Job Sequencing Problem Solver')
    
    # Upload dataset
    st.sidebar.title('C:\Users\DELL\Downloads\jobs.csv')
    uploaded_file = st.sidebar.file_uploader('C:\Users\DELL\Downloads\jobs.csv', type='csv')
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        st.subheader('Dataset')
        st.write(df)
        
        # Solve job sequencing problem
        sequence, total_profit = job_sequencing(df)
        
        st.subheader('Job Sequence')
        st.write(sequence)
        
        st.subheader('Total Profit')
        st.write(total_profit)

if _name_ == '_main_':
    main()