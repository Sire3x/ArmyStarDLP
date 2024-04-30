import matplotlib.pyplot as plt
import pyshark
import pandas as pd

"""Name: Tyler Furches, Parker Langenberg, Chad Dailey, Dylan Acosta, Dylan Wilson
Start Date 1/25/2024"""


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









