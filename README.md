# ArmyStarDLP
An Army Sponsored Research project that aims to push the next generation of technology into the future, focused on data loss prevention through the use of a proxy server that would classify images, documents, and other specified information picked up off of network traffic.

# Introduction
The project aims to address cybersecurity threats stemming from data leaks via photographs transmitted over networks, with a three-phase approach. Phase 1 involves real-time packet capture to identify image data in network traffic. Phase 2 employs artificial intelligence, particularly convolutional neural networks, for image classification, distinguishing between sensitive and non-sensitive content. In Phase 3, decisions are made based on classification results, either allowing non-sensitive images to proceed or blocking the transmission of sensitive ones, potentially using packet manipulation or network filtering techniques. Real-world incidents like the FitBit data leak underscore the project's relevance, but challenges such as false positives/negatives, performance concerns, legal/ethical considerations, and adaptability to evolving threats must be addressed through collaboration with experts and rigorous testing before deployment.

# Phase One: Capturing The Packet
Developed code that allows us to capture network traffic using pyshark, a python extension of Wireshark, that when interrupted returns a .pcap file. This initial phase is pivotal as it lays the groundwork for subsequent analysis and investigation into potential security breaches. Without capturing network traffic, there is no basis for identifying vulnerabilities or enhancing security measures. We would then take this pcap file and upload it into a program called BruteShark. This allows us to recreate the data that was transmitted over the network in a straightforward process for a large amount of data. We then extract this data and it is returned as a file that contains all of the information included in the network capture. This can include modules such as DNS, File Extraction, Network Map Creation, Credentials Extractor (Passwords and Hashes), and VoIP Calls.

# Phase Two: Data Classification
We then take the file that was extracted from BruteShark and then upload it into a data classification process. This data classification system allows us to identify security breaches, through the use of a training set of data, and comparing data from that training set to anything that was extracted. By doing this we can see if any sensitive information is being sent out from a theoretical base or host. And, based on what we saw from the Packet Capture this classification system can show us exactly what is being sent from Point A to Point B. This is because all of these programs are running on a proxy server, which verifies that data being sent outside of a secure environment does not contain anything that may create a vulnerability or breach. Once we have used our data classification system it is either put into flagged or unflaged files.

# Phase Three: Post Processing
After getting a flagged and unflagged file that contains its respective information we can then move forward with post-processing. The issue that is dealt with now is how to ensure that the data captured that is flagged doesn't get sent out. We take the information that is flagged and deny it from being sent to its intended destination. This data that is flagged gets held back for further analysis to see what was sent specifically, and if there is a potential threat should it be sent. As for the unflagged data, we can alter the original capture so that only the files that are inside the unflagged folder end up being sent to their intended destination.

# Conclusion
The goal of this project is to ensure that secure facilities have the capabilities to prevent data breaches from occurring. Through the use of a proxy server and the phases/code described above it allows a secure environment to guarantee that nothing sensitive is being sent out. This can help improve security systems by finding weaknesses and insider threats that could be inside of an environment. Future integration of convolutional neural networks could enhance classification accuracy and adaptability to evolving threats, ultimately this program can be improved on and automated in the future.
