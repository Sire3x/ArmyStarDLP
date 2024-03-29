import pyshark
import csv

def pcap_to_csv(input_pcap, output_csv):
    cap = pyshark.FileCapture(input_pcap)

    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header
        csv_writer.writerow(['Timestamp', 'Source IP', 'Destination IP', 'Protocol', 'Length'])

        for packet in cap:
            try:
                timestamp = float(packet.sniff_timestamp)
                source_ip = packet.ip.src
                dest_ip = packet.ip.dst
                protocol = packet.transport_layer  # This might be 'TCP', 'UDP', or 'ICMP'

                if hasattr(packet, 'length'):
                    length = int(packet.length)
                else:
                    length = len(packet)

                csv_writer.writerow([timestamp, source_ip, dest_ip, protocol, length])

            except AttributeError as e:
                # Skip packets without necessary attributes
                print(f"Skipping packet: {e}")

if __name__ == "__main__":
    input_pcap_file = "w.pcap"
    output_csv_file = "../TestingClasses/please.csv"

    pcap_to_csv(input_pcap_file, output_csv_file)
