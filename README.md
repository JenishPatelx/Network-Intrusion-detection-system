# Network-Intrusion-detection-system

Overview





The Intrusion Detection System (IDS) project is designed to monitor and analyze network traffic and system behavior to detect potential security threats. By combining multiple detection techniques such as signature-based detection and hybrid detection, the system identifies malicious activities, unauthorized access attempts, or abnormal behavior in real-time. The project uses various tools and libraries like Scapy, Pandas, and Scikit-learn to implement packet sniffing, data cleaning, feature extraction, and anomaly detection.

Project Structure



The project is organized into the following key components:




Packet Sniffer (monitoring): Captures network packets to monitor traffic in real-time using Scapy.
Data Cleaner (data_processing): Cleans and preprocesses raw data by removing duplicates and handling missing values.
Feature Extractor (data_processing): Extracts relevant features from the raw network traffic data, such as source IP, destination IP, and protocol.
Signature-based Detector (detection): Detects potential intrusions by comparing network traffic with predefined attack signatures.
Hybrid Detector (detection): Combines multiple detection techniques, including signature-based and anomaly-based detection, to enhance detection accuracy.
Event Logger (loging): Logs alerts and system events for monitoring and analysis.
Main Application (src/main.py): The main entry point for running the IDS, integrating all components for real-time detection and alerting.
Features
Real-time Network Traffic Monitoring: Captures network packets and logs the details like source IP, destination IP, and protocol.
Data Preprocessing: Cleans captured data by removing duplicates and handling missing values.
Intrusion Detection: Uses signature-based detection to compare traffic with known attack patterns and generate alerts.
Hybrid Detection: Combines different detection techniques for better accuracy and fewer false positives.
Logging and Alerting: Logs alerts to a file for monitoring and later analysis.
Working
1. Packet Sniffing
The system begins by capturing network packets using the Scapy library. It sniffs the network traffic on a given interface (e.g., eth0) for a defined number of packets. Each packet contains details like:

Source IP
Destination IP
Protocol (TCP/UDP)
For example, it might capture the following packet:

json
![image](https://github.com/user-attachments/assets/ab35afb8-5460-4e46-a747-d8795cc0ebe8)


2. Data Cleaning
Once the packets are captured, they are cleaned and preprocessed using the DataCleaner class. This involves removing duplicate packets and filling in missing values to ensure that the data is consistent and usable.

For example, if you have a list of packets with some duplicates, the cleaner removes them, resulting in a data frame with unique packet entries.

3. Feature Extraction
After cleaning the data, the FeatureExtractor class extracts meaningful features from the packets. These features might include:

Source IP address
Destination IP address
Protocol (TCP, UDP, etc.)
These features are extracted for use in the detection process.

4. Intrusion Detection
The system uses two types of detectors to identify potential threats:

Signature-based Detection: The SignatureBasedDetector class compares incoming traffic against a set of predefined attack signatures. If the traffic matches any known attack patterns, an alert is triggered.

For example, a packet with a source IP of 192.168.1.1 and a destination IP of 10.0.0.2 with a TCP protocol might match a known signature of a DoS attack, triggering an alert.

Hybrid Detection: The HybridDetector combines signature-based detection with other techniques (e.g., anomaly detection, machine learning). This allows the system to detect new or unknown types of attacks that may not be in the signature database.

5. Event Logging
When an intrusion is detected, an alert is logged by the EventLogger class. The alerts are saved to a log file for further analysis. For example, the alert might look like:


Alert: Intrusion detected at index 3: {'source_ip': '192.168.1.1', 'destination_ip': '10.0.0.2', 'protocol': 'TCP'}
6. Real-time Operation
Once set up, the system continuously monitors network traffic, cleans the data, extracts features, and applies detection techniques in real-time. Alerts are generated whenever suspicious activity is detected, providing proactive security monitoring.

Installation
Clone the repository:

git clone https://github.com/your-username/IDS_Project.git


Navigate to the project directory:

cd IDS_Project


Install required dependencies:


pip install -r requirements.txt


Run the main script:


python src/main.py


Dependencies
Scapy: For packet sniffing and manipulation.
Pandas: For data manipulation and cleaning.
Scikit-learn: For machine learning (if you add any models for anomaly detection).
Logging: For logging alerts and system events.
Example Output

![image](https://github.com/user-attachments/assets/9b6a9200-e11e-41f1-87ad-1d0b52656962)

Future Improvements


Anomaly Detection: Implement machine learning-based anomaly detection techniques to identify unknown attack patterns.
Real-time Dashboard: Create a real-time dashboard using tools like Grafana or Kibana for better visualization of network traffic and alerts.
Distributed IDS: Extend the system to handle larger networks by distributing the monitoring across multiple nodes.



Contributing


If you'd like to contribute to the project, feel free to fork the repository, create a new branch, and submit a pull request. Contributions to improve detection accuracy or add new features are welcome.
