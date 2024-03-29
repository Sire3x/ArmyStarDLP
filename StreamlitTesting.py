import streamlit as st
import pandas as pd
import PCAPtoCSV as pc


# filename = input("Please Enter the Output File Name & have it end in .csv OR .pcap")    #Could make this work with static based off an Or statement

pc.pcap_to_csv("needle_in_a_haystack.pcap", "test3.csv")
#data = pd.read_csv("test3.csv")
#st.write(data)

