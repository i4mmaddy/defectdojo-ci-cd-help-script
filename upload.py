import requests
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script for import scan results into defectdojo using API v2')
    parser.add_argument('--host', help="Host eg: http://192.168.1.1 or https://defectdojo.com", required=True)
    parser.add_argument('--api_key', help="API V2 Key", required=True)
    parser.add_argument('--engagement_id', help="Engagement ID Mandatory", required=True)
    parser.add_argument('--result', help="Scanner output file", required=True)
    parser.add_argument('--scanner', help="Type of scanner", required=True)
    parser.add_argument('--date_of_scan', help="Date of the scan in YYYY-MM-DD eg: 2021-05-25", required=True)
    parser.add_argument('--build_id', help="Reference to external build id", required=False)

    # Parse out arguments
    args = vars(parser.parse_args())
    host = args["host"]
    api_key = args["api_key"]
    result_file = args["result_file"]
    scanner = args["scanner"]
    engagement_id = args["engagement_id"]
    date = args["date_of_scan"]





url = host
headers = {'Accept': 'application/json',
           'Authorization': 'Token'+ api_key}






files = {'file': open(result_file,'rb')}


formdata = {
    'scan_date': date,
    'minimum_severity': 'Info',
    'active': 'true',
    'verified':'true',
    'scan_type':scanner,
    'engagement':engagement_id,
    'push_to_jira':'false',
    'close_old_findings':'false'
}


print(headers)
print(formdata)






