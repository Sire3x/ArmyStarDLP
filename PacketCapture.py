import matplotlib.pyplot as plt
import pyshark
import pandas as pd

"""Name: Tyler Furches, Parker Langenberg, Chad Dailey (DOG), Dylan Acosta, Dylan Wilson
Start Date 1/25/2024
Research Project: ADD A DESCRIPTION HERE"""


"""Notes from 1/25/2024: Live capture is working and packet data is printing inside of the PyCharm console below
 streamlit is no longer working and we are still trying to fix that and come to a consensus on how to get the data that is captured into the array to write into it
 I have tried writing the file as a csv file but even when i set data = read_csv and then use streamlit and pandas to write it is giving me an error and I am unsure as to why.
 
 Next Steps: With basic Data now captured the categorization of the data and what we can do with it is the next step.  Figuring out if it is secure as well as if it is too slow on a large scale
 is something that also needs to be considered as none of the runs done today lasted more than 30 seconds and at some points were still producing near 500 packets making the bar graph difficult to interpret."""
                 #If streamlit is being used must use cmd prompt and command -> "streamlit run ResearchProject.py"




###################################SECTION ONE OF THE PROJECT: Capturing Data/Wireshark Collection##################################################
#Goal of this section is to capture live data from wireshark and turn it into a CSV File, this CSV file will then be used
#In Section 2.  The idea is to turn a live capture of wireshark and turn that into a csv file that csv file will then be
#used by streamlit and turn into a data table for localhost.  Could also potentially trying manipulating a pcap file
#and messing around with that for streamlit if possible.


filename = input("Please Enter the Output File Name & have it end in .csv OR .pcap")    #Could make this work with static based off an Or statement
try:
    capture = pyshark.LiveCapture(interface='Wi-Fi', output_file=filename)          #These Two lines are Live Capture of the Wifi Network
    capture.sniff()


except KeyboardInterrupt:  #When run is interrupted, assuming at least 10 packets are captured it will go through all the packets
    print(capture)         #That were captured during the pyshark execution.  If a packet matches the terms "UDP,TCP, etc." Then
    if len(capture) > 10:  #It will print out the related packet information and the port it came from while appending additional information
        capture1 = pyshark.FileCapture(filename)
        ip = []
        for pkt in capture1:
            if("IP" in pkt):
                if ("UDP" in pkt):
                    print("IP:UDP Source " + pkt.ip.src, "\nUDP Port: " + pkt.udp.dstport + "\n")
                    ip.append([pkt.ip.src, pkt.udp.dstport])
                elif ("TCP" in pkt):
                    print("IP:TCP Source " + pkt.ip.src, "\nTCP Port: " + pkt.tcp.dstport + "\n")
                    ip.append([pkt.ip.src, pkt.tcp.dstport])                                                #The ip.append then adds the IP to the array which will be printed out later on
            elif ("IPV6" in pkt):
                if ("UDP" in pkt):
                    print("IPV6:UDP Source " + pkt.ipv6.src, "\nUDP Port: " + pkt.udp.dstport + "\n")
                    ip.append([pkt.ipv6.src, pkt.udp.dstport])
                elif ("TCP" in pkt):
                    print("IPV6:TCP Source " + pkt.ipv6.src, "\nTCP Port: " + pkt.tcp.dstport + "\n")
                    ip.append([pkt.ipv6.src, pkt.tcp.dstport])


#################################SECTION TWO OF THE PROJECT: Data Table/Pandas###################################################################

        data = pd.DataFrame(ip, columns=['sourceip', 'port'])
        data['port'] = data['port'].astype(int)
        data_crosstab = pd.crosstab(data['sourceip'], data['port'])     #These 3 lines and cross tab create the table that is printed out at the conclusion of the run time
        print(data_crosstab)
        data_crosstab.plot.bar(stacked=True)
        plt.show()  #Creates Bar Graph
    else:
        print("Not enough packets captured for execution")







#####################################################Testing Stuff###############################################################################################################
#Static Example with Grades

                                      #This is what actually writes to the local host, it is the streamline package that allows you to create the local host"""

#data = pd.read_csv("exams.csv")     #Reads in the CSV File (Data set) and assigns it to a variable, data

#st.subheader('Fixed Test Data Set as we Work')              #This is the title of the data set that will be displayed when creating the local host"""
#st.write(data)









